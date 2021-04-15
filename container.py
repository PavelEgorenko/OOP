from matricesFunc import InData
from binary_matrix import bin_matrix
from diagonal_matrix import diagonal_matrix
from multimethods import *
from multimethod import multimethod


class container:
    def __init__(self):
        self.matrices = []

    def InData(self, file):
        for line in file:
            nm = InData(line)
            self.matrices.append(nm)

    def OutData(self:bin_matrix, ofst):
        ofst.write("Container contains " + str(len(self.matrices)) + " elements.\n")
        for i in range(len(self.matrices)):
            ofst.write(str(i + 1) + ": ")
            self.matrices[i].Out(ofst)

    def Sort(self):
        for i in range(len(self.matrices) - 1):
            for k in range(len(self.matrices) - 1):
                if self.matrices[k].size > self.matrices[k + 1].size:
                    self.matrices[k], self.matrices[k + 1] = self.matrices[k + 1], self.matrices[k]

    def Clear(self):
        self.matrices = []

    def Multimethod(self, ofst):
        ofst.write("Multimethod\n")
        for i in range(len(self.matrices)-1):
            for j in range(i, len(self.matrices)):
                mmm(self.matrices[i], self.matrices[j], ofst)
                self.matrices[i].Out(ofst)
                self.matrices[j].Out(ofst)
