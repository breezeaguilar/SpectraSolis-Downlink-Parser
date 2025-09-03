import requests
from bs4 import BeautifulSoup
# from ImageCompression import *

GREEN = '\033[32m'
RED = '\033[31m'
RESET = '\033[0m'

# open URL
# navigate to table
# open/download/parse absolute href in first column/last row

integration_reqURL = 'https://sg-webserver.phys.lsu.edu/payload-integration-data/?pname=pyld09'
reqURL = 'https://sg-webserver.phys.lsu.edu/payload-flight-data/?pname=pyld09'

response = requests.get(reqURL)

soup = BeautifulSoup(response.text, 'html.parser')
div = soup.find('div', class_ = 'elementor-widget-container')

thread_list = soup.find_all('td')
# print(thread_list)

#NOTE: 3 for the most recent log, 6 for testing
log_difference = 3
downlink_thread = str(thread_list[len(thread_list) - log_difference])

_, _, downlink_link = downlink_thread.partition("href=\"")
downlink_link, _, _ = downlink_link.partition("\">")

downlink_response = requests.get(downlink_link)
# print(downlink_response.content)

downlink_string = str(downlink_response.content)
# print(downlink_string)

downlink_data = downlink_string.split("SP")

logIdx = 0
for raw in downlink_data:
    # ensure bytes
    if isinstance(raw, str):
        raw = raw.encode("latin1")  # last resort, don't ask me what it is i just know if i take this out it doesnt work

    idx = raw.find(b"time:")  # locate payload
    if idx == -1:
        idx = raw.find(b"command")  # handle command messages
    if idx == -1:
        # couldn't find ASCII payload
        continue

    header = raw[:idx]
    payload = raw[idx:].decode("utf-8", errors="ignore").strip()
    
    print(f"{RED}Showing line {logIdx}{RESET}")
    print("Header: SP", header)
    print(f"Message: {GREEN}{payload}{RESET}")
    print()

    logIdx+=1