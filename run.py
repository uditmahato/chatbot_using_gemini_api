import re
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


def parse_response(text):
    # Initialize the output and states
    html_output = ""
    in_list = False
    list_level = 0

    # Split the text by lines
    lines = text.split('\n')

    for line in lines:
        # Handle bold headers
        if line.startswith("**") and line.endswith("**"):
            if in_list:
                html_output += "</ul>\n"
                in_list = False
            html_output += f"<h3>{line.strip('**').strip()}</h3>\n"
        
        # Handle bullet points
        elif line.startswith("*") and not (line.startswith("**") and line.endswith("**")):
            # Check if we're already in a list
            if not in_list:
                html_output += "<ul>\n"
                in_list = True
            # Check for nesting (if there are nested lists)
            if line.count('*') > list_level:
                html_output += "<ul>\n"
                list_level = line.count('*')
            elif line.count('*') < list_level:
                html_output += "</ul>\n"
                list_level = line.count('*')
            html_output += f"  <li>{line.strip('*').strip()}</li>\n"
        
        # Handle paragraphs and ensure lists are closed
        else:
            if in_list:
                html_output += "</ul>\n"
                in_list = False
            html_output += f"<p>{line.strip()}</p>\n"

    # Close any remaining open lists
    if in_list:
        html_output += "</ul>\n"

    return html_output

def chat_with_bot(prompt):
    # Create a chat session
    chat = model.start_chat(history=[])
    # Send the message and stream the response
    response = chat.send_message(prompt, stream=True)
    
    response_text = ""
    for chunk in response:
        if chunk.text:
            response_text += chunk.text + ' '

    # Parse the accumulated response into HTML
    parsed_html = parse_response(response_text)

    # Yield the parsed HTML content
    yield parsed_html


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
