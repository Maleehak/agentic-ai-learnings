from flask import Flask, request, jsonify, render_template
from olama_model import llama_response
#from olama_model import granite_response, mistral_response

import time

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    user_message = data.get('message')
    model = data.get('model')
    
    if not user_message or not model:
        return jsonify({"error": "Missing message or model selection"}), 400
    
    system_prompt = """
    You are an expert customer support assistant.

    Analyze the customer's message and return:

    1. summary: A concise summary of their concern.
    2. sentiment: An integer between 0 and 100.
    - 0 = Extremely negative
    - 50 = Neutral
    - 100 = Extremely positive
    3. response: A professional, empathetic and helpful
    response addressing their concern.

    Return actual values, not a JSON schema.
    Follow the required JSON format strictly.
    """
    
    start_time = time.time()
    
    try:
        if model == 'llama':
            result = llama_response(system_prompt, user_message)
            
        # elif model == 'granite':
        #     result = granite_response(system_prompt, user_message)
        # elif model == 'mistral':
        #     result = mistral_response(system_prompt, user_message)
        else:
            return jsonify({"error": "Invalid model selection"}), 400
        
        print("Result:", result)
        print("Result type:", type(result))

        result['duration'] = time.time() - start_time
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)