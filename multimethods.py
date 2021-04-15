from diagonal_matrix import diagonal_matrix
from binary_matrix import bin_matrix
from multimethod import multimethod


@multimethod
def mmm(obj1: diagonal_matrix, obj2: bin_matrix,ofst):
    ofst.write("Diagonal and common matrix:\n")


@multimethod
def mmm(obj: bin_matrix, obj2: diagonal_matrix, ofst):
    ofst.write("Common and diagonal matrix:\n")


@multimethod
def mmm(obj: diagonal_matrix, obj2: diagonal_matrix, ofst):
    ofst.write("Diagonal and diagonal matrix:\n")


@multimethod
def mmm(obj: bin_matrix, obj2: bin_matrix, ofst):
    print("2")
    ofst.write("Common and common matrix:\n")

if __name__ == "__main__":
    A = diagonal_matrix()
    B = bin_matrix()
    C = diagonal_matrix()
    ofst = open("output.txt", "w")
    mmm(C, A, ofst)
