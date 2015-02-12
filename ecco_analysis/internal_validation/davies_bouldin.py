from numpy import array,float32
from numpy.linalg import norm
from util import *

def davies_bouldin(X, labels, metric='euclidean'):
    C,label_traductor = obtain_clusters_as_cluster_of_vectors(X,labels)
    n = len(C)
    A = obtain_centroids_of_clusters(C)
    S = obtain_scatter_degree_in_clusters(C,A,metric)
    M = obtain_measure_of_separation_between_clusters(A,metric)
    R = obtain_measure_of_scheme_of_clusters(S,M)
    D = obtain_simmetry_conditions(R)
    return (1.0/n)*sum(D)