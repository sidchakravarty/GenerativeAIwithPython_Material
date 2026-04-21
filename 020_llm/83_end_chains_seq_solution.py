
#%% packages
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from dotenv import load_dotenv, find_dotenv
import pprint
load_dotenv(find_dotenv(usecwd=True))

#%% set up prompt template

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a storyteller. You can write stories about characters in certain situations."),
    ("user", "Character: {character}; Situation: {situation}")
])

    
# %% Setup the model and chain
model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
# model = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)
chain = prompt | model # | StrOutputParser()
# %% Invoke the chain

input_variables = {"character": "Bert", "situation": "He finds out that he is a storm trooper and the " \
"order 66 has just been executed."}
res = chain.invoke(input_variables)

# %%
print(res)
 

#%% calculate the cost
cost_input_tokens = 0.15 # $/1M tokens
cost_output_tokens = 0.6 # $/1M tokens

# %%
usage_metadata = res.usage_metadata
used_input_tokens = usage_metadata['input_tokens']
used_output_tokens = usage_metadata['output_tokens']
# %%
cost = used_input_tokens * cost_input_tokens / 1e6 + used_output_tokens * cost_output_tokens / 1e6
cost # $
# %%

usage_metadata
# %%
