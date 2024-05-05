import requests
from bs4 import BeautifulSoup


def extract_content(url) -> str:
    """
    Given a URL scrapes the web and returns the string of all text of the Web
    """
    # Send a GET request to the URL
    response = requests.get(url)
    # Check if the request was successful

    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the specific HTML elements containing the content you want
    paragraphs = soup.find_all("p")
    ans = ""
    # Extract and print the text from each <p> tag
    for p in paragraphs:
        text = p.get_text()
        ans += text + "\n"
    ans = ans.lstrip()
    ans = ans.rstrip()
    return ans
