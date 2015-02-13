from util3 import *
from util import join_dict

def write_files(features,words,features_filename,words_filename):
    f = open(features_filename,'w')
    w = open(words_filename,'w')
    n = len(words)
    for i in range(n):
        f.write(features[i]+'\n')
        w.write(words[i]+'\n')
    f.close()
    w.close()




if(len(sys.argv) == 6):
    headers = open_file(sys.argv[1],';',True)
    books = open_file(sys.argv[2],';',True)
    books_and_headers = join_dict(headers,books)
    feature = sys.argv[3]
    features_filename = sys.argv[4]
    words_filename = sys.argv[5]
    id = list(books_and_headers.keys())
    year,title,words = list(zip(*list(books_and_headers.values())))
    if(feature == 'id'):
        write_files(id,words,features_filename,words_filename)
    elif(feature == 'year'):
        write_files(year,words,features_filename,words_filename)
    elif(feature == 'title'):
        write_files(title,words,features_filename,words_filename)