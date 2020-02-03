import numpy as np
class pca:
    def __init__(self, n_components):
        n=n_components
    def fit(self,value):
        M=np.mean(value.T,axis=1)
        C=value-M
        V=np.cov(C.T) 
        val,vec=np.linalg.eig(V)
        var_ratio= V/sum(V)
        self.variance_ratio=var_ratio
    def transform(self, data):
        M=np.mean(data.T,axis=1)
        C=data-M
        V=np.cov(C.T) 
        val,vec=np.linalg.eig(V)
        return np.dot(vec.T,C.T)
