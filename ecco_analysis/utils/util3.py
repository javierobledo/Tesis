import csv, sys

def unicode_csv_reader(unicode_csv_data, dialect=csv.excel, **kwargs):
    # csv.py doesn't do Unicode; encode temporarily as UTF-8:
    csv_reader = csv.reader(utf_8_encoder(unicode_csv_data),
                            dialect=dialect, **kwargs)
    for row in csv_reader:
        # decode UTF-8 back to Unicode, cell by cell:
        yield [unicode(cell, 'utf-8') for cell in row]

def utf_8_encoder(unicode_csv_data):
    for line in unicode_csv_data:
        yield line.encode('utf-8')

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

def write_csv(data,filename):
    outfile = open(filename,'w')
    for term,freq in data:
        line = '"'+term+'";'+'"'+str(freq).replace('.',',')+'"\n'
        outfile.write(line)
    outfile.close()

def write_topk_csv(data,filename):
    outfile = open(filename,'w')
    for line in data:
        outfile.write(line.replace('.',',')+'\n')
    outfile.close()

def from_dict_topk_to_matrix(data):
    v = vocabulary(data)
    labels = [str(x)+'-'+str(y) for (x,y),z in data]
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

def vocabulary(data):
    v = set()
    for date,terms in data:
        v |= set([x for x,y in terms])
    return v

def all_to_line(matrix):
    return ['"'+'";"'.join(map(str,row))+'"' for row in matrix]

if __name__ == "__main__":
    if(len(sys.argv) == 2):
        file_name = sys.argv[1]
        data = unicode_csv_reader(file_name)
        for row in data:
            print(row)