import os, argparse

def tf(args):
    headersfile = args.headersfile
    booksfile = args.booksfile
    s = args.s
    os.system('python3 Tesis/ecco_analysis/exploratory_analysis/topk/term_frequency.py '+headersfile+' '+booksfile+' tf '+str(s))

def df(args):
    headersfile = args.headersfile
    booksfile = args.booksfile
    s = args.s
    print('python3 Tesis/ecco_analysis/exploratory_analysis/topk/document_frequency.py '+headersfile+' '+booksfile+' df '+str(s))
    #os.system('python3 Tesis/ecco_analysis/exploratory_analysis/topk/document_frequency.py '+headersfile+' '+booksfile+' df '+str(s))

def topk_unigram(args):
    headersfile = args.headersfile
    booksfile = args.booksfile
    s = args.s
    k = args.k
    os.system('python Tesis/ecco_analysis/exploratory_analysis/topk/topk.py '+headersfile+' '+booksfile+' '+str(s)+' '+str(k))

def topk_bigram(args):
    headersfile = args.headersfile
    booksfile = args.booksfile
    s = args.s
    k = args.k
    os.system('python Tesis/ecco_analysis/exploratory_analysis/topk_bigram/bigram.py '+headersfile+' '+booksfile+' '+str(k)+' '+str(s))

def tfidf(args):
    headersfile = args.headersfile
    booksfile = args.booksfile
    mname = args.mname
    mfilename = args.mfilename
    mindf = args.mindf
    min_n = args.min_n
    max_n = args.max_n
    os.system('python3 Tesis/ecco_analysis/spectral_clustering/text_to_tfidf.py '+headersfile+' '+booksfile+' '+mname+' '+mfilename+' '+str(mindf)+' '+str(min_n)+' '+str(max_n))

def clustering(args):
    mname = args.mname
    mfilename = args.mfilename
    k1 = args.k1
    k2 = args.k2
    output = args.output+'-k1_'+str(k1)+'-k2_'+str(k2)
    os.system('python3 Tesis/ecco_analysis/spectral_clustering/spectral.py '+mname+' '+mfilename+' '+str(k1)+' '+str(k2)+' '+output)

def indexes(args):
    mname = args.mname
    mfilename = args.mfilename
    modelfile = args.modelfile
    index = args.index
    os.system('python3 Tesis/ecco_analysis/internal_validation/apply_index.py '+mname+' '+mfilename+' '+modelfile+' '+index)

def adoption(args):
    os.system('')

def use(args):
    os.system('')

# create the top-level parser
parser = argparse.ArgumentParser(description='Process the ECCO-TCP Dataset, making an exploratory analysis (calculates tf, df, topk-unigrams and topk-bigrams) and a cluster analysis using the spectral biclustering algorithm. The clusters could be validated usign internal validation (Davies-Bouldin, Dunn or Silhouette indexes)')
subparsers = parser.add_subparsers(title='Types of Analysis',description='Select between Exploratory or Cluster Analysis',help='Options of analysis to be selected')
# create the parser for the "exploratory" command
exploratoryparser = subparsers.add_parser('exploratory',help='An exploratory analysis allows you to calculate term-frequency, document-frequency, top-k unigrams and top-k bigrams')
exploratorysubparsers = exploratoryparser.add_subparsers(title='Exploratory Analysis',description='Options for Exploratory Analysis')
# create the parser for the "exploratory tf" command
tfparser = exploratorysubparsers.add_parser('tf',help='Calculate the Relative Term-Frequency',epilog='The output are s CSV files (determined for the quantity of periods), each one with two columns: terms;frequency, where terms are the terms in de vocabulary of the period, and frequency is the relative term-frequency of the term')
tfparser.add_argument('headersfile',help='The entire filename of the headers of books')
tfparser.add_argument('booksfile',help='The entire filename of the books')
tfparser.add_argument('-s',nargs='?',metavar='s',default=10,help='The quantity of periods. For example, if the books are from 1700 to 1800, and s=10, de term-frequency will be calculated for each decade, i.e., 1701-1710, 1711-1720, etc. The default value is s=10')
tfparser.set_defaults(func=tf)
# create the parser for the "exploratory df" command
dfparser = exploratorysubparsers.add_parser('df',help='Calculate the Relative Document-Frequency',epilog='The output are s CSV files (determined for the quantity of periods), each one with two columns: terms;frequency, where terms are the terms in de vocabulary of the period, and frequency is the relative document-frequency of the term')
dfparser.add_argument('headersfile',help='The entire filename of the headers of books')
dfparser.add_argument('booksfile',help='The entire filename of the books')
dfparser.add_argument('-s',nargs='?',metavar='s',default=10,help='The quantity of periods. For example, if the books are from 1700 to 1800, and s=10, de term-frequency will be calculated for each decade, i.e., 1701-1710, 1711-1720, etc. The default value is s=10')
dfparser.set_defaults(func=df)
# create the parser for the "exploratory topk-unigram" command
topkparser = exploratorysubparsers.add_parser('topk-unigram',help='Obtain the top-k terms, based on the relative term-frequency',epilog='The output is a CSV file called topk-k_[k]-s_[s].csv, where [k] and [s] are determined by the arguments -k and -s. This file represents a (s x |v|) matrix, where v is the union of all the top-k terms in each period. Each element e_ij of the matrix represents the relative term-frequency of the term i in the period j')
topkparser.add_argument('headersfile',help='The entire filename of the headers of books')
topkparser.add_argument('booksfile',help='The entire filename of the books')
topkparser.add_argument('-s',nargs='?',metavar='s',default=10,help='The quantity of periods. For example, if the books are from 1700 to 1800, and s=10, de term-frequency will be calculated for each decade, i.e., 1701-1710, 1711-1720, etc. The default value is s=10')
topkparser.add_argument('-k',nargs='?',metavar='s',default=50,help='The k most frequent terms in each period, based on the relative term-frequency. The default value is k=50')
topkparser.set_defaults(func=topk_unigram)
# create the parser for the "exploratory topk-bigram command
topkbigramparser = exploratorysubparsers.add_parser('topk-bigram',help='Obtain the top-k bigrams, based on the log-likelihood ratio score (LLR)',epilog='The output is a CSV file called topkbigram-k_[k]-s_[s].csv, where [k] and [s] are determined by the arguments -k and -s. This file represents a (s x |v|) matrix, where v is the union of all the top-k bigrams in each period. Each element e_ij of the matrix represents the LLR of the bigram i in the period j')
topkbigramparser.add_argument('headersfile',help='The entire filename of the headers of books')
topkbigramparser.add_argument('booksfile',help='The entire filename of the books')
topkbigramparser.add_argument('-s',nargs='?',metavar='s',default=10,help='The quantity of periods. For example, if the books are from 1700 to 1800, and s=10, de term-frequency will be calculated for each decade, i.e., 1701-1710, 1711-1720, etc. The default value is s=10')
topkbigramparser.add_argument('-k',nargs='?',metavar='s',default=50,help='The k most frequent bigrams in each period, based on the LLR. The default value is k=50')
topkbigramparser.set_defaults(func=topk_bigram)
# create the parser for the "cluster" command
clusterparser = subparsers.add_parser('cluster',help='A Cluster Analysis classifies the documents in clusters, using the spectracl biclustering algorithm')
clustersubparsers = clusterparser.add_subparsers(title='Cluster Analysis',description='Options for Cluster Analysis')
# create the parser for the "cluster spectral" command
spectralparser = clustersubparsers.add_parser('spectral',help='Classifies the ECCO-TCP dataset using the Spectral Biclustering algorithm')
spectralsubparsers = spectralparser.add_subparsers(title='Preprocessing and Text Classification',description='First you need to obtain the tf-idf matrix from the dataset in order to use the spectral biclustering algorithm')
tfidfparser = spectralsubparsers.add_parser('tfidf',help='Calculate the TF-IDF matrix for the ECCO-TCP dataset',epilog='The output is a HDF5 table file containing a sparce matrix with dimensions |D| x |V|, where |D| is the number of documents in the ECCO-TCP corpus, and |V| the size of the vocabulary')
tfidfparser.add_argument('headersfile',help='The entire filename of the headers of books')
tfidfparser.add_argument('booksfile',help='The entire filename of the books')
tfidfparser.add_argument('-mname',nargs='?',metavar='matrix_name',default='tfidf',help='The name of the matrix to be stored. This value will be needed when you use the spectral biclustering algorithm. The default value is mname=tfidf')
tfidfparser.add_argument('-mfilename',nargs='?',metavar='matrix_filename',default='tfidf.h5',help='The filename of the file where the matrix will be stored. This value will be needed when you use the spectral biclustering algorithm. The default value is mfilename=tfidf.h5')
tfidfparser.add_argument('-mindf',nargs='?',metavar='min_df_value',default=1,help='When building the vocabulary ignore terms that have a term frequency strictly lower than the given threshold. The default value is mindf=1')
tfidfparser.add_argument('-min_n',nargs='?',metavar='n',default=1,help='This value determine the minimal n-gram that will be use. For example, if min_n=1, the unigrams will be included. The default value is min_n=1')
tfidfparser.add_argument('-max_n',nargs='?',metavar='n',default=1,help='This value determine the maximal n-gram that will be use. For example, if min_n=1 and max_n=1, only the unigrams will be included. If min_n=1 and min_n=2, unigrams and bigrams will be included. The default value is max_n=1')
tfidfparser.set_defaults(func=tfidf)
biclusterparser = spectralsubparsers.add_parser('biclustering',help='Use the spectral biclustering algorithm to classificate the information. The input is a TFIDF matrix (use tfidf on the dataset first)',epilog='The output is a vector in NumPy .npy format. This vector has |D| size, and each element C_i represent de cluster number of the document i')
biclusterparser.add_argument('-mname',nargs='?',metavar='matrix_name',default='tfidf',help='The name of the TFIDF matrix to be read. The default value is mname=tfidf')
biclusterparser.add_argument('-mfilename',nargs='?',metavar='matrix_filename',default='tfidf.h5',help='The filename of the file where the TFIDF matrix will be read. The default value is mfilename=tfidf.h5')
biclusterparser.add_argument('-output',nargs='?',metavar='filename',default='bicluster',help='The output filename where the clustering result will be stored. The default value is output=bicluster-k1_[k1]-k2_[k2].npy; where [k1] and [k2] are determined by the arguments -k1 and -k2')
biclusterparser.add_argument('-k1',nargs='?',metavar='k',default=2,help='The number of document clusters. The default value is k1=2')
biclusterparser.add_argument('-k2',nargs='?',metavar='k',default=2,help='The number of term clusters. The default value is k2=2')
biclusterparser.set_defaults(func=clustering)
# create the parser for the "cluster int_validation" command
internalparser = clustersubparsers.add_parser('validation',help='Validate the clusters quality usign internal validation methrics (Davies-bouldin,Dunn and Silhouette)',epilog='The output is a real number indicating the index value')
internalparser.add_argument('-mname',nargs='?',metavar='matrix_name',default='tfidf',help='The name of the TFIDF matrix to be read. The default value is mname=tfidf')
internalparser.add_argument('-mfilename',nargs='?',metavar='matrix_filename',default='tfidf.h5',help='The filename of the file where the TFIDF matrix will be read. The default value is mfilename=tfidf.h5')
internalparser.add_argument('-modelfile',nargs='?',metavar='filename',help='The filename of the file where the bicluster model will be read')
internalparser.add_argument('index',help='The index name. This could be: dunn (for dunn index), db (for davies-bouldin index) or sh (for silhouette index)')
internalparser.set_defaults(func=indexes)
args = parser.parse_args()
if hasattr(args, 'func'):
    args.func(args)