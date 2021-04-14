class matrices:
    OutputType = ["None", "line by line", "one dimensional array"]

    def __init__(self):
        self.type = ""
        self.key = 0
        self.size = 0
        self.mtx = ""
        self.sumelems = 0
        self.isError = False

    def sum_of_elements(self):
        lst = self.mtx.replace("\n", "").split(" ")
        for i in lst:
            self.sumelems += int(i)


