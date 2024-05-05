from helper import load_mistral_api_key, mistral
load_mistral_api_key()

email = """
Dear mortgage lender, 

What's your 30-year fixed-rate APR, how is it compared to the 15-year 
fixed rate?

Regards,
Anna
"""

prompt = f"""
You are a mortgage lender customer service bot, and your task is to 
create personalized email responses to address customer questions.
Answer the customer's inquiry using the provided facts below. Ensure 
that your response is clear, concise, and directly addresses the 
customer's question. Address the customer in a friendly and 
professional manner. Sign the email with "Lender Customer Support."   

# Facts
30-year fixed-rate: interest rate 6.403%, APR 6.484%
20-year fixed-rate: interest rate 6.329%, APR 6.429%
15-year fixed-rate: interest rate 5.705%, APR 5.848%
10-year fixed-rate: interest rate 5.500%, APR 5.720%
7-year ARM: interest rate 7.011%, APR 7.660%
5-year ARM: interest rate 6.880%, APR 7.754%
3-year ARM: interest rate 6.125%, APR 7.204%
30-year fixed-rate FHA: interest rate 5.527%, APR 6.316%
30-year fixed-rate VA: interest rate 5.684%, APR 6.062%

# Email
{email}
"""

response = mistral(prompt)
print(response)

# Dear Anna,
#
# Thank you for reaching out to us. I'm happy to help you with your mortgage rate inquiries.
#
# Our current 30-year fixed-rate mortgage has an Annual Percentage Rate (APR) of 6.484%. In comparison, the 15-year fixed-rate mortgage has an APR of 5.848%. As you can see, the APR for the 15-year term is lower than the 30-year term.
#
# This difference is due to the fact that the 15-year mortgage has a shorter term, which means you will pay off your loan more quickly. This results in less interest being paid over the life of the loan, leading to a lower APR. However, the monthly payments for a 15-year mortgage will be higher than those for a 30-year mortgage due to the shorter repayment period.
#
# I hope this information helps. Please let me know if you have any other questions.
#
# Best regards,
# Lender Customer Support
