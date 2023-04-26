"""
Imports
"""
from options.parsing.sucess_filter import *
from options.scan.cli_args import *
import json
import argparse
import os
"""
Functions
    Centralizes CLI arguments.
"""
"""
    cli_options
    A function to centralize flags for the purpose
    of maintaining a clean '--help' message.
    Uses if statements to determine which argument has
    been specified.
"""
def cli_options():
    # args
    parser = argparse.ArgumentParser() 
    parser.add_argument('--file', required=False, help='processes a single file input containing a list of urls.')
    parser.add_argument('--allowed',action='store_true',required=False, help='outputs all the resources in robots.txt that web scrapers are authorized to scrape.')
    parser.add_argument('--scrape',action='store_true', required=False, help='visits resources found in robots.txt and extracts other resources find in the html source.')
    args = parser.parse_args()
    #args.file = input("FILE INPUT (DEBUG) : ")
    # args.scrape = input("SCRAPE OPT (DEBUG) : ")
    #args.allowed = input("ALLOWED (DEBUG) : ")
    if args.file:
        file_arg(args.file)
    if args.scrape:
        scrape_arg(args.scrape)
    if args.allowed:
        allowed_arg(args.allowed)
    return args

    