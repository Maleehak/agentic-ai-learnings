import gradio as gr
from huggingface_hub import HfFolder

def add_numbers(Num1, Num2):
    return Num1 + Num2

def add_messages(msg1, msg2):
    return msg1 + " " + msg2

# Define the interface
demo = gr.Interface(
    fn=add_messages, 
    inputs=[gr.Text(), gr.Text()], # Create two numerical input fields where users can enter numbers
    outputs=gr.Text() # Create numerical output fields
)

# Launch the interface
demo.launch(server_name="127.0.0.1", server_port= 7860)
