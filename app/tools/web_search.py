from dotenv import load_dotenv
from langchain.tools import tool
load_dotenv()

from langchain_tavily import TavilySearch

# @tool
def web_search(query:str):
    """
    Search the web for recent information related to a given query.

    Args:
        query (str): The search query describing the topic or claim.

    """

    tool = TavilySearch(
        max_results=5,
        topic="general",
        search_depth="basic"
    )   

    url_links=[]

    result=tool.invoke(query)

    for i in result["results"]:
        url_links.append(i["url"])
    return url_links
