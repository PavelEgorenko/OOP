from matricesFunc import InData
from binary_matrix import bin_matrix
from diagonal_matrix import diagonal_matrix


class container:
    def __init__(self):
        self.matrices = []

    def InData(self, file):
        for line in file:
            nm = InData(line)
            if nm.isError:
                print("Ошибка в", len(self.matrices) + 1, "строке")
                exit()
            self.matrices.append(nm)

    def OutData(self, ofst):
        ofst.write("Container contains " + str(len(self.matrices)) + " elements.\n\n")
        for i in range(len(self.matrices)):
            self.matrices[i].Out(ofst)
            ofst.write("\n")

    def OutDataFirstType(self, ofst1):
        ofst1.write("Container contains " + str(len(self.matrices)) + " elements.\n")
        for i in range(len(self.matrices)):
            self.matrices[i].OutDataFiltr(ofst1)

    def Sort(self):
        for i in range(len(self.matrices)-1):
            for k in range(len(self.matrices)-1):
                if self.matrices[k].key > self.matrices[k+1].key:
                    self.matrices[k], self.matrices[k+1] = self.matrices[k+1], self.matrices[k]

    def Clear(self):
        self.matrices = []
