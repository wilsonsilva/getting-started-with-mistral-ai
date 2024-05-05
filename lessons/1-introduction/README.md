# Introduction

Welcome to this short course Getting Started with Mistral built in partnership with Mistral AI.

Many popular and very effective LLMs are built on the standard transformer architecture, but one of the recent open source models released by Mistral, called Mixtral 8X7B, modifies the standard transformer architecture using a mixture of experts.

This means there are eight distinct feedforward neural networks called experts and at inference time, a different gating neural network first chooses to activate two of these eight experts to run to predict the next token. It then takes a weighted average of these to expert outputs in order to actually generate that next token.

This mixture of expert design allows the Mixtral Model to have both the performance improvements of a larger model, while having inference costs comparable to a smaller model. Specifically, even though the Mixtral model has 46.7 billion parameters at inference time, it only uses 12.9 of those parameters to predict each token.

I'm delighted that our instructor for this course is Sophia Yang, who is head of Developer Relations at Mistral AI.

Thank you Andrew. I am super excited to work with you and your team on this. In this course, you will get hands on experience with various open source and commercial Mistral models, including the open source Mixtral Model that Andrew just described via our API calls.

Yes, and you also learn about some unique and useful features of the Mistral models. For example, you learn to implement a function calling with Mistral's API. This enables you to instruct a model to call a user defined Python function, say, a function that carries out web search or receives texts from a database to help it gather the relevant information to answer a user's request.

Function calling and powers in LLM to more reliably and efficiently perform tasks that code does well, such as accessing information from a larger database or performing complex math.

Another feature of the Mistral model that I think is very useful is the JSON load. When you integrate in LLM into a larger software application, it's often very helpful for the LLM's output to be easily fed into downstream software systems by having it open as response in a structured JSON format.

For some LLMs users may rely on, say, clever prompting, or using a framework like Langchain a LlamaIndex to guarantee a reliable JSON format in the response. Mistral has a JSON mo feature that you can set to reliably generate responses that in the JSON format that you request. Sophia will also go through these examples using the Mistral API.

Yes, that's exactly right. And I'm also excited that you can easily try out both the open source Mistral Models, Mistral 7B and Mixtral 8X7B as well as the commercial models Mistral small, Mistral Medium, and Mistral Large through our API. To better decide when it makes sense for you to use each of the models depending on your use case.

Many people have worked to create this course. I like to thank from Mistral, Guillaume Lampe, Timothee Lacroix and Lelio Renaud Lavaud, from DeepLearning.AI Eddy Shyu had also contributed to this course. In the first lesson you'll get a more in-depth look at the Mixtral 8X7B mixture of experts architecture as well as an overview of the open source and commercial Mistral models. That sounds great.

Let's go on to the next video to get started.
