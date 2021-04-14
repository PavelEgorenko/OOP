from matrices import matrices


class bin_matrix(matrices):
    def __init__(self):
        super().__init__()
        self.type = "Binary"
        self.mtx = ""

    def In(self, line):
        mtx1 = line.split(" ")
        countlines = int(len(mtx1) ** 0.5)
        self.key = mtx1.pop(0)
        if self.key != "1" and self.key != "2":
            print("Неверно введен тип вывода данных в обычной матрице матрице", end=", ")
            self.isError = True
            return
        self.size = countlines
        for i in mtx1:
            if not i.isdigit():
                print("В матрице содержаться не только числа", end=", ")
                self.isError = True
                return
        if len(mtx1) ** 0.5 != self.size:
            print("Неверно введено количество элементов в матрице", end=", ")
            self.isError = True
            return

        for i in range(0, len(mtx1), countlines):
            mtx2 = ""
            for k in range(countlines):
                mtx2 += (mtx1[i + k]) + " "
            self.mtx += mtx2 + "\n"
        self.mtx = self.mtx[:-2]
        if self.key == "2":
            self.mtx = self.mtx.replace("\n", "")
        self.sum_of_elements()

    def Out(self, ofst):
        ofst.write("Common two-dimensional array:\n")
        ofst.write("Size = " + str(self.size)+"\n")
        ofst.write("Sum of elements = " + str(self.sumelems) + "\n")
        ofst.write("Output Type = " + self.OutputType[int(self.key)] + "\n")
        ofst.write(self.mtx+"\n")

    def OutDataFiltr(self, ofst1):
        return None
