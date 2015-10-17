import time,sys,os,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
from utils.file import *
from numpy import float32,save,load
from sklearn.cluster.bicluster import SpectralBiclustering

def terms_by_cluster(term_clusters,terms):
    d = {}
    i = 0
    for cluster in term_clusters:
        if int(cluster) not in d:
            d[int(cluster)] = []
        d[int(cluster)].append(terms[i])
        i += 1
    return d

def cluster_term_frequency(clusters):
    d = {}
    for cluster,terms in clusters.items():
        d[cluster] = {}
        for term in terms:
            if term not in d[cluster]:
                d[cluster][term] = 0
            d[cluster][term] += 1
    return d

def scored_term_by_cluster(terms,terms_score):
    l = []
    for term in terms:
        l.append((term,terms_score[term]))
    return l

def cluster_terms_ordered_by_score(clusters,terms_score,k):
    d = {}
    for cluster,terms in clusters.items():
        term_cluster_score = scored_term_by_cluster(terms, terms_score)
        sorted_by_second = sorted(term_cluster_score, key=lambda tup: tup[1])
        sorted_by_second.reverse()
        d[cluster] = [x[0] for x in sorted_by_second[0:k]]
    return d


if __name__ == "__main__":
    if(len(sys.argv) == 6):
        tfidf_file = sys.argv[1]
        document_clusters_file = sys.argv[2]
        term_clusters_file = sys.argv[3]
        tfidf_mat_name = sys.argv[4]
        tfidf_terms_file = sys.argv[5]
        document_clusters = load(document_clusters_file)
        term_clusters = load(term_clusters_file)
        tfidf_terms = load(tfidf_terms_file)
        tfidf = load_sparse_mat(tfidf_mat_name,tfidf_file).astype(float32)
        tfidf_sum = tfidf.toarray().sum(axis=0)
        term_and_score = dict(zip(tfidf_terms,tfidf_sum))
        clusters = terms_by_cluster(term_clusters,tfidf_terms)
        clusters = cluster_terms_ordered_by_score(clusters, term_and_score,20)
        for cluster,terms in clusters.items():
            print(cluster,":",terms)



