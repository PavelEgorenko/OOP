from matrices import matrices


def OutDataFiltr():
    return None


class diagonal_matrix(matrices):
    def __init__(self):
        super().__init__()
        self.type = "Diagonal"
        self.mtx = ""

    def In(self, line):
        mtx1 = line.split(" ")
        self.key = mtx1.pop(0)
        self.size = len(mtx1)

        for i in mtx1:
            mtx2 = ""
            for k in range(len(mtx1)):
                if i == mtx1[k]:
                    mtx2 += (i + " ")
                else:
                    mtx2 += "0 "
            self.mtx += mtx2 + "\n"
        self.mtx = self.mtx[:-2]
        if self.key == "2":
            self.mtx = self.mtx.replace("\n", "")
        self.sum_of_elements()

    def Out(self, ofst):
        ofst.write("Diagonal two-dimensional array:\n")
        ofst.write("Size = " + str(self.size) + "\n")
        ofst.write("Output Type = " + self.OutputType[int(self.key)] + "\n")
        ofst.write("Sum of elements = " + str(self.sumelems) + "\n")
        ofst.write(self.mtx + "\n")

    def OutDataFiltr(self, ofst1):
        ofst1.write("Diagonal two-dimensional array:\n")
        ofst1.write("Size = " + str(self.size) + "\n")
        ofst1.write(self.mtx + "\n\n")
