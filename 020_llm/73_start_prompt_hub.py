#%% packages
import langchainhub as hub
from langsmith import Client
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv('.env')


#%% fetch prompt
client = Client()
prompt_template = client.pull_prompt("hardkothari/prompt-maker")
prompt_template

#%% get input variables
prompt_template.input_variables

# %% model
model = ChatOpenAI(model="gpt-4o-mini", 
                   temperature=0)

# %% chain
chain = prompt_template | model
# %% invoke chain
lazy_prompt = "A mysterious fog rolls into a quiet coastal town."
task = "Write a short story (around 500 words) exploring the impact of the fog on the town and its inhabitants. Consider what might be hidden within the fog."
improved_prompt = chain.invoke(
    {
        "lazy_prompt": lazy_prompt, 
        "task": task
    })
print(improved_prompt)

# %%
improved_prompt.content
# %% run model with improved prompt

# %% Original prompt
response_lazy = model.invoke(f"{lazy_prompt} {task}")
print(response_lazy.content)
# %% Improved prompt
response_improved = model.invoke(f"{improved_prompt} {task}")
print(response_improved.content)
# %%
