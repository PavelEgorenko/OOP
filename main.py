from container import container

try:
    ifst = open("input.txt").read().split("\n")
except:
    exit()
ofst = open("output.txt", "w")
ofst1 = open("output1.txt", "w")

print("Start.")
c = container()
c.InData(ifst)
ofst.write("Filled container.\n")
c.Sort()
c.OutData(ofst)
c.OutDataFirstType(ofst1)
c.Clear()
ofst.write("Empty container.\n")
c.OutData(ofst)
print("Stop")
ofst.close()
ofst1.close()
