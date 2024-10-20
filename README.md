# RAG-Powered Chatbot

This project is a simple chatbot application built using Langchain, OpenAI's GPT-4o-mini model, and Streamlit. The chatbot is designed to provide a conversational interface where users can interact with an AI assistant.

## Features

- **User Interface**: Built with Streamlit, providing a clean and interactive UI.
- **Customizable Appearance**: Users can select colors for user and assistant messages.
- **Session Management**: Maintains conversation history across interactions.
- **Environment Configuration**: Uses a `.env` file to manage environment variables.

## Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd rag-powered-chatbot
   ```

2. **Install dependencies**:
   Make sure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Variables**:
   Create a `.env` file in the root directory and add your environment variables as needed.

4. **Run the application**:
   Start the Streamlit app by running:
   ```bash
   streamlit run chatbot/app.py
   ```

## Usage

- **Settings**: Adjust preferences such as user name and message colors in the sidebar.
- **Interaction**: Type your message in the input box and click "Send" to interact with the chatbot.
- **Clear History**: Use the "Clear Conversation" button in the sidebar to reset the conversation.

## Dependencies

- `langchain_openai`
- `langchain_core`
- `streamlit`
- `python-dotenv`

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
