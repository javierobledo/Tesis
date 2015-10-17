import os,sys,inspect
from sklearn.feature_extraction.text import TfidfVectorizer
from numpy import float32,save
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)


from utils.util3 import open_file
from utils.util import join_dict
from utils.file import *

if(len(sys.argv) == 8):
    headers = open_file(sys.argv[1],';',True)
    books = open_file(sys.argv[2],';',True)
    mat_name = sys.argv[3]
    mat_filename = sys.argv[4]
    min_df_value = int(sys.argv[5])
    min_n = int(sys.argv[6])
    max_n = int(sys.argv[7])
    books_and_headers = join_dict(headers,books)
    data = []
    for id,(year,title,text) in books_and_headers.items():
        data.append(text)
    vectorizer = TfidfVectorizer(min_df=min_df_value,dtype=float32,ngram_range=(min_n,max_n))
    X = vectorizer.fit_transform(data)
    store_sparse_mat(X,mat_name,mat_filename)
    y = vectorizer.get_feature_names()
    save(mat_name+"_features",y)