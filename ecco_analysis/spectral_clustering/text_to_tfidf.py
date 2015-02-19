import os,sys,inspect
from sklearn.feature_extraction.text import TfidfVectorizer
from numpy import float32
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)


from utils.util3 import open_file
from utils.util import join_dict
from utils.file import *

if(len(sys.argv) == 5):
    headers = open_file(sys.argv[1],';',True)
    books = open_file(sys.argv[2],';',True)
    mat_name = sys.argv[3]
    mat_filename = sys.argv[4]
    books_and_headers = join_dict(headers,books)
    data = []
    for id,(year,title,text) in books_and_headers.items():
        data.append(text)
    vectorizer = TfidfVectorizer(min_df=1,dtype=float32)
    X = vectorizer.fit_transform(data)
    store_sparse_mat(X,mat_name,mat_filename)