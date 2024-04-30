from chat_processor import ChatClient

# Подумать над тем, чтобы 2 чата было, один парсит картинку, другой проверяет


def test_chat_with_gpt(request):
    tm_name = request.POST.get('clients_tm_app_name', '')
    registered_tm_to_compare = request.POST.get('tm_to_compare', '')

    # registered_tm_to_compare_base_64 = convert_image_to_base64(
    # registered_tm_to_compare)

    request_text = (
        f'Please compare the following trademarks:\n'
        f'1. My Trademark: "{tm_name}"\n'
        f'2. Registered Trademark: "{registered_tm_to_compare}"\n'
    )

    prompt_content = (
        "As an expert in trademark comparison, you're tasked "
        "with assessing the similarity between two trademarks. "
        "Based on the names provided, estimate the similarity "
        "percentage. "
        "Your response should include the names of both trademarks "
        "followed by the estimated similarity percentage, "
        "formatted as follows: "
        "'Trademark 1 - Trademark 2 - Similarity Percentage percent'. "
        "Ensure your reply is concise and "
        "presented in Russian. Use the word 'процент' to denote percentage."
    )

    chat_client = ChatClient()
    result = chat_client.chat_with_gpt(
        prompt_content=prompt_content, request_text=request_text
    )
    # context = {
    #     'tm_name': data_for_chat,
    # }
    return {'result': result}


# TODO Нужно указать какой знак зарегистрирован, какой из них новый.
# TODO Промпты нужно писать на английском
# TODO Сделать обозначения параметрами через гет
# TODO Проверку сходства знаков нужно сохранять в базе, чтобы не тратить токены.
