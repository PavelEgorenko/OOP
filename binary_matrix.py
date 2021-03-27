from matrices import matrices


class bin_matrix(matrices):
    def __init__(self):
        super().__init__()
        self.mtx = ""

    def In(self, line):
        mtx1 = line.split(" ")
        self.key = mtx1.pop(0)
        countlines = int(len(mtx1) ** 0.5)
        self.size = countlines

        for i in range(0, len(mtx1), countlines):
            mtx2 = ""
            for k in range(countlines):
                mtx2 += (mtx1[i + k]) + " "
            self.mtx += mtx2 + "\n"
        self.mtx = self.mtx[:-2]

    def Out(self, ofst):
        ofst.write("Common two-dimensional array:\n")
        if self.key == "2":
            self.mtx = self.mtx.replace("\n", "")
        ofst.write("Size = " + str(self.size)+"\n")
        ofst.write("Output Type = " + self.OutputType[int(self.key)]+ "\n")
        ofst.write(self.mtx+"\n")