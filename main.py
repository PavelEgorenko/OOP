from container import container

ifst = open("input.txt").read().split("\n")
ofst = open("output.txt", "w")

print("Start.")
c = container()
c.InData(ifst)
ofst.write("Filled container.\n")
c.OutData(ofst)
for i in range(len(c.matrices)):
    print(c.matrices[i])
c.Clear()
ofst.write("Empty container.\n")
c.OutData(ofst)
print("Stop")
ofst.close()