# Import the necessary packages
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from langchain_ollama import ChatOllama

# Specify the model and project settings 
model_id = "llama3.2:1b"

# Wrap up the model into Olama inference
olama_llm = ChatOllama(
        model=model_id,
        temperature=0
    )

# Get the query from the user input
query = input("Please enter your query: ")

# Print the generated response
print(olama_llm.invoke(query))
