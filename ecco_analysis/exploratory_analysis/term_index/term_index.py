import numpy
from numpy import array,inner
import csv,sys

lmap = lambda func, *iterable: list(map(func, *iterable))

def read_csv(file_name,delimit):
    lines = []
    with open(file_name) as csvfile:
        reader = csv.reader(csvfile,delimiter=delimit)
        next(reader, None)
        for row in reader:
            lines.append(row)
    return lines

def rep(string):
    return string.replace(',','.')

#Dado una matriz con las frecuencias relativos o radios de verosimilitud se obtiene una matriz binaria
#d(w,i) en donde d vale 1 si la palabra w aparece en el periodo i y 0 si no
def period_array(LR):
    return array(LR > 0, dtype=int)

#Dado un archivo csv y su separador, devuelve un arreglo con los nombres de las palabras
#y una matriz con los valores leidos para cada periodo
def csv_to_array(file_name,delimit):
    csv = read_csv(file_name,delimit)
    header = []
    for row in csv:
        header.append(row[0])
    return array(header),array([array(lmap(float,map(rep,row[1:]))) for row in csv])

#Para una palabra w, se calcula su indice de uso, el cual viene dado por la suma de todos
#los radios de verosimilitud de cada periodo para dicha palabra
def use_index(w):
    return inner(LR[w],d[w])

def adoption_index(w):
    _,n = LR.shape
    sum = 0.0
    for i in range(n):
        for j in range(i+1,n):
            sum += (LR[w,i]-LR[w,j])*d[w,i]*d[w,j]
    return sum

def total(data):
    n,_ = data.shape
    return array([sum(data[i]) for i in range(n)])

if __name__ == "__main__":
    if(len(sys.argv[1:]) > 1):
        file_name = sys.argv[1]
        output = sys.argv[2]
        words,LR = csv_to_array(file_name,';')
        fr = total(LR)
        d = period_array(LR)
        n = words.size
        outfile = open(output,'w')
        outfile.write('term;total_frequency;use_index;adoption_index\n')
        for i in range(n):
            outfile.write(words[i]+';'+str(fr[i]).replace('.',',')+';'+str(use_index(i)).replace('.',',')+';'+str(adoption_index(i)).replace('.',',')+'\n')
        outfile.close()
