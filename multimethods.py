from diagonal_matrix import diagonal_matrix
from binary_matrix import bin_matrix
from multimethod import multimethod


@multimethod
def multimethod(obj1: diagonal_matrix(), obj2: bin_matrix(), ofst: str):
    print("1")
    # ofst.write("Diagonal and common matrix:\n")


@multimethod
def multimethod(obj1: diagonal_matrix(), obj2: diagonal_matrix(), ofst: int):
    print("1")
    # ofst.write("Diagonal and common matrix:\n")
