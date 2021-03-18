from diagonal_matrix import diagonal_matrix
from binary_matrix import bin_matrix
from matrices import matrices


def InData(line):
    nm = matrices()
    if line[0] == '1':
        line = line[2:]
        nm = diagonal_matrix()
    elif line[0] == '2':
        line = line[2:]
        nm = bin_matrix()
    nm.In(line)
    return nm
