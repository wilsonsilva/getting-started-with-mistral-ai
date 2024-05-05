# Prompting 

In this lesson, you will learn how to access and prompt Mistral models via API calls and perform various tasks like classification, information extraction, personalization and summarization.

Let's start coding. In the classroom, the libraries are already installed for you, but if you're running this or your own machine, you will want to install the following:

`pip install mistralai`

Let's just comment this out because we don't need to run this in this session.

### Load API key and helper function

We have a helper function here to help you load the Mistral API key

```python
from helper import load_mistral_api_key
load_mistral_api_key()
```

and another helper function here for you to load the Mistral models so you can get started running Mistral API easily 

```python
from helper import mistral
mistral("hello, what can you do?")
```

Okay, ask the model. *Hello, what can you do?* At the end of this lesson, I will walk you through the code in the helper function, so that you can see how the API calls works and use the API outside of this classroom environment.

## Classification

First, let's take a look at how you can use our models to classify bank customer inquiries. In this prompt, you are a bank customer service bot. Your task is to assess customer intent and categorize customer inquiry. We have a list of predefined categories. If the text doesn't fit in any of the categories, classify it as customer service. Then you can see here we're providing some examples for the model to know exactly what we're expecting.

```python
prompt = """
    You are a bank customer service bot. 
    Your task is to assess customer intent and categorize customer 
    inquiry after <<<>>> into one of the following predefined categories:
    
    card arrival
    change pin
    exchange rate
    country support 
    cancel transfer
    charge dispute
    
    If the text doesn't fit into any of the above categories, 
    classify it as:
    customer service
    
    You will only respond with the predefined category. 
    Do not provide explanations or notes. 
    
    ###
    Here are some examples:
    
    Inquiry: How do I know if I will get my card, or if it is lost? I am concerned about the delivery process and would like to ensure that I will receive my card as expected. Could you please provide information about the tracking process  for my card, or confirm if there are any indicators to identify if the card has been lost during delivery?
    Category: card arrival
    Inquiry: I am planning an international trip to Paris and would like to inquire about the current exchange rates for Euros as well as any associated fees for foreign transactions.
    Category: exchange rate 
    Inquiry: What countries are getting support? I will be traveling and living abroad for an extended period of time, specifically in France and Germany, and would appreciate any information regarding compatibility and functionality in these regions.
    Category: country support
    Inquiry: Can I get help starting my computer? I am having difficulty starting my computer, and would appreciate your expertise in helping me troubleshoot the issue. 
    Category: customer service
    ###
    
    <<<
    Inquiry: {inquiry}
    >>>
    Category:
"""
```

#### Ask Mistral to check the spelling and grammar of your prompt

Okay. If we want to make sure our prompt doesn't have any spelling or grammar error, we can ask the model to correct the spelling and grammar first. Let's run this.

```python
response = mistral(f"Please correct the spelling and grammar of \
this prompt and return a text that is the same prompt,\
with the spelling and grammar fixed: {prompt}")  
```

And then let's print the response.

```python
print(response)
```

#### Try out the model  

We can see that it made some grammar corrections. For example, _customer inquiry_ is now _the customer inquiry_. Now we can use this corrected prompt and replace the inquiry with the actual inquiry.

```python
mistral(
    response.format(
        inquiry="I am inquiring about the availability of your cards in the EU"
    )
)
```

I am inquiring about the availability of your cards in the EU. And then let's run the sale and we get country support, which is what we expect.

```python
'country support'
```

Now let's run another inquiry. _What is the weather today?_

```python
mistral(
    response.format(
        inquiry="What's the weather today?"
    )
)
```

```python
'customer service'
```

Because this is not in any of the predefined categories. The model correctly categorize it as `customer service`.

Now let's come back to take a closer look at this prompt and see what kind of prompt technique we used. First of all, we use role play to provide our model a role, which is a bank customer service bot. This as personal context to the model.

```
You are a bank customer service bot
```

Second, we used few shot learning, where we give a few examples in the prompts. Learning can often improve model performance, especially when the task is difficult or when we want the model to respond in a specific manner. 

``` 
###
Here are some examples:

Inquiry: How do I know if I will get my card, or if it is lost? I am concerned about the delivery process and would like to ensure that I will receive my card as expected. Could you please provide information about the tracking process  for my card, or confirm if there are any indicators to identify if the card has been lost during delivery?
Category: card arrival
Inquiry: I am planning an international trip to Paris and would like to inquire about the current exchange rates for Euros as well as any associated fees for foreign transactions.
Category: exchange rate 
Inquiry: What countries are getting support? I will be traveling and living abroad for an extended period of time, specifically in France and Germany, and would appreciate any information regarding compatibility and functionality in these regions.
Category: country support
Inquiry: Can I get help starting my computer? I am having difficulty starting my computer, and would appreciate your expertise in helping me troubleshoot the issue. 
Category: customer service
###
```

Third, we use delimiters like hash or angle brackets to specify the boundary between different sections of the text. In our example, we use the triple hash to indicate examples and angled bracket to indicate customer inquiry.

```
###
examples
###

<<<
customer inquiry
>>>
```

And finally, in a case when the model is verbose, we can add: "do not provide explanations or notes", to make sure the output is concise. If you're wondering which deminetor to use, it doesn't matter as choose whichever you prefer.

## Information Extraction with JSON Mode

Next, I would like to show you an example of information extraction. We have seen many cases where information extraction can be useful. In this example, let's say you have some medical notes and you would like to extract some information from this text.

```python
medical_notes = """
A 60-year-old male patient, Mr. Johnson, presented with symptoms
of increased thirst, frequent urination, fatigue, and unexplained
weight loss. Upon evaluation, he was diagnosed with diabetes,
confirmed by elevated blood sugar levels. Mr. Johnson's weight
is 210 lbs. He has been prescribed Metformin to be taken twice daily
with meals. It was noted during the consultation that the patient is
a current smoker. 
"""
```

In this prompt, we provide the medical notes and ask the model to return JSON format with the following JSON schema, where we define what we want to extract, the type of this variable, and the list of output options.

```python
prompt = f"""
Extract information from the following medical notes:
{medical_notes}

Return json format with the following JSON schema: 

{{
        "age": {{
            "type": "integer"
        }},
        "gender": {{
            "type": "string",
            "enum": ["male", "female", "support"]
        }},
        "diagnosis": {{
            "type": "string",
            "enum": ["migraine", "diabetes", "arthritis", "acne"]
        }},
        "weight": {{
            "type": "integer"
        }},
        "smoking": {{
            "type": "string",
            "enum": ["yes", "no"]
        }}
}}
"""
```

For example, for diagnosis, the model should output one of these four options. Let's run this one. And when we run the model, we get exact format of what we defined.

```json
{"age":  60, "gender":  "male", "diagnosis":  "diabetes", "weight": 210, "smoking":  "yes"}
```

Here in the Mistral function. We defined it JSON as true to enable JSON mode.

```python
response = mistral(prompt, is_json=True)
print(response)
```

We'll go through the Python API calls at the end of the lesson. 

Let's take a look at this prompt again. What strategy we use here is that we explicitly ask in the prompt to return JSON format. __It's important to ask for the JSON format when we enable the JSON mode__. Another strategy we use here, is that we define the JSON schema. We use this JSON schema in the prompt to ensure the consistency and structure of the JSON output. Note, that if we don't have the is JSON equals true. The output may still be a JSON format, but we recommend you to enable the JSON mode to return a __reliable__ JSON format.

## Personalisation
 
Next, let's take a look at how our models can create personalized email responses to address customer questions. Because large language models are really good at personalization tasks. Here's an email where the customer, Anna, is asking the mortgage lender about the mortgage rate.

```python
email = """
Dear mortgage lender, 

What's your 30-year fixed-rate APR, how is it compared to the 15-year 
fixed rate?

Regards,
Anna
"""
```

And here is our prompt.

```python
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
```

You are a mortgage lender customer service bot, and your task is to create personalized email responses to address customer questions, answer the customer's inquiry using the provided facts below. And then we have some numbers about the interest rates in the prompts. And similar to what we have seen before, we use the string format to add the actual email content to this email variable here. Let's run the cell.

```python
response = mistral(prompt)
print(response)
```

```
Dear Anna,

Thank you for reaching out to us. I'm happy to help you with your mortgage rate inquiries.

Our current 30-year fixed-rate mortgage has an Annual Percentage Rate (APR) of 6.484%. In comparison, the 15-year fixed-rate mortgage has an APR of 5.848%. As you can see, the APR for the 15-year term is lower than the 30-year term.

This difference is due to the fact that the 15-year mortgage has a shorter term, which means you will pay off your loan more quickly. This results in less interest being paid over the life of the loan, leading to a lower APR. However, the monthly payments for a 15-year mortgage will be higher than those for a 30-year mortgage due to the shorter repayment period.

I hope this information helps. Please let me know if you have any other questions.
 
Best regards,
Lender Customer Support
```

As you can see, we get a personalized email to Anna answering her questions based on the facts provided. With this kind of prompt, you can imagine that you can easily create your own customer service bot. Answer questions about your product. It's important to use clear and concise language when presenting these facts or your product information. This can help the model to provide accurate and quick responses to customer queries.

## Summarization

```python
newsletter = """
European AI champion Mistral AI unveiled new large language models and formed an alliance with Microsoft. 

What’s new: Mistral AI introduced two closed models, Mistral Large and Mistral Small (joining Mistral Medium, which debuted quietly late last year). Microsoft invested $16.3 million in the French startup, and it agreed to distribute Mistral Large on its Azure platform and let Mistral AI use Azure computing infrastructure. Mistral AI makes the new models available to try for free here and to use on its La Plateforme and via custom deployments.

Model specs: The new models’ parameter counts, architectures, and training methods are undisclosed. Like the earlier, open source Mistral 7B and Mixtral 8x7B, they can process 32,000 tokens of input context. 

Mistral Large achieved 81.2 percent on the MMLU benchmark, outperforming Anthropic’s Claude 2, Google’s Gemini Pro, and Meta’s Llama 2 70B, though falling short of GPT-4. Mistral Small, which is optimized for latency and cost, achieved 72.2 percent on MMLU.
Both models are fluent in French, German, Spanish, and Italian. They’re trained for function calling and JSON-format output.
Microsoft’s investment in Mistral AI is significant but tiny compared to its $13 billion stake in OpenAI and Google and Amazon’s investments in Anthropic, which amount to $2 billion and $4 billion respectively.
Mistral AI and Microsoft will collaborate to train bespoke models for customers including European governments.
Behind the news: Mistral AI was founded in early 2023 by engineers from Google and Meta. The French government has touted the company as a home-grown competitor to U.S.-based leaders like OpenAI. France’s representatives in the European Commission argued on Mistral’s behalf to loosen the European Union’s AI Act oversight on powerful AI models. 

Yes, but: Mistral AI’s partnership with Microsoft has divided European lawmakers and regulators. The European Commission, which already was investigating Microsoft’s agreement with OpenAI for potential breaches of antitrust law, plans to investigate the new partnership as well. Members of President Emmanuel Macron’s Renaissance party criticized the deal’s potential to give a U.S. company access to European users’ data. However, support French lawmakers support the relationship.

Why it matters: The partnership between Mistral AI and Microsoft gives the startup crucial processing power for training large models and greater access to potential customers around the world. It gives the tech giant greater access to the European market. And it gives Azure customers access to a high-performance model that’s tailored to Europe’s unique regulatory environment.

We’re thinking: Mistral AI has made impressive progress in a short time, especially relative to the resources at its disposal as a startup. Its partnership with a leading hyperscaler is a sign of the tremendous processing and distribution power that remains concentrated in the large, U.S.-headquartered cloud companies.
"""
``` 

Finally, we have summarization. Summarization is a common task for large language models, and our model can do a really good job as summarization. Let's say you want to summarize [this newsletter from The Batch](https://www.deeplearning.ai/the-batch/mistral-enhances-ai-landscape-in-europe-with-microsoft-partnership-and-new-language-models):

```python
newsletter = """
European AI champion Mistral AI unveiled new large language models and formed an alliance with Microsoft. 

What’s new: Mistral AI introduced two closed models, Mistral Large and Mistral Small (joining Mistral Medium, which debuted quietly late last year). Microsoft invested $16.3 million in the French startup, and it agreed to distribute Mistral Large on its Azure platform and let Mistral AI use Azure computing infrastructure. Mistral AI makes the new models available to try for free here and to use on its La Plateforme and via custom deployments.

Model specs: The new models’ parameter counts, architectures, and training methods are undisclosed. Like the earlier, open source Mistral 7B and Mixtral 8x7B, they can process 32,000 tokens of input context. 

Mistral Large achieved 81.2 percent on the MMLU benchmark, outperforming Anthropic’s Claude 2, Google’s Gemini Pro, and Meta’s Llama 2 70B, though falling short of GPT-4. Mistral Small, which is optimized for latency and cost, achieved 72.2 percent on MMLU.
Both models are fluent in French, German, Spanish, and Italian. They’re trained for function calling and JSON-format output.
Microsoft’s investment in Mistral AI is significant but tiny compared to its $13 billion stake in OpenAI and Google and Amazon’s investments in Anthropic, which amount to $2 billion and $4 billion respectively.
Mistral AI and Microsoft will collaborate to train bespoke models for customers including European governments.
Behind the news: Mistral AI was founded in early 2023 by engineers from Google and Meta. The French government has touted the company as a home-grown competitor to U.S.-based leaders like OpenAI. France’s representatives in the European Commission argued on Mistral’s behalf to loosen the European Union’s AI Act oversight on powerful AI models. 

Yes, but: Mistral AI’s partnership with Microsoft has divided European lawmakers and regulators. The European Commission, which already was investigating Microsoft’s agreement with OpenAI for potential breaches of antitrust law, plans to investigate the new partnership as well. Members of President Emmanuel Macron’s Renaissance party criticized the deal’s potential to give a U.S. company access to European users’ data. However, support French lawmakers support the relationship.

Why it matters: The partnership between Mistral AI and Microsoft gives the startup crucial processing power for training large models and greater access to potential customers around the world. It gives the tech giant greater access to the European market. And it gives Azure customers access to a high-performance model that’s tailored to Europe’s unique regulatory environment.

We’re thinking: Mistral AI has made impressive progress in a short time, especially relative to the resources at its disposal as a startup. Its partnership with a leading hyperscaler is a sign of the tremendous processing and distribution power that remains concentrated in the large, U.S.-headquartered cloud companies.
"""
```

And here's the prompt I tried:

```python
prompt = f"""
You are a commentator. Your task is to write a report on a newsletter. 
When presented with the newsletter, come up with interesting questions to ask,
and answer each question. 
Afterward, combine all the information and write a report in the markdown
format. 

# Newsletter: 
{newsletter}

# Instructions: 
## Summarize:
In clear and concise language, summarize the key points and themes 
presented in the newsletter.

## Interesting Questions: 
Generate three distinct and thought-provoking questions that can be 
asked about the content of the newsletter. For each question:
- After "Q: ", describe the problem 
- After "A: ", provide a detailed explanation of the problem addressed 
in the question.
- Enclose the ultimate answer in <>.

## Write a analysis report
Using the summary and the answers to the interesting questions, 
create a comprehensive report in Markdown format. 
"""
```

You are a commentator. Your task is to write a report on the newsletter. When presented with the newsletter, come up with interesting questions to ask and answer each question. Afterward, combine all the information and write a report in the markdown format. Then I have a section to insert the content of the newsletter and a section for instructions.

First, to summarize key points.

```markdown
# Instructions: 
## Summarize:
In clear and concise language, summarize the key points and themes 
presented in the newsletter.
```

Second is to generate three distinct and thought provoking questions.

```markdown
## Interesting Questions: 
Generate three distinct and thought-provoking questions that can be 
asked about the content of the newsletter. For each question:
- After "Q: ", describe the problem 
- After "A: ", provide a detailed explanation of the problem addressed 
in the question.
- Enclose the ultimate answer in <>.
```

Third is to write an analysis report.

```markdown
## Write a analysis report
Using the summary and the answers to the interesting questions, 
create a comprehensive report in Markdown format. 
```

Let's run our Mistral Model:

```python
response = mistral(prompt)
print(response)
```

```markdown

```

And this is exactly what we asked for. We get a summary, we get interesting questions, and we get the analysis report. Of course, you can always ask the model to summarize the newsletter without these instructions. If you have a complex task providing step by step instructions, usually help the model to use a series of intermediate reasoning steps to solve complex tasks. In our example, using these steps might help the model think in each step and generate a more comprehensive report. One interesting strategy here is that we ask the model to automatically guide the reasoning and understanding process by generating examples with explanations and steps. Another strategy that's used often is that you can ask the model to, output in a certain format. For example, using a markdown format.

So that's all the prompts I want to show you in this lesson. In this lesson, we used a helper function to help us load the Mistral model. Here's how the API call works. We first need to define the Mistral client. You will want to replace this API key variable with your own API key. If you are running Mistral models outside the classroom environment. We also need to define the chat messages. The chat message can start with a user message, or a system message, or in a system message. A system message usually sets the behavior and context for the AI assistant, but is optional. You can have both the system message and the user message just in the user message, and experiment and see which kind of messages produced better result. In this lesson, we'll just have everything in the user message. Then we define how we can get the model response where we need to define the model and the messages. If we enable the JSON mode, we need to add a line here. Response format type as JSON object. To specify that we want the response format as JSON. There are several other not required arguments we can change here. You can check the API specs to see all the details.

Okay, so that's it for this lesson. We learned how we can prompt Mistral Models to do various tasks. In the next lesson, we'll take a look at how do you choose which Mistral models for which use case. See you in the next lesson.
