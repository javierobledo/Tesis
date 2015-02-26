import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
nextdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(nextdir)
sys.path.insert(0,parentdir)

from utils.util3 import open_file,obtain_time_slices,split_dict_in_time_slices,write_csv
from utils.util import join_dict,term_frequency_collection,total_terms
from sklearn.feature_extraction.text import TfidfVectorizer
from numpy import float32

def vocabulary(corpus):
    v = set()
    for document in corpus:
        v |= set(document)
    return v

def document_frequency(term,corpus):
    return sum([1 for document in corpus if term in document])

def relative_document_frequency(corpus):
    df = {}
    X = vectorizer.fit_transform([' '.join(document) for document in corpus]).A
    v = vectorizer.get_feature_names()
    N = len(v)
    for i in range(N):
        df[v[i]] = float(sum(X[:,i])/N)
    list_of_tuples = df.items()
    list_of_tuples = sorted(list_of_tuples,key=lambda x: x[1])
    list_of_tuples.reverse()
    return list_of_tuples

if len(sys.argv) > 4:
    s = int(sys.argv[4])
    output = sys.argv[3]
    headers = open_file(sys.argv[1],';',True)
    books = open_file(sys.argv[2],';',True)
    books_and_headers = join_dict(headers,books)
    slices = obtain_time_slices(1700,1800,s)
    corpus_sliced = split_dict_in_time_slices(slices,books_and_headers)
    count = 0
    for corpus in corpus_sliced.values():
        vectorizer = TfidfVectorizer(binary=True,use_idf=False,smooth_idf=False,norm=None)
        df = relative_document_frequency(corpus)
        start,end = slices[count]
        write_csv(df,output+str(start)+'_'+str(end)+'.csv')
        count += 1