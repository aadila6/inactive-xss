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

SEARCH_API_KEY = 'AIzaSyBgzBrQZBnowp5XTlgeJ_a8OJ8Q4Fs8ixU'
SEARCH_ENGINE_ID = '22997d160aa4d4f63'
# SEARCH_QUERY = 'jquery.get >= 3.0.0'
#SEARCH_QUERY = 'https://tags.tiqcdn.com/utag/tealium-solutions/main/prod/utag.js OR utag.js'
SEARCH_QUERY = 'utag.js'
SEARCH_QUERY = '"https://tags.tiqcdn.com/utag/tealium-solutions/main/prod/utag.js" OR (utag.js AND (ecommerce OR retail OR news OR technology OR sports))'
SEARCH_QUERY = '"//tealium universal tag - utag.loader" AND "Copyright 2022"'
# SEARCH_QUERY = '"https://tags.tiqcdn.com/utag/tealium-solutions/main/prod/utag.js" OR (utag.js AND (ecommerce OR retail OR news OR technology OR sports OR finance OR health OR entertainment OR travel OR education OR automotive OR fashion OR food OR real_estate OR government OR non_profit OR marketing OR art OR gaming OR music OR environment)))'
SEARCH_URL = f'https://www.googleapis.com/customsearch/v1?key={SEARCH_API_KEY}&cx={SEARCH_ENGINE_ID}&q={SEARCH_QUERY}'

CONFIRM_URL = "http://localhost:8000/xss/check"

out = "crawler/output.txt"
out_websites = "crawler/utag_websites_04.txt"


def fetch_websites(start):
    SEARCH_URL = f'https://www.googleapis.com/customsearch/v1?key={SEARCH_API_KEY}&cx={SEARCH_ENGINE_ID}&q={SEARCH_QUERY}&start={start}'
    response = requests.get(SEARCH_URL)
    search_results = response.json()
    try:
        websites = [item['link'] for item in search_results['items']]
    except:
        websites = []
    return websites

all_websites = []
for i in range(1, 101, 10):
    print('Fetching... website-{}'.format(i))
    websites = fetch_websites(i)
    all_websites.extend(websites)

print(all_websites)

with open(out_websites, "w") as outfile:
    for website in all_websites:
        outfile.write(f"{website}\n")
    outfile.write("\n")


#
# # Open the output file for writing
# with open(out, "w") as outfile:
#     for website in websites:
#         code_snippets = []
#         rpctext = ""
#         try:
#             response = requests.get(website)
#             soup = BeautifulSoup(response.content, 'html.parser')
#             scripts = soup.find_all('script')
#             for script in scripts:
#                 src = script.get('src')
#                 if src:
#                     src = urljoin(website, src)
#                     code_snippets.append(requests.get(src).text)
#         except Exception as e:
#             print(f"Error checking website {website}: {e}")
#         if code_snippets:
#             outfile.write(f"Code snippets from {website}:\n")
#             for snippet in code_snippets:
#                 rpctext = rpctext + snippet
#                 outfile.write(f"{snippet}\n")
#             outfile.write("\n")
#             rpcData = {"url": website, "snippet": rpctext}
#             ret = requests.post(CONFIRM_URL, rpcData)
#             print(ret)
#
# with open(out_websites, "w") as outfile:
#     for website in websites:
#         outfile.write(f"{website}\n")
#     outfile.write("\n")
