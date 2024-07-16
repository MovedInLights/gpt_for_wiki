import json
import logging
from abc import ABC, abstractmethod
from enum import Enum

import requests
from bs4 import BeautifulSoup

LINKMARK_URL = 'https://linkmark.ru/search'


class SearchType(str, Enum):
    WORD = '1'
    NUMBER = '3'
    COMPANY = '4'


class BaseSearchType(ABC):
    def __init__(self, search_type: SearchType, tm_name, classes_for_search):
        self.search_type = search_type
        self.tm_name = tm_name
        self.classes_for_search = classes_for_search
        logging.info(
            f'Initialized BaseSearchType with search_type={self.search_type}, '
            f'tm_name={self.tm_name}, classes_for_search={self.classes_for_search}'
        )
        self.request = {
            'search': self.tm_name,
            'search_2': None,
            'vena-class': 'Выбрать',
            'search_4': None,
            'mktu1[]': self.classes_for_search,
            'vena_limit_subclass': '0',
            'vena_limit_heading': '12',
            'search_type': self.search_type,
        }

    def make_request(self):
        logging.info(
            f'Requesting name {self.tm_name} '
            f'for {self.classes_for_search} '
            f'in {self.search_type} '
            f'with request {self.request}'
        )
        response = requests.post(
            LINKMARK_URL,
            data=self.request,
            headers={'DNT': '1'},
        )
        logging.info(f'Request response {response.text}')
        return response

    @abstractmethod
    def handle_response(self, response):
        ...


class WordSearch(BaseSearchType):
    def handle_response(self, response):
        parsed_html = BeautifulSoup(response.text, 'html.parser')

        monitoring_add_link = parsed_html.select(
            '#search-form > div.row > div.monitoring-add-wrapper > a'
        )
        req_id = monitoring_add_link[0].get('req-id')

        response = requests.post(
            f'https://linkmark.ru/request.json/{req_id}',
            data={'type': 'm', 'num': '20', 'offset': '0'},
            headers={'DNT': '1', 'X-Requested-With': 'XMLHttpRequest'},
        )
        result = response.json()

        tm_name_list = []
        for index, item in enumerate(result['res']):
            logging.info(
                f'Processing {item} {type(item)}, item words are '
                f'{item["words"]}, json: {json.loads(item["icgs"])}'
            )
            item['icgs'] = json.loads(item['icgs'])
            item['id'] = index
            if item['status'] != 1:
                tm_name_list.append(item.get('words', ''))

        logging.info(f'Finished processing {tm_name_list} items')

        data_for_chat = [
            {
                'status': tm.get('status', ''),
                'formatted_reg_date': tm.get('formatted_reg_date', ''),
                'link': tm.get('link', ''),
                'doc_num': tm.get('doc_num', ''),
                'src_image_link': tm.get('src_image_link', ''),
                'words': tm.get('words', ''),
                'formatted_priority_date': tm.get('formatted_priority_date', ''),
                'owner': tm.get('owner', ''),
                'code': tm.get('code', ''),
                'id': tm.get('id', ''),
            }
            for tm in result['res']
        ]
        data_for_chat_json = json.dumps(data_for_chat)

        logging.info(f'Working with the results: {result["res"]}')
        context = {
            'tm_name': self.tm_name,
            'classes_for_search': self.classes_for_search,
            'results': result['res'],
            'data_for_chat': data_for_chat_json,
            'tm_name_list': tm_name_list,
        }
        return context


class NumberSearch(BaseSearchType):
    def handle_response(self, response):
        trademarks = []
        parsed_html = BeautifulSoup(response.text, 'html.parser')
        items = parsed_html.select('div.result-div-item-wrapper')

        for item in items:
            table = item.select('div.result-div-item-v2 > table')[0]
            try:
                status = item.select(
                    'div.result-div-item-status.tm_status.status_2 > div'
                )[0].text
            except IndexError:
                status = item.select(
                    'div.result-div-item-status.tm_status.status_4 > div'
                )[0].text

            link = item.select("div.result-div-item-action > a")[0].attrs['href']

            ths, tds = table.select('th'), table.select('td')
            result = {
                th.text.strip().replace(':', ''): td.text.strip()
                for th, td in zip(ths, tds)
            }

            for old_key, new_key in key_map.items():
                if old_key in result:
                    if new_key == 'icgs':
                        result[new_key] = [
                            {'code': icgs_raw}
                            for icgs_raw in result.pop(old_key).split(', ')
                        ]
                    elif new_key == 'owner':
                        result[new_key] = {'name': result.pop(old_key)}
                    else:
                        result[new_key] = result.pop(old_key)

            result['status'] = status
            result['link'] = link
            try:
                result['src_image_link'] = get_tm_app_picture(result['tm_app_num'])
            except KeyError:
                result['src_image_link'] = get_tm_picture(result['doc_num'])

            trademarks.append(result)

        context = {
            'tm_name': self.tm_name,
            'results': trademarks,
        }
        return context


class CompanySearch(BaseSearchType):
    pass


def get_tm_picture(tm_number):
    tm_number_with_zeros = tm_number.zfill(7)

    url = (
        f'https://fips.ru/ofpstorage/Doc/TM/RUNWTM/000/000/'
        f'{tm_number_with_zeros[:3]}/'
        f'{tm_number_with_zeros[3:6]}/'
        f'{tm_number_with_zeros[6]}00/'
        f'ТЗ-{tm_number}-00001/00000001.jpg'
    )
    return url


def get_tm_app_picture(tm_number):
    return (
        f'https://fips.ru/Image/RUTMAP_Images/'
        f'new{tm_number[:4]}/'
        f'{tm_number[4]}00000/'
        f'{tm_number[4]}'
        f'{tm_number[5]}0000/'
        f'{tm_number[4]}'
        f'{tm_number[5]}'
        f'{tm_number[6]}000/'
        f'{tm_number}.jpg'
    )


key_map = {
    'Свидетельство': 'doc_num',
    'Приоритет': 'formatted_priority_date',
    'Дата подачи': 'formatted_reg_date',
    'Дата регистрации': 'formatted_reg_date',
    'МКТУ': 'icgs',
    'Заявленные классы': 'icgs',
    'Правообладатель': 'owner',
    '№ заявки': 'tm_app_num',
    'Заявитель': 'owner',
}
