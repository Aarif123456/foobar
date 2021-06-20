def transposeMatrix(matrix):
    return list(map(list,zip(*matrix)))

def getMatrixMinor(matrix,i,j):
    return [row[:j] + row[j+1:] for row in (matrix[:i]+matrix[i+1:])]

# Iterative implementation to get determinant
def getMatrixDeterminant(matrix):
    size = len(matrix)
    det=1
    total=1
    temp=[0 for i in range(size+1)]
    for i in range(size):
        index=i # initialize the index
        while matrix[index][i] == 0 and index<size: index+=1
        # if there is non zero element
        if index == size: continue
        if index != i:
            # loop for swapping the diagonal element row and index row
            for j in range(size):
                matrix[index][j], matrix[i][j] = matrix[i][j], matrix[index][j]
            # determinant sign changes when we shift rows
            # go through determinant properties
            det *= math.pow(-1, index - i)
        # storing the values of diagonal row elements
        for j in range(size):
            temp[j] = matrix[i][j]
        # traversing every row below the diagonal element
        for j in range(i+1, size):
            num1 = temp[i]
            diagonal = temp[i]
            nxt = matrix[j][i]
            # traversing every column of row and multiplying to every row
            for k in range(size):
                matrix[j][k] = (diagonal * matrix[j][k]) - (nxt * temp[k])
            total *= diagonal; # Det(kA)=kDet(A)

    for i in range(size):
        det *= matrix[i][i]
    return Fraction((int)(det), total)

def zeros_matrix(row,col):
    return [[0.0 for _ in range(col)]for _ in range(row)]

def multiply_matrices(A, B):
    """
    Returns the product of the matrix A * B
        :param A: The first matrix - ORDER MATTERS!
        :param B: The second matrix

        :return: The product of the two matrices
    """
    # Section 1: Ensure A & B dimensions are correct for multiplication
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])
    if colsA != rowsB:
        raise ArithmeticError(
            'Number of A columns must equal number of B rows.')

    # Section 2: Store matrix multiplication in a new matrix
    C = zeros_matrix(rowsA, colsB)
    for i in range(rowsA):
        for j in range(colsB):
            total = 0
            for ii in range(colsA):
                total += A[i][ii] * B[ii][j]
            C[i][j] = total

    return C

import unittest

class sTest(unittest.TestCase):
    
    def test_determinant(self):
        test_cases = \
            [
               ([[3,8],\
                 [4,6]],\
                 Fraction(-14,1)),\
               ([[4,6],
                [3,8]],\
                Fraction(14,1)),\
               ([[5,3,7],\
                [2,4,9],\
                [3,6,4],\
               ],Fraction(-133)),\
               ([[1,0,2,-1],\
                [3,0,0,5],\
                [2,1,4,-3],\
                [1,0,5,0],\
               ],Fraction(30))
            ]
        for arguments, expected in test_cases:
            with self.subTest(arguments=arguments, expected=expected):
                self.assertEqual(getMatrixDeterminant(arguments), expected)
    


