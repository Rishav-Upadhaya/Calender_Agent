import requests
from bs4 import BeautifulSoup
from langchain_core.tools import tool
from typing import List


API_URL = "https://merolagani.com/Ipo.aspx"

params = {
    "type" : "past"
}

@tool(description="Get share information from Merolagani")
def get_share_info() -> List: 
    """Fetch share information from Merolagani."""
    response = requests.get(API_URL, params=params)
    soup = BeautifulSoup(response.content, 'html.parser')
    query = []

    content_divs = soup.find_all('div', class_='announcement-list')
    for div in content_divs:
        for a_tag in div.find_all('a'):
            query.append(a_tag.text.strip())
            print(a_tag.text.strip())
    
    return query
    
    