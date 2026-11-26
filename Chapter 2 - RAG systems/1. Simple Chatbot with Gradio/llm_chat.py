# Import necessary packages
import gradio as gr
from langchain_ollama import ChatOllama

# Specify the model and project settings 
model_id = "llama3.2:1b"

# Wrap up the model into Olama inference
olama_llm = ChatOllama(
        model=model_id,
        temperature=0.6
    )

# Function to generate a response from the model
def generate_response(prompt_txt):
    generated_response = olama_llm.invoke(prompt_txt)
    return generated_response.content

# Create Gradio interface
chat_application = gr.Interface(
    fn=generate_response,
	allow_flagging="never",
    inputs=gr.Textbox(label="Input", lines=2, placeholder="Type your question here..."),
    outputs=gr.Textbox(label="Output"),
    title="Olama Chatbot",
    description="Ask any question and the chatbot will try to answer."
)

# Launch the app
chat_application.launch(server_name="127.0.0.1", server_port= 7860)
