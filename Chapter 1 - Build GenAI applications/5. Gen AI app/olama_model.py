
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field


# Define JSON output structure
class AIResponse(BaseModel):
    summary: str = Field(description="Summary of the user's message")
    sentiment: int = Field(description="Sentiment score from 0 (negative) to 100 (positive)")
    response: str = Field(description="Suggested response to the user")


# JSON output parser
json_parser = JsonOutputParser(pydantic_object=AIResponse)


# Model IDs
LLAMA_MODEL_ID = "llama3.2:1b"
#GRANITE_MODEL_ID = "granite3.3:2b"
#MISTRAL_MODEL_ID = "mistral"


# Function to initialize a model
def initialize_model(model_id):
    return ChatOllama(
        model=model_id,
        temperature=0
    )


# Initialize models
llama_llm = initialize_model(LLAMA_MODEL_ID)
#granite_llm = initialize_model(GRANITE_MODEL_ID)
#mistral_llm = initialize_model(MISTRAL_MODEL_ID)


# Prompt templates
llama_template = PromptTemplate(
    template="""You are a friendly and helpful AI assistant. You task is to respond politely to the user

Instructions:
{system_prompt}

Analyze the following user message:
{user_prompt}

{format_prompt}

Important:
- Generate actual values for all fields.
- Do not return the JSON schema.
- Return only a valid JSON object.
""",
    input_variables=["system_prompt", "format_prompt", "user_prompt"]
)

# granite_template = PromptTemplate(
#     template="System: {system_prompt}\n{format_prompt}\nHuman: {user_prompt}\nAI:",
#     input_variables=["system_prompt", "format_prompt", "user_prompt"]
# )

# mistral_template = PromptTemplate(
#     template="<s>[INST]{system_prompt}\n{format_prompt}\n{user_prompt}[/INST]",
#     input_variables=["system_prompt", "format_prompt", "user_prompt"]
# )


def get_ai_response(model, template, system_prompt, user_prompt):

    chain = template | model | json_parser

    result = chain.invoke({
        'system_prompt': system_prompt,
        'user_prompt': user_prompt,
        'format_prompt': json_parser.get_format_instructions()
    })

    return result

# Model-specific response functions
def llama_response(system_prompt, user_prompt):
    return get_ai_response(llama_llm, llama_template, system_prompt, user_prompt)


# def granite_response(system_prompt, user_prompt):
#     return get_ai_response(granite_llm, granite_template, system_prompt, user_prompt)


# def mistral_response(system_prompt, user_prompt):
#     return get_ai_response(mistral_llm, mistral_template, system_prompt, user_prompt)
