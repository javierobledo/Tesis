import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
nextdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(nextdir)
sys.path.insert(0,parentdir)

from utils.util import *

#separar en s partes
#por cada parte
#obtener los topk
#guardar en una estructura de datos
#guardar en archivo
#graficar
#
#leer el archivo de headers
#leer el archivo de books
#juntar la informacion
#obtener las s partes
#separar en s partes

if len(sys.argv) > 4:
    data = []
    k = int(sys.argv[3])
    s = int(sys.argv[4])
    headers = open_file(sys.argv[1],';',True)
    books = open_file(sys.argv[2],';',True)
    books_and_headers = join_dict(headers,books)
    slices = obtain_time_slices(1700,1800,s)0
    corpus_sliced = split_dict_in_time_slices(slices,books_and_headers)
    count = 0
    for corpus in corpus_sliced.values():
        tf = term_frequency_collection(corpus)
        start,end = slices[count]
        total = total_terms(tf)
        data.append(((start,end), [(x,y/float(total)) for x,y in top_k(tf,k)]))
        count += 1
    write_topk_csv(all_to_unicode(from_dict_topk_to_matrix(data)),'topk-k_'+str(k)+'-s_'+str(s)+'.csv')