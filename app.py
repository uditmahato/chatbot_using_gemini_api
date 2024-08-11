from flask import Flask, render_template, request, Response
import google.generativeai as genai

app = Flask(__name__)

# Fetch the API key from the environment variable
GOOGLE_API_KEY = 'AIzaSyBi3fQCz0JRVvgpH0BOSOZS702nml5zUbE'

if not GOOGLE_API_KEY:
    raise ValueError("No API key found. Please set the GOOGLE_API_KEY environment variable.")
# Initialize the API with the fetched key
genai.configure(api_key=GOOGLE_API_KEY)

# Load the model
model = genai.GenerativeModel('gemini-1.0-pro-latest')

def chat_with_bot(prompt):
    # Create a chat session
    chat = model.start_chat(history=[])
    # Send the message and stream the response
    response = chat.send_message(prompt, stream=True)
    # Yield chunks of text from the response
    for chunk in response:
        if chunk.text:
            words = chunk.text.split()
            for word in words:
                yield word + ' '
        else:
            yield ''
    yield ''  # Ensure the client knows the response is complete

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    prompt = data.get('prompt')
    return Response(chat_with_bot(prompt), content_type='text/plain')

if __name__ == "__main__":
    app.run(debug=True)
