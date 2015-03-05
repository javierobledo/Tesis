from sklearn.feature_extraction.text import TfidfVectorizer
from numpy import float32,array,multiply
import sys

def open_file(filename, separator, with_marks=False):
    d = {}
    f = open(filename)
    for line in f:
        if(with_marks):
            data = line.strip().split('"'+separator+'"')
            data = [x.replace('"','') for x in data]
            d[data[0]] = data[1:]
        else:
            data = line.strip().split(separator)
            data = [x for x in data]
            d[data[0]] = data[1:]
    f.close()
    return d

def join_dict(dic1,dic2):
    d = {}
    for key in dic1:
        d[key] = dic1[key] + dic2[key]
    return d

def obtain_time_slices(start,end,portions):
    jump = int((end - start)/portions)
    first = list(range(start+1,end,jump))
    last = list(range(start+jump,end+jump,jump))
    return list(zip(first,last))

def split_dict_in_time_slices(slices,books):
    count = 0
    d = {}
    for id,(year,title,text) in books.items():
        for i in range(len(slices)):
            t0,t1 = slices[i]
            if(t0 <= int(year) <= t1):
                if(i not in d):
                    d[i] = []
                d[i].append(text.split())
    return d

def join_text(corpus):
    return [' '.join(text) for text in corpus]

def tf(corpus,min_n,max_n):
    vectorizer = TfidfVectorizer(dtype=float32,ngram_range=(min_n,max_n),use_idf=False,smooth_idf=False,sublinear_tf=False,norm=None)
    X = vectorizer.fit_transform(corpus)
    y = vectorizer.get_feature_names()
    N = X.sum()
    X = multiply(X.sum(0).A1,1/N)
    term_freq = list(zip(y,X))
    term_freq_sorted = sorted(term_freq, key=lambda tup: tup[1])
    term_freq_sorted.reverse()
    return term_freq_sorted

def df(corpus,min_n,max_n):
    vectorizer = TfidfVectorizer(dtype=float32,ngram_range=(min_n,max_n),binary=True,use_idf=False,smooth_idf=False,norm=None)
    X = vectorizer.fit_transform(corpus)
    N,m = X.shape
    y = vectorizer.get_feature_names()
    X = X.sum(0).A1
    X = multiply(X,1/N)
    doc_freq = list(zip(y,X))
    doc_freq_sorted = sorted(doc_freq, key=lambda tup: tup[1])
    doc_freq_sorted.reverse()
    return doc_freq_sorted

def write(ngram,type,time_period,frequencies):
    start,end = time_period
    file = open(type+'_'+ngram+'_'+str(start)+'-'+str(end)+'.csv','w')
    for term,frequency in frequencies:
        file.write(term+';'+str(frequency).replace('.',',')+'\n')
    file.close()

if len(sys.argv) > 6:
    headers = open_file(sys.argv[1],';',True)
    books = open_file(sys.argv[2],';',True)
    s = int(sys.argv[3])
    min_n = int(sys.argv[4])
    max_n = int(sys.argv[5])
    type = sys.argv[6]
    books_and_headers = join_dict(headers,books)
    slices = obtain_time_slices(1700,1800,s)
    corpus_slices = split_dict_in_time_slices(slices,books_and_headers)
    data = []
    if(min_n == max_n):
        ngram = str(min_n)+'-gram_'
    else:
        ngram = str(min_n)+'-gram_'+str(max_n)+'-gram_'
    for id,corpus_slice in corpus_slices.items():
        corpus = join_text(corpus_slice)
        if(type == 'df'):
            frequency = df(corpus,min_n,max_n)
        elif(type == 'tf'):
            frequency = tf(corpus,min_n,max_n)
        write(ngram,type,slices[id],frequency)





