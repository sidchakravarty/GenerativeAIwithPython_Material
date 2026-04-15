# Generative AI with Python

## 3. LLM - Deep Dive

### 3.1 Model Training Process

![1776035231939.png](./1776035231939.png)

![1776035369175.png](./1776035369175.png)

Instead of just extending sentences by adding new words, LLMs are now trained on large corpuses of instruction dataset that teaches the model how to respond to different instructions.

![1776035383359.png](./1776035383359.png)

![1776035515821.png](./1776035515821.png)

### 3.2 Model Improvement Options

Now, we're going to take a look at different ways to improve the model output.And here this is already a foresighton different sections that we're going to cover at some later point.But first things first,if you use a model and you are not satisfied with the outputbecause you did not put enough effort into your user query in the first place.So that would be the simplest part called direct prompting.And we will see in this lecturehow you could improve the output.So the first thing would bethat you want to improve it bymodifying at the beginning of this chain.So the train is that you have the user query, it's passed to the LMand the LLM is providing some output.So one thing would bethat the problem is at the beginning of the train,if the beginning of the train is that you were quite sloppy in providing the queryand it was maybe not specific enough.There are many different waysto improve your query.All of this is running under the umbrella called Prompt Engineering.So you can put a lot of effort into tuning your prompt.Andthat would be all trying to change the chain at the beginning.But this might not change or might not solve the problemif the model doesn't have the answer. So, if in the model weights the answer is not included,then you cannot solve it with prompt engineering.And herethe technique called retrieval augmented generation is coming into play.This is working in the following wayand we will spend a lot of time on this.But here just quickly on a very high level,we are starting out again with the user query.Andthen the user query is passedin two different ways to the model.One way is the direct passing to the large language model.The other one is that you make a bypassand the user query is passed to some external sourcefrom the external source which could be a vector database or an internet search,you get back certain results which are very relevant for answering the question.Thenthe model is provided with this output as well.And with this contextual information,the model is now capable of answering the questionand providing a good output.So this isthe core idea of retriever augmented generation.And in the majority of cases, this is the way to go.But in specific cases, it might be thatfine tuning. The modelis a better approach.In that case, it would be two stagesthe first stage would be this horizontal path.So you would start out with your external data source.It is passed to the large language modeland some so called finetuned large language model is created.So you can see here now that thisinformation from the external sourceis now going to end up as**parametric weights of the model.**And now once the model has been trained,the query is running as usual.So the user is passing inthe question in its query,then this is passed to the finetuned large language modeland the model itself is then providing the output.So this would be the idea of finetuning some large language modeland the difficulty is from left to right. So the most simple one is of course direct prompting,putting not much effort into it,but you are not satisfied with the result. Thenprompt engineering is the nextmore difficult approachRsystems are still a bit more difficult. But again,with the difficulty, the performance is increasingand fine tuning is probably the most complicatedpart of it.And as I said, usually not necessary. So, we are going to work mostly with Rsystems in the scope.

![1776035778454.png](./1776035778454.png)

### 3.3 Model Providers

![1776036637966.png](./1776036637966.png)

### 3.4 Model Benchmarking

![1776036693109.png](./1776036693109.png)

LLM Leaderboard: [https://arena.ai/leaderboard](https://https://arena.ai/leaderboard)

![1776036879224.png](./1776036879224.png)

![1776036893209.png](./1776036893209.png)

### 3.5 Interaction with LLMs

#### 3.5.1 Python

![1776254636958.png](./1776254636958.png)

![1776254663109.png](./1776254663109.png)

#### 3.5.2 Groq

![1776255870273.png](./1776255870273.png)

![1776260183492.png](./1776260183492.png)

#### 3.5.3 OpenAI

[LangChain](https://docs.langchain.com/oss/python/langchain/overviewhttps://)

![1776260430717.png](./1776260430717.png)

![1776260488538.png](./1776260488538.png)

![1776260542065.png](./1776260542065.png)

![1776260557979.png](./1776260557979.png)

![1776260757283.png](./1776260757283.png)****

![1776260814914.png](./1776260814914.png)

[OpenAI Models](https://developers.openai.com/api/docs/modelshttps://)

![1776261601248.png](./1776261601248.png)

#### 3.5.4 Gemini



![1776264998797.png](./1776264998797.png)

### 3.6 Message Types

 ![1776265312028.png](./1776265312028.png)

 ![1776267895497.png](./1776267895497.png)

 ![1776268495732.png](./1776268495732.png)

[Adding a System Message to Groq](https://console.groq.com/playgroundhttps://)

 ![1776268821290.png](./1776268821290.png)

### 3.7 LLM Parameters

 ![1776269156247.png](./1776269156247.png)

 ![1776270468357.png](./1776270468357.png)

 ![1776270608661.png](./1776270608661.png)

 ![1776270848195.png](./1776270848195.png)

Using Groq playground to change the model parameters.

 ![1776271087697.png](./1776271087697.png)

 ![1776271145448.png](./1776271145448.png)

### 3.8 Model Selection

 ![1776273213888.png](./1776273213888.png)

### Model Capabilities

 ![1776273327240.png](./1776273327240.png)

 ![1776273498200.png](./1776273498200.png)

 ![1776273524991.png](./1776273524991.png)
