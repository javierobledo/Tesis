import sys,os,inspect
from davies_bouldin import davies_bouldin
from  dunn import dunn
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
from utils.file import *
from numpy import load,float32
from sklearn.metrics import silhouette_score

if(__name__ == '__main__'):
    if(len(sys.argv) > 4):
        data_name = sys.argv[1]
        data_filename = sys.argv[2]
        model_filename = sys.argv[3]
        index = sys.argv[4]
        data = load_sparse_mat(data_name,data_filename).astype(float32)
        model = load(model_filename).astype(int)
        if(index == 'dunn'):
            du = dunn(data,model)
            print(du)
            du = dunn(data,model)
            print(du)
        elif(index == 'db'):
            dbi = davies_bouldin(data,model)
            print(dbi)
        elif(index == 'sh'):
            sh = silhouette_score(data,model)
            print(sh)
            sh = silhouette_score(data,model)
            print(sh)
        else:
            print("That internal index doesnt exist")
