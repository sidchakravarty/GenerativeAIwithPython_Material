#%% packages
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv,find_dotenv
from langchain_core.output_parsers import JsonOutputParser # for structured output parsing
from pydantic import BaseModel, Field # for structured output parsing
load_dotenv(find_dotenv(usecwd=True))


#%% structured output
class TranslationResponse(BaseModel):
    source_text: str = Field(description="The original text that was translated.")
    target_text: str = Field(description="The translated text.")
    source_language: str = Field(description="The language of the original text.")
    target_language: str = Field(description="The language of the translated text.")
    tonality: int = Field(description="Tonality of the translation, on a scale from 1 (most negative) to 5 (most positive).")
#%% set up prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an AI assistant that translates a source language into "
    "other languages. No babbling! Make sure your output is a valid JSON object "
    "with the following fields: source_text, target_text, source_language, "
    "target_language, tonality [range of 1 to 5, with 1 being most negative "
    "and 5 being most positive]."),
    ("user", "Translate this sentence: '{input}' into {target_language}"),
])

# %% model
model = ChatOpenAI(model="gpt-4o-mini", 
                   temperature=0)

# %% chain
chain = prompt | model | JsonOutputParser(pydantic_object=TranslationResponse)

# %% invoke chain

output = chain.invoke({
    "input": "I am so happy to see you!",
    "target_language": "French"
})


# %% input: a sentence
# output: {'tonality': ['warm', 'aggressive', 'depressed']}
print(output)
# %%
