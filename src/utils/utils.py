import numpy as np
from scipy.io import loadmat


def read_npy(npyfile):
    return np.load(npyfile)


def read_mat(matfile):
    return loadmat(matfile)


if __name__ == '__main__':
    print "npy"
    print read_npy('data.npy')
    print 'mat'
    print read_mat('data.mat')
