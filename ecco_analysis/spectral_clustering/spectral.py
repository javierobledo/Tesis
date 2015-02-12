import time,sys,os,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
from utils.file import *
from numpy import float32,save
from sklearn.cluster.bicluster import SpectralBiclustering

if __name__ == "__main__":
    if(len(sys.argv) == 6):
        mat_name = sys.argv[1]
        mat_filename = sys.argv[2]
        k = int(sys.argv[3])
        l = int(sys.argv[4])
        output_mat_name = sys.argv[5]
        tfidf = load_sparse_mat(mat_name,mat_filename).astype(float32)
        start = time.time()
        model = SpectralBiclustering(n_clusters=(k,l),random_state=0)
        model.fit(tfidf)
        end = time.time()
        print(model.column_labels_)
        print(model.row_labels_)
        print("Biclustering process takes",int(round(end-start)),"seconds")
        save(output_mat_name,model.row_labels_.astype(float32))