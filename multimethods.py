from diagonal_matrix import diagonal_matrix
from binary_matrix import bin_matrix
from triangle_matrix import triangle_matrix
from multimethod import multimethod


@multimethod
def mmm(obj1: diagonal_matrix, obj2: bin_matrix, ofst):
    ofst.write("Diagonal and common matrix:\n")


@multimethod
def mmm(obj: bin_matrix, obj2: diagonal_matrix, ofst):
    ofst.write("Common and diagonal matrix:\n")


@multimethod
def mmm(obj: diagonal_matrix, obj2: diagonal_matrix, ofst):
    ofst.write("Diagonal and diagonal matrix:\n")


@multimethod
def mmm(obj: bin_matrix, obj2: bin_matrix, ofst):
    ofst.write("Common and common matrix:\n")


@multimethod
def mmm(obj: triangle_matrix, obj2: bin_matrix, ofst):
    ofst.write("Triangle and common matrix:\n")


@multimethod
def mmm(obj: bin_matrix, obj2: triangle_matrix, ofst):
    ofst.write("Common and triangle matrix:\n")


@multimethod
def mmm(obj: triangle_matrix, obj2: diagonal_matrix, ofst):
    ofst.write("triangle and diagonal matrix:\n")


@multimethod
def mmm(obj: diagonal_matrix, obj2: triangle_matrix, ofst):
    ofst.write("diagonal and triangle matrix:\n")


@multimethod
def mmm(obj: triangle_matrix, obj2: triangle_matrix, ofst):
    ofst.write("triangle and triangle matrix:\n")


if __name__ == "__main__":
    A = diagonal_matrix()
    B = bin_matrix()
    C = diagonal_matrix()
    ofst = open("output.txt", "w")
    mmm(C, A, ofst)
