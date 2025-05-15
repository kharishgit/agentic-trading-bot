import os
from langchain.tools import tool
from langchain_community.tools import TavilySearchResults
from langchain_community.tools.polygon.financials import PolygonFinancials
from dotenv import load_dotenv
from langchain_community.utilities.polygon import PolygonAPIWrapper
from langchain_community.tools.bing_search import BingSearchResults 
from data_models.models import RagToolSchema
from langchain_pinecone import PineconeVectorStore
from utils.model_loaders import ModelLoader
from utils.config_loader import load_config
from pinecone import Pinecone

# Load environment variables
env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path=env_path, override=True)

# Verify the POLYGON_API_KEY is loaded
polygon_api_key = os.getenv("POLYGON_API_KEY")
print("POLYGON_API_KEY from env:", polygon_api_key)
if not polygon_api_key:
    raise ValueError("POLYGON_API_KEY is not set in the environment.")

# Initialize wrappers and tools
api_wrapper = PolygonAPIWrapper(polygon_api_key=polygon_api_key)  # Pass the key explicitly
model_loader = ModelLoader()
config = load_config()

@tool(args_schema=RagToolSchema)
def retriever_tool(question):
    """this is retriever tool"""
    pinecone_api_key = os.getenv("PINECONE_API_KEY")
    pc = Pinecone(api_key=pinecone_api_key)
    vector_store = PineconeVectorStore(
        index=pc.Index(config["vector_db"]["index_name"]), 
        embedding=model_loader.load_embeddings()
    )
    retriever = vector_store.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={
            "k": config["retriever"]["top_k"], 
            "score_threshold": config["retriever"]["score_threshold"]
        },
    )
    retriever_result = retriever.invoke(question)
    return retriever_result

tavilytool = TavilySearchResults(
    max_results=config["tools"]["tavily"]["max_results"],
    search_depth="advanced",
    include_answer=True,
    include_raw_content=True,
)

financials_tool = PolygonFinancials(api_wrapper=api_wrapper)
# result = financials_tool.invoke({"query": "AAPL"})
# print("financials_tool result for AAPL:", result)

