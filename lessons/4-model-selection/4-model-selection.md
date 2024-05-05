# Model Selection

In this lesson, you will learn how to select the appropriate Mistral models depending on your use case. Let's take a look.

Mistral AI provides five API endpoints featuring five leading language models:

| Model          | Endpoint                |
|----------------|-------------------------|
| Mistral 7B     | `open-mistral-7b`       |
| Mixtral 8x7B   | `open-mixtral-8x7b`     |
| Mistral Small  | `mistral-small-latest`  |
| Mistral Medium | `mistral-medium-latest` |
| Mistral Large  | `mistral-large-latest`  |

Looking at the model performance such as the MMLU: multitask language understanding task, Mistral Large performs the best. In fact, Mistral Large outperforms all the other models across various benchmarks including reasoning, multilingual tasks, mathematics and coding.

However, performance might not be the only consideration here. For your applications, you might also want to consider pricing. We offer competitive pricing on our models and it's worth considering the performance-pricing trade-offs. Mistral models are behind many large language model applications at scale.

Here's a brief overview on the types of use cases we see along with their respective Mistral model. Simple tasks that one can do in bulk, such as classification, customer support, or text generation, are powered by Mistral Small. Intermediate tasks that require moderate reasoning like data extraction, summarization, writing emails, and so on are powered by Mistral Medium. Complex tasks now require advanced reasoning capabilities or are highly specialized like synthetic text generation, code generation, RAG or agents are powered by Mistral Large. Let's take a look at some examples.

In this notebook, let's first use our helper function to load the API key. You can replace this with your own API key if you're running this outside of the class environment. 

Let's define a Mistral function to call the Mistral Python API easily. We have seen this code in the previous lesson.

For simple tasks like classification, we can use a smaller size model like Mistral Small. For example, let's classify an email as spam or not spam. Let's run our Mistral model. Mistral Small was able to classify the email correctly as spam. In fact, all of our models can get good results here. Using Mistral Small is more cost effective and it's faster. So, we recommend using Mistral Small to do simple tasks.

Mistral medium is great for intermediate tasks that require language transformation. For example, we can ask the model to compose an email for new customers who have just made their first purchase with your product. Make sure you have the order details in the prompt. Let's run Mistral Medium, and let's take a look at the response. And now we get a nice-looking email addressing to customer Anna with her order details.

Mistral large is great for complex tasks that require advanced reasoning capabilities or that are highly specialized. In this example, let's ask Mistral Large to calculate the difference in payment dates between the two customers whose payment amounts are close to each other in a given dataset. Let's try Mistral small first. Here you can see Mistral small gives the incorrect final answer. But since our model results are probabilistic, if you actually run this multiple times, it might sometimes give you the correct result. 

Okay, now let's run Mistral Large and print the model response. As you can see, Mistral Large can break down this question into multiple steps and is able to give us the right answer.

Let's try another fun example. Given the purchase details, how much did I spend on each category? Restaurants, groceries, stuffed animals, and props. And then we have the transaction details here. Let's first run, Mistral Small. You can see there are some mistakes here. For example, the world food wraps shoe bills at two restaurants. And now let's try Mistral Large. And it happens to categorize the world food wraps correctly as a restaurant and gives us the correct answer for each category.

In the next example, let's say you are about to meet a really important person named Andrew, and you're hoping to make a good impression on him. But you only have 20 minutes to chat. When you see him? He asks you? By the way, how do I find two numbers that add up to a third number? How can Mistral help you make a good impression? Let's take a look at this coding task. Mistral large is the top performer in coding tasks. So let's give it a try.

Great. So, now let's run this function. And let's see if the code passed these tests. Let's copy and paste here. Great. So it looks like our function works. And now Andrew would be very happy that you give the right answer.

Addition. Mistral large has been specifically trained to understand and generate text in multiple languages, especially in French, German, Spanish and Italian. Here is an example. Asking in French, which ones are heavier? A pound of iron or a kilogram of feathers? Let's roll, Mistral Large. I don't understand French, but I hope it answers correctly that a kilogram of feather is heavier.

Okay, so far we have seen many use cases with our models, but we have not talked about external tools. Connecting our models to external tools can help us build applications that are even more powerful. In the next lesson, you will learn how to use function calling to connect Mistral models to tools. See you in the next lesson.
