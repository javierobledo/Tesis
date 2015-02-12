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

if __name__ == "__main__":
    if(len(sys.argv) == 2):
        file_name = sys.argv[1]
        data = unicode_csv_reader(file_name)
        for row in data:
            print(row)