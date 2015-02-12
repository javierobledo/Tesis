from util import *
from numpy import min,max

def dunn(X, labels):
    C,l = obtain_clusters_as_cluster_of_vectors(X,labels)
    n = len(C)
    Δ = obtain_distance_intraclusters(C)
    δ = obtain_distance_interclusters(C)
    mΔ = max(Δ)
    return min([min([δ[i,j]/mΔ for j in [x for x in range(n) if x != i]]) for i in range(n)])