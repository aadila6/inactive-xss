'''
Author: Adila
Date: 2023-04-10 18:32:20
LastEditors: liziwei01
LastEditTime: 2023-04-10 19:31:35
Description: file conten
'''
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

SEARCH_API_KEY = 'AIzaSyAvktGfYy08SsUFgektGY8vMHDeumwtGY4'
SEARCH_ENGINE_ID = 'a7574f723fa714c00'
SEARCH_QUERY = 'jquery.get >= 3.0.0'
SEARCH_URL = f'https://www.googleapis.com/customsearch/v1?key={SEARCH_API_KEY}&cx={SEARCH_ENGINE_ID}&q={SEARCH_QUERY}'

CONFIRM_URL = "http://localhost:8000/xss/check"

# Set the filename of the text file containing website URLs
out = "crawler/output.txt"
out_websites = "crawler/websites.txt"

response = requests.get(SEARCH_URL)
search_results = response.json()
print(search_results)  # Print the search results JSON object to see its contents

# websites = [item['link'] for item in search_results['items']]
websites = ['https://www.fallingbrick.co.uk/']
print(websites)
# Open the output file for writing
with open(out, "w") as outfile:
    for website in websites:
        code_snippets = []
        rpctext = ""
        try:
            response = requests.get(website)
            soup = BeautifulSoup(response.content, 'html.parser')
            scripts = soup.find_all('script')
            for script in scripts:
                src = script.get('src')
                if src:
                    src = urljoin(website, src)
                    code_snippets.append(requests.get(src).text)
        except Exception as e:
            print(f"Error checking website {website}: {e}")
        if code_snippets:
            outfile.write(f"Code snippets from {website}:\n")
            for snippet in code_snippets:
                rpctext = rpctext + snippet
                outfile.write(f"{snippet}\n")
            outfile.write("\n")
            rpcData = {"url": website, "snippet": rpctext}
            ret = requests.post(CONFIRM_URL, rpcData)
            print(ret)

with open(out_websites, "w") as outfile:
    for website in websites:
        outfile.write(f"{website}\n")
    outfile.write("\n")
