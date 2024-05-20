FINAL_MESSAGE_PROMPT = (
    'Ваше обозначение "{Trademark1}" - '
    'Зарегистрированный товарный знак "{Trademark2}" - '
    'Процент сходства: {SimilarityPercentage}%. '
    'Вероятность противопоставления ФИПС - {Prediction}.'
)

COMPARE_PROMPT = (
    "As an expert in trademark comparison, "
    "you need to assess the similarity between two trademarks. "
    "Based on the provided names, estimate the similarity percentage "
    "and the likelihood of opposition. "
    "Your response should include the names of both trademarks "
    "followed by the estimated similarity percentage and the likelihood of opposition, "
    f"formatted as follows: {FINAL_MESSAGE_PROMPT} "
    "Ensure your reply is concise and presented in Russian. "
    "Use the phrase 'Ваше обозначение' to denote the user's trademark. "
    "Use the phrase 'Зарегистрированный товарный знак' "
    "to denote the registered trademark. "
    "Use the word 'процент' to denote percentage. "
    "For the likelihood of opposition, "
    "use one of the following terms based on the similarity percentage: "
    "'очень низкая', 'низкая', 'умеренная', 'высокая', 'очень высокая'."
)

COMPARE_REQUEST = (
    'Пожалуйста, сравните следующие товарные знаки:\n'
    '1. Моё обозначение: "{clients_tm_app_name}"\n'
    '2. Зарегистрированный товарный знак: "{tm_app_to_compare}"\n'
)
