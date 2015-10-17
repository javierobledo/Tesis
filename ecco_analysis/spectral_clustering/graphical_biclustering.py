import time,sys,os,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
from utils.file import *
from numpy import float32,save,amax,amin
from sklearn.cluster.bicluster import SpectralBiclustering
from matplotlib import pyplot as plt
import numpy as np

if __name__ == "__main__":
    if(len(sys.argv) == 6):
        mat_name = sys.argv[1]
        mat_filename = sys.argv[2]
        k = int(sys.argv[3])
        l = int(sys.argv[4])
        output_mat_name = sys.argv[5]
        tfidf = load_sparse_mat(mat_name,mat_filename).astype(float32)
        data = tfidf.A

        im = plt.matshow(data, aspect='auto', cmap='jet')
        vmax = amax(data)
        vmin = amin(data)
        plt.clim(vmin,vmax)
        plt.colorbar(im)
        m,n = tfidf.shape
        print("Matrix dimensions: ",m,"x",n)
        print("Row clusters:",k)
        print("Column clusters:",l)
        start = time.time()
        model = SpectralBiclustering(n_clusters=(k,l),random_state=0)
        model.fit(tfidf)
        end = time.time()
        print("Biclustering process takes",int(round(end-start)),"seconds")
        fit_data = data[np.argsort(model.row_labels_)]
        fit_data = fit_data[:, np.argsort(model.column_labels_)]
        im = plt.matshow(fit_data, aspect='auto', cmap='jet')
        plt.clim(vmin,vmax)
        plt.colorbar(im)
        im = plt.matshow(np.outer(np.sort(model.row_labels_) + 1,
                     np.sort(model.column_labels_) + 1),
            cmap='jet',aspect='auto')
        plt.clim(vmin,vmax)
        plt.colorbar(im)
        plt.title("Checkerboard structure of rearranged data")
        plt.show()
#        save(output_mat_name,model.row_labels_.astype(float32))
#        print("Output file in",output_mat_name+".npy")