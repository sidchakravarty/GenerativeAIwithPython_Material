#%% packages
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(usecwd=True))
# TODO: add package import
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
# %%
api_key = api_key=os.getenv("GOOGLE_API_KEY")
# %%
# List all models
genai.configure(api_key=api_key)
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)

# %%
# Model overview: https://ai.google.dev/models/gemini
MODEL_NAME = 'gemini-2.5-flash'
# TODO: add the model

model = ChatGoogleGenerativeAI(model=MODEL_NAME,
                              temperature=0.7,
                              api_key=api_key)
# %% Run the model
res = model.invoke("What is a Generative AI?")
# %% find out what is in the result
res.model_dump()
# %% only print content
print(res.content)
# %%
