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
        if k == i and k != 0:
            break
    f.close()
    return term_freq


filename = sys.argv[1]
k = int(sys.argv[2])
s = int(sys.argv[3])
output = sys.argv[4]
d_output = sys.argv[5]
#Si o es full, entonces en vez de rellenar con 0s, utiliza el valor de frecuencia
o = sys.argv[6]
periods = obtain_time_slices(1700,1800,s)
tf = {}
tf_t = {}
v = {}
v_t = {}
file = open(output, 'w')
dout = open(d_output, 'w')
file.write('top-k;'+';'.join([str(start)+'-'+str(end) for start, end in periods])+'\n')
dout.write('top-k;'+';'.join([str(start)+'-'+str(end) for start, end in periods])+'\n')
vocabulary = set()
for period in periods:
    tf[period] = read_file(filename, period, k)
    if(o == 'full'):
        tf_t[period] = read_file(filename,period,0)
    v[period] = set(tf[period].keys())
    if(o == 'full'):
        v_t[period] =set(tf_t[period].keys())
    vocabulary |= v[period]
for term in vocabulary:
    info = [term]
    d_info = [term]
    for period in periods:
        if term in v[period]:
            info.append(tf[period][term])
            d_info.append(1)
        else:
            d_info.append(0)
            if o =='full':
                if term in v_t[period]:
                    info.append(tf_t[period][term])
                else:
                    info.append(0)
            else:
                    info.append(0)
    line = ';'.join(list(map(str, info)))+'\n'
    d_line = ';'.join(list(map(str, d_info)))+'\n'
    dout.write(d_line)
    file.write(line)
file.close()
dout.close()