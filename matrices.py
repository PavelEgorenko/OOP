class matrices:
    def __init__(self):
        self.size = 0
        self.mtx = ""
        self.sumelems = 0

    def sum_of_elements(self):
        lst = self.mtx.replace("\n", "").split(" ")
        for i in lst:
            self.sumelems += int(i)


