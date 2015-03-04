from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from nltk import Text
from sklearn.feature_extraction.text import TfidfVectorizer
from numpy import float32

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
nextdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(nextdir)
sys.path.insert(0,parentdir)

from utils.util import *
from utils.util3 import open_file,obtain_time_slices,write_topk_csv,from_dict_topk_to_matrix,all_to_line

def preprocess(min_df_value,corpus):
    vectorizer = TfidfVectorizer(min_df=min_df_value,dtype=float32,ngram_range=(2,2))
    X = vectorizer.fit_transform(corpus)
    v = vectorizer.get_feature_names()
    return v

def join_text(corpus):
    return [' '.join(text) for text in corpus]


if len(sys.argv) > 5:
    data = []
    k = int(sys.argv[3])
    s = int(sys.argv[4])
    minf = int(sys.argv[5])
    headers = open_file(sys.argv[1],';',True)
    books = open_file(sys.argv[2],';',True)
    books_and_headers = join_dict(headers,books)
    slices = obtain_time_slices(1700,1800,s)
    corpus_slices = split_dict_in_time_slices(slices,books_and_headers)
    for id,corpus_slice in corpus_slices.items():
        corpus = join_text(corpus_slice)
        v = preprocess(minf,corpus)
        line = []
        words = []
        for text in corpus_slice:
            words += text
        t = Text(text)
        bcf = BigramCollocationFinder.from_words(t.tokens)
        bcf.apply_word_filter(lambda w: w not in v)
        scored = bcf.score_ngrams(BigramAssocMeasures.likelihood_ratio)[0:k]
        start,end = slices[id]
        data.append(((start,end),[(x+' '+y,z) for (x,y),z in scored]))
    write_topk_csv(all_to_line(from_dict_topk_to_matrix(data)),'topkbigram-k_'+str(k)+'-s_'+str(s)+'-f_'+str(minf)+'.csv')
