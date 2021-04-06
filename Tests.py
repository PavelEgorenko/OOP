from unittest import TestCase
from binary_matrix import bin_matrix
from diagonal_matrix import diagonal_matrix
from triangle_matrix import triangle_matrix
from matricesFunc import InData
from matrices import matrices
from container import container


class Test_bin_matrix(TestCase):
    def test_in(self):
        nm = bin_matrix()
        nm.In("1 1 2 3 4 5 6 7 8 9")
        nm1 = bin_matrix()
        nm1.In("2 1 2 3 4 5 6 7 8 9")
        self.assertEqual(nm.mtx, "1 2 3 \n4 5 6 \n7 8 9")
        self.assertEqual(nm.key, "1")
        self.assertEqual(nm1.mtx, "1 2 3 4 5 6 7 8 9")
        self.assertEqual(nm1.key, "2")

    def test_out(self):
        nm = bin_matrix()
        nm.size = 1
        nm.mtx = "3"
        nm.sumelems = 3
        nm.key = 1
        ofsttest = open("testbitout.txt").read()
        ofst = open("tests.txt", "w")
        ofst = nm.Out(ofst)
        ofst1 = open("tests.txt").read()
        self.assertEqual(ofst1, ofsttest)


class Test_diag_matrix(TestCase):
    def test_in(self):
        nm = diagonal_matrix()
        nm.In("1 1 2 3")
        nm1 = diagonal_matrix()
        nm1.In("2 3 2 1")
        self.assertEqual(nm.mtx, "1 0 0 \n0 2 0 \n0 0 3")
        self.assertEqual(nm.key, "1")
        self.assertEqual(nm1.mtx, "3 0 0 0 2 0 0 0 1")
        self.assertEqual(nm1.key, "2")

    def test_out(self):
        nm = diagonal_matrix()
        nm.size = 1
        nm.mtx = "3"
        nm.sumelems = 3
        nm.key = 1
        ofsttest = open("testdiagout.txt").read()
        ofst = open("tests.txt", "w")
        ofst = nm.Out(ofst)
        ofst1 = open("tests.txt").read()
        self.assertEqual(ofst1, ofsttest)


class Test_triang_matrix(TestCase):
    def test_in(self):
        nm = triangle_matrix()
        nm.In("1 1 2 3 4 5 6")
        nm1 = triangle_matrix()
        nm1.In("2 3 2 1")
        self.assertEqual(nm.mtx, "1 0 0 \n2 3 0 \n4 5 6")
        self.assertEqual(nm.key, "1")
        self.assertEqual(nm1.mtx, "3 0 2 1")
        self.assertEqual(nm1.key, "2")

    def test_out(self):
        nm = triangle_matrix()
        nm.size = 1
        nm.mtx = "3"
        nm.sumelems = 3
        nm.key = 1
        ofsttest = open("testtriangout.txt").read()
        ofst = open("tests.txt", "w")
        ofst = nm.Out(ofst)
        ofst1 = open("tests.txt").read()
        self.assertEqual(ofst1, ofsttest)


class Test_matrices_func(TestCase):
    def test_In(self):
        nm = InData("1 1 1")
        ntest = diagonal_matrix()
        nm1 = InData("2 3 3 3")
        ntest1 = bin_matrix()
        self.assertEqual(type(nm), type(ntest))
        self.assertEqual(type(nm1), type(ntest1))


class Test_matrices(TestCase):
    def test_summ_of_elements(self):
        nm = bin_matrix()
        nm.mtx = "1 1 1 2 2 2 3 3 3"
        nm.sum_of_elements()
        nm1 = diagonal_matrix()
        nm1.mtx = "1 0 0 \n0 2000 0 \n0 0 1010"
        nm1.sum_of_elements()
        self.assertEqual(nm.sumelems, 18)
        self.assertEqual(nm1.sumelems, 3011)


class Test_container(TestCase):
    def test_In(self):
        c = container()
        file = ["1 1 3 4 5 6", "2 1 1 2 3 4"]
        c.InData(file)
        self.assertEqual(len(c.matrices), 2)

    def test_Out(self):
        c = container()
        ofsttest = open("testcontout.txt").read()
        ofst = open("tests.txt", "w")
        ofst = c.OutData(ofst)
        ofst1 = open("tests.txt").read()
        self.assertEqual(ofst1, ofsttest)

    def test_Out_filtr(self):
        c = container()
        bin = bin_matrix()
        bin.mtx = "1"
        c.matrices.append(bin)
        diag = diagonal_matrix()
        diag.mtx = "226"
        c.matrices.append(diag)
        ofsttest = open("testcontoutFiltr.txt").read()
        ofst = open("tests.txt", "w")
        ofst = c.OutDataFirstType(ofst)
        ofst1 = open("tests.txt").read()
        self.assertEqual(ofst1, ofsttest)

    def test_Sort(self):
        c = container()
        ctest = container()
        nm1 = bin_matrix()
        nm1.key = 1
        nm2 = triangle_matrix()
        nm2.key = 2
        nm3 = triangle_matrix()
        nm3.key = 1
        nm4 = bin_matrix()
        nm4.key = 1
        c.matrices.append(nm1)
        c.matrices.append(nm2)
        c.matrices.append(nm3)
        c.matrices.append(nm4)
        c.Sort()
        ctest.matrices.append(nm1)
        ctest.matrices.append(nm3)
        ctest.matrices.append(nm4)
        ctest.matrices.append(nm2)
        self.assertEqual(c.matrices, ctest.matrices)

    def test_Clear(self):
        c = container()
        for i in range(12):
            c.matrices.append(i)
        c.Clear()
        self.assertEqual(c.matrices, [])
