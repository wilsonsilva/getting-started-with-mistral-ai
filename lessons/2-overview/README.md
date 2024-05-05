# Overview

In this lesson, you'll get an overview of the various Mistral Models and Mistral, we aspire to build the best foundation models.

Currently, we offer six models for all use cases and business needs. Let's dive in.

We offered two open source models that you can download the model and use it anywhere without restrictions. Mistral 7B is our first model that was released last September.

It outperforms Llama models with the similar and even greater sizes. You can see in the chart the orange part represents Mistral 7B and the other colored bars represent various Llama models. On the horizontal axis, these labels, like Knowledge Reasoning code, are advocates of standard evaluation benchmarks.

We measure performance on a variety of tasks. For example, the reason reasoning benchmark includes swag, art, easy r challenge and other tasks. The coding benchmark includes human A and MVP. 

Mistral 7B fits on one GPU. Perfect for you to get started experimenting with. Mixtral 8X7B is a sparse mixture of expert model we released last December. At a high level, imagine you have eight experts to help you process your text.

Instead of saying all experts, we choose the top experts to help you. For more details, the foundation of our model is a transformer block, which composed of two layers, a feedforward layer and a multi had attention layer. Each input token goes through the same layers.

How can we add capacity to the model? We duplicate the feed for layer and times. But now how do we decide which input token goes to which feed for layers? We use a router to map each token to the top K feed forward layers and ignore the rest. As a result, even though Mistral has 46.7 billion total parameters but only uses 12.9 billion parameters per token providing great performance with fast inference. 

It outperforms LLaMa 2 70B and most benchmarks with eight times faster inference and it matches or outperforms GPT 3.5 a most standard benchmarks.

And we're excited to be contributing to some of the amazing models that are available to the AI community. and they're under the open source Apache 2.0 license, which means you can download the model weights of both models, fine tuned, and customize them for your own use cases and use them without any restrictions.

For example, you can create your own AI applications for commercial use. We are committed to open models will release more open models in the future.

We also offer four optimized enterprise-grade models. Mistral small is the best for lower latency use cases. Mistral Medium is suitable for your language based tasks now may only require moderate reasoning such as data extraction, summarization and email writing.

Mistral Large is our flagship model for your most sophisticated needs with advanced reasoning capabilities. Mistral Large approaches the performance of GPT-4 and outperforms

It has native multilingual capabilities, it strongly out performs LLaMa 2 70B on common sense and reasoning benchmarks in French, German, Spanish and Italian. 

It offers a 32k tokens context window. In fact, all of our served models have 32K context window live. It excels in instruction following and is natively capable of function calling.

You can use function calling with both Mistral small and Mistral Large. By the way, if you are not familiar with function calling, we'll go through how they do function, calling in this course. 

And finally we have an embedding model which offers the state of the art embeddings for text and can be used for many use cases like clustering and classification.

Many customers leverage a model for a wide variety of applications across industries such as banking, telecom, media, logistic fintech, among others.

They have deployed our models for tasks like RAG, content generation, content synthesis, code generation, insights generation and more.

Throughout this course you will learn how you can use Mistral Models And use cases similar to these. To get started using our models right away. You can use Le Chat, our chat interface to interact directly with our models.

Let's go to chat on Mistral.AI. We can ask in the chat to write a Python function to sort the given string. 
Now we get a nice looking Python function. Please note, that Le Chat is currently free to use. So you just need to sign up and you can use it.

If you are interested in running our open source models locally, you can use transformers, Llama.cpp or ollama. Note that a lot of people use a quantized version of our model in order to load our model into the memory.

Keep in mind that the model quantization may harm model performance. So, don't be surprised if the quantized model doesn't perform as well as expected.

Even though it is fun to download Mistral models on your own machine, please keep in mind that for faster inference, more reliable performance and to skills we do recommend using a host of service such as La Plateforme where you can access not only the open source models but also the enterprise models with a simple API call.

To access our model through La Plateforme, you can create your own API keys. To set up your API keys, go to console.mistral.ai . Create your own account, set up your billing information, and click on API keys to create new API keys.

We offer pricing which is cheaper than some of the other hosting platforms. This course will focus on using our API endpoints
We'll dive into any use cases using our API in the rest of the class.

For the rest of the class you don't actually need to create account, we'll provide administrator API key for you to using the class. In the next lesson, you will learn how to use Mistral API and learn some of the prompting techniques.

Let's get started with the next lesson.
