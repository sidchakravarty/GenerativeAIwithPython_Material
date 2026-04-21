#%% packages
from langchain_core.prompts import ChatPromptTemplate
#%% set up prompt template
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a funny assistant."),
        ("human", "What is the capital of {country} and what do the people {activity}?"),
    ]
)

prompt_template

#%% invoke prompt template
prompt = prompt_template.invoke(
    {
        "country": "France", 
        "activity": "do for fun"
    }
)
print(prompt)

# %%
