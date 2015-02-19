import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
nextdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(nextdir)
sys.path.insert(0,parentdir)

from utils.util import *

if len(sys.argv) > 4:
    k = int(sys.argv[3])
    s = int(sys.argv[4])
    headers = open_file(sys.argv[1],';',True)
    books = open_file(sys.argv[2],';',True)
    books_and_headers = join_dict(headers,books)
    slices = obtain_time_slices(1700,1800,s)
    corpus_sliced = split_dict_in_time_slices(slices,books_and_headers)
    count = 0
    top_k = {}
    for corpus in corpus_sliced.values():
        tf = term_frequency_collection(corpus)
        start,end = slices[count]
        #write_csv(tf,'tf'+str(start)+'_'+str(end)+'.csv')
        if(count == 0):
            for term,freq in tf[0:k]:
                top_k[term] = [freq]

        else:
            dtf = dict(tf)
            for term in top_k:
                if term not in dtf:
                    top_k[term] += [0]
                else:
                    top_k[term] += [dtf[term]]
    #print top_k
        count += 1
    write_csv_summary(top_k,'summary-k_'+str(k)+'-s_'+str(s)+'.csv')
