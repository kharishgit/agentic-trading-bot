📈 Agentic Trading Bot






Agentic Trading Bot is an AI-powered stock market chatbot built with Streamlit and FastAPI, designed to provide real-time stock prices, financial data, and market insights. Users can upload stock market-related documents (PDFs or DOCX) to create a knowledge base and interact with the bot to get answers about stocks, indices (e.g., NIFTY 50), and more. The bot leverages multiple APIs for stock data and integrates retrieval-augmented generation (RAG) for enhanced query responses.

🚀 Live Demo: Try the app locally by following the setup instructions below!

🌐 GitHub Repository: kharishgit/agentic-trading-bot

✨ Features
Interactive Chat Interface: Ask questions like "stock price of Apple" or "Tell me about NIFTY 50" and get instant responses.
Real-Time Stock Prices: Fetches live stock prices using Alpha Vantage and Finnhub APIs.
Financial Data: Retrieves financial statements (e.g., revenue, net income) via Polygon API.
Document Upload: Upload stock market PDFs or DOCX files to build a knowledge base for RAG.
Index Support: Provides live values for market indices like NIFTY 50.
Error Handling: Robust error handling with custom exceptions (TradingBotException).
Persistent Chat History: Maintains conversation history using Streamlit’s session state.
🛠️ Tech Stack
Frontend: Streamlit (for the UI)
Backend: FastAPI (for API endpoints)
APIs:
Polygon API (financial data and delayed stock prices)
Alpha Vantage API (real-time stock prices)
Finnhub API (real-time stock prices)
Tavily API (web search for general queries)
RAG: Pinecone (vector database) for document retrieval
Libraries:
LangChain (for tools and API wrappers)
Requests (for HTTP requests)
Pinecone (for vector storage and retrieval)
📋 Prerequisites
Before setting up the project, ensure you have the following:

Python 3.8 or higher
Git installed
API keys for the following services:
Polygon API
Tavily API
Pinecone API
Google API (for embeddings or other Google services)
Grok API (optional, for additional AI capabilities)


🚀 Setup Instructions
1. Clone the Repository
Clone the project from GitHub:

bash

Copy
git clone https://github.com/kharishgit/agentic-trading-bot.git
cd agentic-trading-bot
2. Create a Virtual Environment
Set up a Python virtual environment to manage dependencies:

bash

Copy
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies
Install the required Python packages:

bash

Copy
pip install -r requirements.txt
If a requirements.txt file doesn’t exist, install the following packages manually:

bash

Copy
pip install streamlit fastapi uvicorn requests langchain langchain-community pinecone-client python-dotenv
4. Configure Environment Variables
Create a .env file in the project root and add your API keys:

plaintext

Copy
GOOGLE_API_KEY=
POLYGON_API_KEY=
TAVILY_API_KEY=
GROQ_API_KEY=
PINECONE_API_KEY=


5. Run the Backend (FastAPI)
Start the FastAPI backend server:



Copy
uvicorn app:app --host 0.0.0.0 --port 8000
This runs the backend API at http://localhost:8000. The app assumes app.py is your FastAPI backend file (adjust the filename if different).

6. Run the Frontend (Streamlit)
In a new terminal, activate the virtual environment and start the Streamlit app:


Copy
source venv/bin/activate  # On Windows: venv\Scripts\activate
streamlit run streamlit_ui.py
This opens the Streamlit app in your browser (typically at http://localhost:8501).

🖥️ Usage
Upload Documents:
In the sidebar, upload stock market-related PDFs or DOCX files.
Click "Upload and Ingest" to process the files and create a knowledge base for RAG.
Chat with the Bot:
In the chat section, type a query (e.g., "stock price of Apple" or "Tell me about NIFTY 50").
Click "Send" to get a response from the bot.
The bot will fetch live stock prices, financial data, or general information based on your query.
View Chat History:
The chat history is displayed above the input box, showing both user queries and bot responses.


📄 Example Queries
Stock Price: "stock price of Apple"
Response: Live stock price for AAPL (e.g., 210.211 USD as of May 15, 2025).
Financial Data: "financials of Tesla"
Response: Financial data for TSLA (or fallback data if unavailable).
Index Information: "Tell me about NIFTY 50"
Response: Live value of NIFTY 50 and general information.
General Query: "What is the stock market?"
Response: General information fetched via Tavily search.
🗂️ Project Structure
text

Copy
agentic-trading-bot/
│
├── streamlit_ui.py        # Streamlit frontend for the chatbot UI
├── tools.py               # Tools for fetching stock data, RAG, and web search
├── app.py                 # FastAPI backend (assumed, not provided)
├── .env                   # Environment variables (API keys)
├── exception/             # Custom exception handling
│   └── exceptions.py
├── data_models/           # Pydantic models (e.g., RagToolSchema)
│   └── models.py
├── utils/                 # Utility functions (e.g., model loading, config)
│   ├── model_loaders.py
│   └── config_loader.py
└── README.md              # Project documentation


🛠️ How It Works
Frontend (streamlit_ui.py)
Purpose: Provides an interactive UI with a sidebar for document uploads and a chat interface.
Functionality:
Uploads PDFs/DOCX files to the backend to create a knowledge base.
Sends user queries to the backend and displays the chat history.
Key Components:
File uploader for stock market documents.
Chat form with persistent history using st.session_state.
Backend (Assumed app.py)
Purpose: Handles API requests from the frontend, processes queries, and fetches data.
Endpoints:
/upload: Processes uploaded documents for RAG.
/query: Handles user queries, fetching stock prices, financial data, or general information.
Tools (tools.py)
Purpose: Defines tools for interacting with APIs and performing RAG.
Tools:
financials_tool: Fetches financial statements via Polygon API.
retriever_tool: Performs RAG using Pinecone for document-based queries.
tavilytool: Searches the web for general information.

⚠️ Limitations
Polygon API: Free tier provides delayed stock prices (previous day’s close) and may lack coverage for some stocks (e.g., Tesla, MRF).
Indices: Limited support for non-US indices like NIFTY 50; relies on Alpha Vantage/Finnhub for index data.
Document Upload: Assumes the backend correctly processes uploaded files for RAG.
🤝 Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch: git checkout -b feature/your-feature.
Make your changes and commit: git commit -m "Add your feature".
Push to your branch: git push origin feature/your-feature.
Open a pull request.
Please ensure your code follows the project’s style and includes tests where applicable.

📜 License
This project is licensed under the MIT License. See the  file for details.

📬 Contact
For questions or feedback, reach out to the project maintainer:

GitHub: kharishgit

🙏 Acknowledgments
Thanks to the creators of Streamlit, FastAPI, and LangChain for their amazing tools.
APIs: Polygon, Alpha Vantage, Finnhub, Tavily, Pinecone, and Google for enabling this project.
Inspired by the need for an AI-powered stock market assistant.
⭐ Star this repository if you find it useful! ⭐