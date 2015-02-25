import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
nextdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(nextdir)
sys.path.insert(0,parentdir)

from utils.util3 import open_file,obtain_time_slices,split_dict_in_time_slices,write_csv
from utils.util import join_dict,term_frequency_collection,total_terms

if len(sys.argv) > 4:
    s = int(sys.argv[4])
    output = sys.argv[3]
    headers = open_file(sys.argv[1],';',True)
    books = open_file(sys.argv[2],';',True)
    books_and_headers = join_dict(headers,books)
    slices = obtain_time_slices(1700,1800,s)
    corpus_sliced = split_dict_in_time_slices(slices,books_and_headers)
    count = 0
    top_k = {}
    for corpus in corpus_sliced.values():
        tf = term_frequency_collection(corpus)
        total = float(total_terms(tf))
        tf = [(x,y/total) for x,y in tf]
        start,end = slices[count]
        write_csv(tf,output+str(start)+'_'+str(end)+'.csv')
        count += 1
