from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# ChatGPT API endpoint
API_ENDPOINT = "https://api.openai.com/v1/completions"
#https://api.openai.com/v1/completions
# Set your OpenAI API key here
API_KEY = "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"

@app.route('/chatbot', methods=['POST'])
def chatbot():
    # Get prompt from request
    prompt = request.json.get('prompt')

    # Send prompt to ChatGPT API
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    data = {
        "model": "text-davinci-003",
        "prompt": prompt,
        "max_tokens": 50  # Adjust as needed
    }
    response = requests.post(API_ENDPOINT, json=data, headers=headers)

    # Extract response from API
    if response.status_code == 200:
        return jsonify({"response": response.json().get('choices')[0].get('text')})
    else:
        return jsonify({"error": "Failed to get response from ChatGPT API"}), 500

if __name__ == '__main__':
    app.run(debug=True)
