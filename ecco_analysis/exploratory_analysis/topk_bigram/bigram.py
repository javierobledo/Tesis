from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from nltk import Text

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
nextdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(nextdir)
sys.path.insert(0,parentdir)

from utils.util import *

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
        line = []
        words = []
        for text in corpus_slice:
            words += text
        t = Text(text)
        bcf = BigramCollocationFinder.from_words(t.tokens)
        bcf.apply_freq_filter(minf)
        scored = bcf.score_ngrams(BigramAssocMeasures.likelihood_ratio)[0:k]
        start,end = slices[id]
        data.append(((start,end),[(x+' '+y,z) for (x,y),z in scored]))
    write_topk_csv(all_to_unicode(from_dict_topk_to_matrix(data)),'topkbigram-k_'+str(k)+'-s_'+str(s)+'-f_'+str(minf)+'.csv')
