import requests
from bs4 import BeautifulSoup
import re 

# Define the URL of the website you want to scrape
def find_item(item_name):
    
    url = ('https://lordofthemysteries.fandom.com/wiki/'+item_name)

    # Send a GET request to the website and store the response in a variable
    response = requests.get(url)

    # Parse the HTML content of the response using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    start = soup.find("span", id="Appearance")
    end = soup.find("span", id="References")
    s = soup.find(start)
    e = soup.find(end)
    soup = str(soup)
    
    start = (str(start))
    end = (str(end))
    

    start_index = (soup.index(start))
    end_index = (soup.index(end))
    text = soup[start_index:end_index]


# Find all occurrences of <p> tags in the text and get their indexes
    open_p = [m.start() for m in re.finditer(r'<p>', text)]
    end_p = [m.start() for m in re.finditer(r'</p>', text)]
    

    for i in range(0, len(open_p)):
        info = text[open_p[i]:end_p[i]]
        info = re.sub(r'<[^>]*>', '', info)
        info = info.replace("\n", "")
        print(info)


find_item("Scarlet_Lunar_Corona")
