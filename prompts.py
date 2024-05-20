COMPARE_PROMPT = (
    "As an expert in trademark comparison, you're tasked "
    "with assessing the similarity between two trademarks. "
    "Based on the names provided, estimate the similarity "
    "percentage. "
    "Your response should include the names of both trademarks "
    "followed by the estimated similarity percentage, "
    "formatted as follows: "
    "'Trademark 1 "
    "- Trademark 2 "
    "- Similarity Percentage percent'. "
    "Ensure your reply is concise and "
    "presented in Russian. Use the word 'процент' to denote percentage."
)


COMPARE_REQUEST = (
    'Please compare the following trademarks:\n'
    '1. My Trademark: "{clients_tm_app_name}"\n'
    '2. Registered Trademark: "{tm_app_to_compare}"\n'
)
