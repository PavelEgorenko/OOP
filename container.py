from matricesFunc import InData
from binary_matrix import bin_matrix
from diagonal_matrix import diagonal_matrix


class container:
    def __init__(self):
        self.matrices = []

    def InData(self, file):
        for line in file:
            nm = InData(line)
            self.matrices.append(nm)

    def OutData(self, ofst):
        ofst.write("Container contains " + str(len(self.matrices)) + " elements.\n")
        for i in range(len(self.matrices)):
            ofst.write(str(i + 1) + ": ")
            self.matrices[i].Out(ofst)

    def OutDataFirstType(self, ofst1):
        ofst1.write("Container contains " + str(len(self.matrices)) + " elements.\n")
        for i in range(len(self.matrices)):
            if self.matrices[i].type == "Binary":
                ofst1.write(str(i + 1) + ": ")
                self.matrices[i].Out(ofst1)

    def Clear(self):
        self.matrices = []
