def open_file(filename, separator):
    d = {}
    f = open(filename)
    for line in f:
        data = line.strip(separator).split()
        d[data[0]] = data[1:]
    f.close()
    return d

def join_dict(dic1,dic2):
    d = {}
    for key in dic1:
        d[key] = dic1[key] + dic2[key]
    return d
