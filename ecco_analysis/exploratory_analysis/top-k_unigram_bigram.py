__author__ = 'jrobledo'
import sys


def obtain_time_slices(start,end,portions):
    jump = int((end - start)/portions)
    first = list(range(start+1,end,jump))
    last = list(range(start+jump,end+jump,jump))
    return list(zip(first,last))


def obtain_filename(filename, period):
    start, end = period
    return filename+str(start)+'-'+str(end)+'.csv'


def read_file(filename, period, k):
    filename = obtain_filename(filename, period)
    f = open(filename)
    term_freq = {}
    i = 0
    for l in f:
        term, freq = l.strip().split(';')
        term_freq[term] = freq
        i += 1
        if k == i:
            break
    f.close()
    return term_freq


filename = sys.argv[1]
k = int(sys.argv[2])
s = int(sys.argv[3])
output = sys.argv[4]
periods = obtain_time_slices(1700,1800,s)
tf = {}
v = {}
file = open(output, 'w')
file.write('top-k;'+';'.join([str(start)+'-'+str(end) for start, end in periods])+'\n')
vocabulary = set()
for period in periods:
    tf[period] = read_file(filename, period, k)
    v[period] = set(tf[period].keys())
    vocabulary |= v[period]
for term in vocabulary:
    info = [term]
    for period in periods:
        if term in v[period]:
            info.append(tf[period][term])
        else:
            info.append(0)
    line = ';'.join(list(map(str, info)))+'\n'
    file.write(line)
file.close()