#!/bin/env python
# Python program to sort the words in lexicographical order 
import sys
import argparse

parser = argparse.ArgumentParser(description='Sorts a directory list from stdin in splunk>\'s global or app context', 
                                 epilog='Details: https://docs.splunk.com/Documentation/Splunk/latest/Admin/Wheretofindtheconfigurationfiles#How_app_directory_names_affect_precedence',
                                 formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('-context', dest='context', choices=['app', 'global'], required=True, 
                    help=('''\
app:    sort reverse-lexicographically
global: sort lexicographically'''
                    ))
args = parser.parse_args()

def sortLexo(input_list): 

    # Split the my_string till a space is found. 
    words = input_list.split()

    # sort depending on the context
    # do not get confused but the app context will NOT get reverse sorted while the global one will!
    # why? bc splunk> doc shows the priority(!) listing and NOT the processing(!) order.
    # the processing is exactly the other way around:
    if args.context == 'app':
        sort_reverse = False;
    else:
        sort_reverse = True;
    words.sort(reverse=sort_reverse)

    # Iterate i through 'words' to print the words 
    # in alphabetical manner. 
    for i in words: 
        print( i )  

# main func
if __name__ == '__main__': 
    input_list = sys.stdin.read()
    sortLexo(input_list)
