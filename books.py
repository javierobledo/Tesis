from file import *
import sys

if len(sys.argv) > 2:
    headers = open_file(sys.argv[1],';')
    books = open_file(sys.argv[2],';')
    books_and_headers = join_dict(headers,books)