import numpy as np
class PCA:
    def __init__(self, n_components):
        self.n_components=n_components
        self.mean=None
        self.components=None
    def fit(self,value):
        self.mean=np.mean(value.T,axis=1)
        C=value-self.mean
        V=np.cov(C.T) 
        val,vec=np.linalg.eig(V)
        vec=vec.T
        index=np.argsort(val)[::-1]
        val=val[index]
        vec=vec[index]
        self.variance_ratio= V/sum(V)
        self.components=vec[0:self.n_components]
    def transform(self, data):
        data=data-self.mean
        return np.dot(data,self.componnents.T)
