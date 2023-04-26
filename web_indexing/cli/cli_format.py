"""
Imports
"""
import re 
"""
Functions
    Cleans the output of other functions.
"""
"""
    re_clean_html
    Uses regex to remove all unwanted HTML syntax.
"""
def re_clean_html(html_input):
    return re.sub('<[^>]*>', '', html_input)
"""
    dict_format_multiple_url
    Takes output of other functions & formats response
    information into a dictonary.
    Uses key-value. This data isn't queried. This is for
    formatting.
"""
def dict_format_multiple_url(url_list):
    x = "<"+str(len(url_list))+"> (Duplicates hidden)"
    response_dict = {
        "resources found": x,
        "data": {}
    }
    for it in url_list:
        response_dict["data"][str(it[0])] = {
            'status': it[1],
            'message': it[2]
        }
    return response_dict









