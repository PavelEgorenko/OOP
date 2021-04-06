from matrices import matrices


class triangle_matrix(matrices):
    def __init__(self):
        super().__init__()
        self.type = "Diagonal"
        self.mtx = ""

    def In(self, line):
        mtx1 = line.split(" ")
        self.key = mtx1.pop(0)
        itr = 0
        length = 0
        while length < len(mtx1):
            itr += 1
            length = 0
            for i in range(itr):
                length += i + 1
        self.size = itr

        for i in range(self.size):
            for k in range(self.size):
                if k <= i:
                    self.mtx += mtx1.pop(0) + " "
                else:
                    self.mtx += "0 "
            self.mtx += "\n"
        self.mtx = self.mtx[:-2]
        if self.key == "2":
            self.mtx = self.mtx.replace("\n", "")
        self.sum_of_elements()

    def Out(self, ofst):
        ofst.write("Triangle two-dimensional array:\n")
        ofst.write("Size = " + str(self.size) + "\n")
        ofst.write("Output Type = " + self.OutputType[int(self.key)] + "\n")
        ofst.write("Sum of elements = " + str(self.sumelems) + "\n")
        ofst.write(self.mtx + "\n")

    def OutDataFiltr(self, ofst1):
        return None
