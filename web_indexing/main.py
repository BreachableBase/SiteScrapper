# imports
from options.parsing.sucess_filter import *
from options.scan.argparse_args import cli_options
# main
"""
1 : validate url syntax by using validate_urls, returns (valid_urls, invalid_urls)
2 : check reachability of valid_urls using get_http_code
3 : IF user specifies file input flags :
        call file_input with the given valid_urls output, take the output from file_input and 
        call multiple_input
    IF user inputs a singular URL on the cli
        pass valid_urls into multiple_input
4 : IF user specifies that they only want the successful located resources, 
        pass the output of multiple_input through success_filter and print
    else :
        print the output of multiple_input
"""

def main():
    cli_options()

if __name__ == "__main__":
     main()






















