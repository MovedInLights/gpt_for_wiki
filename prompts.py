FINAL_MESSAGE_PROMPT = (
    'Your trademark "{Trademark1}" - '
    'Registered trademark "{Trademark2}" - '
    'Similarity percentage: {SimilarityPercentage}%. '
    'Opposition probability - {Prediction}.'
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
    "Use the phrase 'Your trademark' to denote the user's trademark. "
    "Use the phrase 'Registered trademark' "
    "to denote the registered trademark. "
    "Use the word 'percent' to denote percentage. "
    "For the likelihood of opposition, "
    "use one of the following terms based on the similarity percentage: "
    "'very low', 'low', 'average', 'high', 'very high'."
)

COMPARE_REQUEST = (
    'Пожалуйста, сравните следующие товарные знаки:\n'
    '1. Моё обозначение: "{clients_tm_app_name}"\n'
    '2. Зарегистрированный товарный знак: "{tm_app_to_compare}"\n'
)
