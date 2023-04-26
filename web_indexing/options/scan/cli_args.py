"""
Imports
"""
from options.parsing.sucess_filter import *
from options.scan.argparse_args import *
from cli.cli_format import *
import argparse
import os
import json
"""
Functions
    Arguments given by the client that specifies :
        - File input
        - Scraping TRUE/FALSE
"""
"""
    file_arg
    Formatting / "main" function.
    Checks if the user input exists [absolute path],
    Checks availability, reachability, status codes.
    Inputs values returned from the afformentioned
    functions into a dictionary formatting function.
    Prints the output of the formatted dictionary.
"""
def file_arg(args):
    if os.path.exists(args):
                print(f"Processing URLs from file {args}...\n")
                global robots_append
                x = availability_filter(args)
                robots_append = file_input(x[2][2]) 
                check_file_https = multiple_input(robots_append)
                robots_filtered = http_sucess_filter(check_file_https)
                dict_sucess = dict_format_multiple_url(robots_filtered[0])
                dict_error = dict_format_multiple_url(x[2][1])
                print(json.dumps(dict_error, indent=3))
                print(json.dumps(dict_sucess, indent=3))
                return x
    else:
        print(f"File {args.file} could not be located. Did you provide the absolute path?\n")
"""
    scrape_arg
    Scrapes robots.txt from user input.
    Defines a dictonary for storage, loops through
    '*/robots.txt', scraping plaintext from the resource
    using a HTTP.GET.TEXT request, takes the output
    through a function which removes all the HTML syntax,
    stores in a dictionary with the given input URL.
    
"""
def scrape_arg(args):
    if args:
        print(f"Scraping URLS from output...\n")
        html_source = {}
        for url in robots_append:
            html_data = requests.get(url).text
            html_clean = re_clean_html(html_data)
            formatted_html = f"\n\n{html_clean.encode().decode('unicode_escape')}"
            html_source["DOMAIN - " +url] = formatted_html
        
        jsonstr = json.dumps(html_source, indent=3)
        jsonstr = jsonstr.replace('\\n','\n')
        print(jsonstr)
"""
    allowed_arg
    Takes input of robots_append, defines a list for
    temporary storage, runs a HTTP get text request on 
    all robots.txt resouces given, filters out 
    allowed and disallowed paths for legal
    purposes, checks for duplicates using set()
    stores the final result in robots_data.txt
    (OPTIONAL : Input() if user wants the output
    to be shown in terminal)
"""
def allowed_arg(args):
    html_data = []
    if args:
        for url in robots_append:
            try:
                html_get = requests.get(url).text
                html_data.append(html_get)
            except Exception as e:
                print(f"Error fetching {url}: {e}")
    allowed = []
    for html in html_data:
        for line in html.split("\n"):
            if line.startswith("Allow:"):
                allowed.append(line.split("Allow: ")[1])
    allowed = list(set(allowed))
    with open('robots_data.txt', 'w+') as f:
        for itr in allowed:
            f.write(itr + '\n')
    cli_out = input("Output to terminal? ")
    if cli_out:
        with open('robots_data.txt', 'r') as f:
            print(f"File contents :\n {f.read()}")
    else:
        print("Output stored in robots_data.txt")
