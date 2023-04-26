"""
Imports
"""
from Projects.web_indexing.options.parsing.http_parsing import * 
import validators
"""
Functions
    Filters for :
        - Reachability,
        - Availabilty,
        - Valid URLs
"""
"""
    http_sucess_filter
    Creates a list with 3 sublists containing [potential]
    sublists. Queried by index from other functions to
    use either 'reachable resources', 'unreachable resources',
    or both.
    Uses comparison operators within a loop to determine these.
"""
def http_sucess_filter(multi_output):
    reachable_list = [x for x in multi_output if x[1] == 200 and x[2] == 'success']
    unreachable_list = [x for x in multi_output if x[1] != 200]
    reachable_urls = [sub_list[0] for sub_list in reachable_list]
    return reachable_list, unreachable_list, reachable_urls
"""
    validate_urls_from_file
    Uses validators module to check if the URL(s) supplied
    follow the standard FQDN.
    Reads the lines of the specified --file & assigns a list
    containing 3 sublists for valid, invalid, and both URLs.
    Queried via index placement.
"""
def validate_urls_from_file(file_path):
    with open(file_path, 'r') as f:
        urls = [line.strip() for line in f.readlines()]
    valid_urls = [url for url in urls if validators.url(url)]
    invalid_urls = [url for url in urls if not validators.url(url)]
    return valid_urls, invalid_urls, urls
"""
    availability_filter
    Ties all these functions together, so I only needed
    to call one function.
    Outputs available URLs, FQDN and reachable.
"""
def availability_filter(input):
    validity_check = validate_urls_from_file(input)
    status_check = multiple_input(validity_check[0])
    reachability_check = http_sucess_filter(status_check) 
    return validity_check, status_check, reachability_check




