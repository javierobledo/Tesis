from numpy import diag,where,zeros,float32,inf,unique,min,max
from numpy.linalg import norm
from scipy.spatial.distance import euclidean

def symmetrize(a):
    return a + a.T - diag(a.diagonal())

def obtain_clusters_as_cluster_of_vectors(X,labels):
    print("Compute cluster vectors...")
    real_labels = unique(labels)
    n = len(real_labels)
    clusters = []
    for i in range(n):
        print(int(((i+1.0)/n)*100),"%")
        clusters.append(obtain_cluster_of_vectors(X,labels,real_labels[i]))
    return clusters,real_labels

def obtain_cluster_of_vectors(X,labels,label):
    return X[where(labels==label)]

def obtain_centroids_of_clusters(C):
    centroids = []
    n = len(C)
    print("Compute centroids...")
    for i in range(n):
        print(int(((i+1.0)/n)*100),"%")
        centroids.append(obtain_centroid_of_cluster(C[i]))
    return centroids

def obtain_centroid_of_cluster(C_i):
    n,m = C_i.shape
    center = zeros(m,dtype=float32)
    for j in range(m):
        y = C_i[:,j]
        center[j] = sum(y)/n
    return center

def select_norm_ord(metric):
    if(metric == 'euclidean'):
        o = None
    elif(metric == 'infinity'):
        o = inf
    elif(metric == 'frobenius'):
        o = 'fro'
    else:
        o = None
    return o

def obtain_scatter_degree_in_clusters(C,A,metric):
    scatters = []
    print("Compute scatter in clusters...")
    o = select_norm_ord(metric)
    n = len(C)
    for i in range(n):
        print(int(((i+1.0)/n)*100),"%")
        scatters.append(obtain_scatter_degree_in_cluster(C[i],A[i],o))
    return scatters

def obtain_scatter_degree_in_cluster(C_i,A_i,o):
    T_i = len(C_i)
    return (1.0/T_i)*sum([norm(C_i[j]-A_i,o) for j in range(T_i)])

def obtain_measure_of_separation_between_clusters(A,metric):
    o = select_norm_ord(metric)
    n = len(A)
    M = zeros((n,n),dtype=float32)
    print("Compute measure of separation between clusters...")
    for i in range(n):
        print(int(((i+1.0)/n)*100),"%")
        for j in range(i):
            M[i,j] = norm(A[i]-A[j],o)
            M[j,i] = M[i,j]
    return M

def obtain_measure_of_scheme_of_clusters(S,M):
    n = len(S)
    R = zeros((n,n),dtype=float32)
    print("Compute measure of scheme of clusters...")
    for i in range(n):
        print(int(((i+1.0)/n)*100),"%")
        for j in range(i):
            R[i,j] = (S[i]+S[j])/M[i,j]
    return R

def obtain_simmetry_conditions(R):
    n,m = R.shape
    D = zeros(n,dtype=float32)
    print("Compute simmetry conditions of clusters...")
    for i in range(n):
        print(int(((i+1.0)/n)*100),"%")
        D[i] = obtain_simmetry_condition(R,i,n)
    return D

def obtain_simmetry_condition(R,i,n):
    return max([R[i,j] for j in [x for x in range(n) if x != i]])

def distance_intercluster(C_i,C_j):
    n,_ = C_i.shape
    m,_ = C_j.shape
    d = zeros((n,m),dtype=float32)
    for i in range(n):
        for j in range(m):
            d[i,j] = euclidean(C_i[i],C_j[j])
    return min(d)

def distance_intracluster(C_i):
    n,m = C_i.shape
    d = zeros((n,n),dtype=float32)
    for i in range(n):
        for j in range(i):
            d[i,j] = euclidean(C_i[i],C_i[j])
    return max(d)

def obtain_distance_intraclusters(C):
    n = len(C)
    d = zeros(n,dtype=float32)
    print("Compute distance intraclusters...")
    for i in range(n):
        print(int(((i+1.0)/n)*100),"%")
        d[i] = distance_intracluster(C[i])
    return d

def obtain_distance_interclusters(C):
    n = len(C)
    d = zeros((n,n),dtype=float32)
    print("Compute distance interclusters...")
    for i in range(n):
        print(int(((i+1.0)/n)*100),"%")
        for j in range(i):
            d[i,j] = distance_intercluster(C[i],C[j])
            d[j,i] = d[i,j]
    return d



