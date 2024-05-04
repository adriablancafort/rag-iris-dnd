import requests
from bs4 import BeautifulSoup


def extract_content(url) -> str:
    # Send a GET request to the URL
    response = requests.get(url)
    print(0)
    # Check if the request was successful
    if response.status_code != 200:
        print(1)
        return "error" + f"bad status code: {response.status_code}"
    try:
        print(2)
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
    except KeyError:
        print(3)
        return "Error."


# Example usage:
#url = "https://2024/psc-pide-disculpas-despues-insultos-presidente-ugt-quien-se-haya-podido-sentir-ofendido_1209101_102.html"
#extracted_content = extract_content(url)
#print(extracted_content)
