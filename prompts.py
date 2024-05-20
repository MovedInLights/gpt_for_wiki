FINAL_MESSAGE_PROMPT = (
    'Your trademark "{Trademark1}" - '
    'Registered trademark "{Trademark2}" - '
    'Similarity percentage: {SimilarityPercentage}%. '
    'Opposition probability: {Prediction}.'
)


COMPARE_PROMPT = (
    "As an expert in trademark comparison, "
    "assess the similarity between the following two trademarks. "
    "Based on their names, estimate the similarity percentage "
    "and the likelihood of opposition. "
    "Format your response as follows: {FINAL_MESSAGE_PROMPT} "
    "Ensure your reply is concise and in Russian. "
    "Use 'Your trademark' for the user's trademark, "
    "'Registered trademark' for the registered trademark, "
    "'percent' for percentage, and one of the following terms "
    "for opposition probability: "
    "'very low', 'low', 'average', 'high', 'very high'. "
    "Place the names of the trademarks within curly brackets."
)

COMPARE_REQUEST = (
    'Please, compare the following trademarks:\n'
    '1. User trademark: "{clients_tm_app_name}"\n'
    '2. Registered trademark: "{tm_app_to_compare}"\n'
)
