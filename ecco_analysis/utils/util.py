#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs

def open_file(filename, separator, with_marks=False):
    d = {}
    f = open(filename)
    for line in f:
        if(with_marks):
            data = line.strip().split('"'+separator+'"')
            data = [x.replace('"','').decode('utf-8') for x in data]
            d[data[0]] = data[1:]
        else:
            data = line.strip().split(separator)
            data = [x.decode('utf-8') for x in data]
            d[data[0]] = data[1:]
    f.close()
    return d

def join_dict(dic1,dic2):
    d = {}
    for key in dic1:
        d[key] = dic1[key] + dic2[key]
    return d

def obtain_time_slices(start,end,portions):
    jump = (end - start)/portions
    first = range(start+1,end,jump)
    last = range(start+jump,end+jump,jump)
    return zip(first,last)

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

def term_frequency_collection(collection):
    tf = {}
    for document in collection:
        for term in document:
            if term not in tf:
                tf[term] = 0
            tf[term] += 1
    list_of_tuples = tf.items()
    list_of_tuples = sorted(list_of_tuples,key=lambda x: x[1])
    list_of_tuples.reverse()
    return list_of_tuples

def top_k(terms,k):
    return terms[:k]

def total_terms(terms):
    s = 0
    for term,freq in terms:
        s += freq
    return s

def write_csv(data,filename):
    outfile = codecs.open(filename,'w',"utf-8")
    for term,freq in data:
        line = '"'+term+'";'+'"'+unicode(freq)+'"\n'
        outfile.write(line)
    outfile.close()

def write_csv_summary(data,filename):
    outfile = codecs.open(filename,'w',"utf-8")
    for term,freqs in data.items():
        line = '"'+term+'";'+';'.join(['"'+unicode(x)+'"' for x in freqs])+'\n'
        outfile.write(line)
    outfile.close()

def from_dict_topk_to_matrix(data):
    v = vocabulary(data)
    labels = [unicode(x)+'-'+unicode(y) for (x,y),z in data]
    matrix = []
    column_names = ['topk'] + labels
    matrix.append(column_names)
    for term in v:
        row = []
        row.append(term)
        for i in range(len(data)):
            (start,end),terms = data[i]
            topk = dict(terms)
            
            if(term in topk):
                row.append(topk[term])
            else:
                row.append(0)
        matrix.append(row)
    return matrix

def all_to_unicode(matrix):
    return ['"'+'";"'.join(map(unicode,row))+'"' for row in matrix]

def vocabulary(data):
    v = set()
    for date,terms in data:
        v |= set([x for x,y in terms])
    return v

def write_topk_csv(data,filename):
    outfile = codecs.open(filename,'w',"utf-8")
    for line in data:
        outfile.write(line.replace('.',',')+'\n')
    outfile.close()

