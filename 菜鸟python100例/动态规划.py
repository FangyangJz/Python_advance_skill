import numpy as np

mat = np.array([
    [3,4,2,6],
    [8,5,6,2],
    [2,3,5,9]])

def rec_opt(mat, i,j):
    if i==0 and j==0:
        return mat[0, 0]
    elif (i==1 and j==0) or (i==0 and j==1):
        return max(mat[i,j], mat[j,i])
    else:
        A = rec_opt(mat, i-2, j-1) + mat[i,j]
        B = rec_opt(mat, i-1, i)
        return max(A, B)

if __name__=='__main__':
    print(mat[0,0])
    r = rec_opt(mat, 2, 2)
    print(r)