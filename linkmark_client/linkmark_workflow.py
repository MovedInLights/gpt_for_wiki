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

    def make_request(self):
        logging.info(
            f'Requesting name {self.tm_name} '
            f'for {self.classes_for_search} '
            f'in {self.search_type}'
        )
        response = requests.post(
            LINKMARK_URL,
            data={
                'search': self.tm_name,
                'search_2': None,
                'vena-class': 'Выбрать',
                'search_4': None,
                'mktu1[]': self.classes_for_search,
                'vena_limit_subclass': '0',
                'vena_limit_heading': '12',
                'search_type': self.search_type,
            },
            headers={'DNT': '1'},
        )
        logging.info(f'Request response {response}')
        return response

    @abstractmethod
    def handle_response(self, response):
        ...


class WordSearch(BaseSearchType):
    def make_request(self):
        ...

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


class CompanySearch(BaseSearchType):
    pass


class NumberSearch(BaseSearchType):
    pass


def linkmark_request(tm_name, classes_for_search):
    logging.info(f'Requesting linkmark for {tm_name} with classes {classes_for_search}')
    response = requests.post(
        LINKMARK_URL,
        data={
            'search': tm_name,
            'search_2': None,
            'vena-class': 'Выбрать',
            'search_4': None,
            'mktu1[]': classes_for_search,
            'vena_limit_subclass': '0',
            'vena_limit_heading': '12',
            'search_type': '1',
        },
        headers={'DNT': '1'},
    )

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
        'tm_name': tm_name,
        'classes_for_search': classes_for_search,
        'results': result['res'],
        'data_for_chat': data_for_chat_json,
        'tm_name_list': tm_name_list,
    }
    return context
