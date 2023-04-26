"""
Imports
"""
import requests
from urllib.parse import urljoin
"""
Functions
    Checks HTTP statuscodes dependant on :
        - File input,
        - CLI input,
        - List input
"""
"""
    get_http_code
    Simple function to get a HTTP code. Queried often.
"""
def get_http_code(link):
    link = requests.get(link)
    return link.status_code
"""
    check_http_code
    Formats HTTP code output from get request,
    Raises ValueError if anything <=4 is recieved.
"""
def check_http_code(status_code):
    first_char = str(status_code)[0]
    code_meaning = {
        "2": "success",
        "3": "redirect",
        "4": "client error",
        "5": "server error"
    }
    meaning = code_meaning.get(first_char)
    if meaning is not None:
        return [status_code, meaning]
    raise ValueError(f"Bad status code {status_code}")
"""
    multiple_input
    User input handler, takes input, gets HTTP code,
    formats HTTP code, stores all of this in a list &
    returns the list.
"""
def multiple_input(multi_user_input):
    results_list = []
    for it in multi_user_input:
        stored_result = get_http_code(it)
        http_cat = check_http_code(status_code=stored_result)
        items = [it] +http_cat
        results_list.append(items)
    return results_list
"""
    file_input
    Adds "robots.txt" to the end of input.
"""
def file_input(reachable_valid_list):
    urls = []
    for it in reachable_valid_list:
        urls.append(urljoin(it, "robots.txt"))
    return urls

