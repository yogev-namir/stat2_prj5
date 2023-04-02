import numpy as np


def ex1(mat, vec):
    # check shape 0 and 1 are equal to x's shape 0
    if mat.shape[0] != vec.shape[0] or mat.shape[1] != vec.shape[0]:
        return
    n = mat.shape[0]
    B = mat.T - np.diag(np.diag(mat))
    X = vec.T
    for i in range(2, n + 1):
        X = np.concatenate((X, i * vec.T))
    ans = B + X
    return ans - np.diag(np.diag(ans))


def ex2(A, B, b, n):
    if not A.shape[0] == A.shape[1] == B.shape[0] == B.shape[1] == b.shape[0]:
        return
    m = b.shape[0]
    P = np.zeros((n * m, n * m))
    # first = np.block([[A,B.T]])
    # last = np.block([[B,A]])
    # C = np.block([[B,A,B.T]])
    # for i in range(0,n):
    #     if i==0:
    #         P
    for i in range(0, n * m, m):  # row block index
        for j in range(0, n * m, m):  # column block index
            if i == j:
                for row in range(m):
                    for col in range(m):
                        P[i + row][j + col] = A[row][col]
            if i == j + m:
                for row in range(m):
                    for col in range(m):
                        P[i + row][j + col] = B[row][col]
            if i == j - m:
                for row in range(m):
                    for col in range(m):
                        P[i + row][j + col] = B.T[row][col]

    arr = [i * b.T for i in range(1, n + 1)]
    y = (np.concatenate(arr)).T
    Q = np.kron(A, P)
    y_arr = [y.T for i in range(0, m)]
    z = np.concatenate(y_arr).T
    x = np.linalg.solve(Q, z)
    return x


def main():
    # A = np.array([[11, -7, 4], [4, 0, 8], [7, 8, 7]])
    # x = np.array([[10, 11, 13]])
    # C = ex1(A, x.T)
    # print(C)

    A2 = np.arange(1, 10)
    A2 = A2.reshape((3, 3))
    B = np.full((3, 3), 2) + A2
    b = np.arange(1, 4).T
    n = 4
    print(ex2(A2, B, b, n))


if __name__ == '__main__':
    main()
