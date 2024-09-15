# Chatbot Interface with Gemini Pro API

This project is a simple web-based chatbot interface using the Gemini Pro API for natural language processing. The chatbot interface allows users to send messages and receive responses from the bot in real time. User messages are aligned to the left, and bot responses are aligned to the right.

## Features

- User-friendly web interface with a chat layout.
- Real-time communication with the bot using the Gemini Pro API.
- Dynamic message alignment (user messages on the left, bot messages on the right).
- Loading state indication for the bot's responses.

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript (Vanilla)
- **Backend**: Gemini Pro API (for NLP)
- **Communication**: Fetch API for asynchronous POST requests.

## Project Structure

```
├── static/
│   ├── style.css    # External CSS file for styling
├── templates/
│   └── index.html   # Main HTML structure for the chatbot
├── app.py           # Flask app to serve the chatbot interface
├── README.md        # Project documentation
└── requirements.txt # Python dependencies
```

## Setting Up the Environment

To set up a virtual environment for this project, follow these steps:

1. **Create a virtual environment:**

   ```bash
   python3 -m venv venv
   ```

2. **Activate the virtual environment:**
   * On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   * On Windows:
     ```bash
     .\venv\Scripts\activate
     ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask application:**

   ```bash
   python app.py
   ```

5. Open your browser and navigate to `http://localhost:5000` to access the chatbot interface.

## License

This project is licensed under the MIT License.
