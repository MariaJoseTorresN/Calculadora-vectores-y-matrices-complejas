import unittest
import calculadoraMatricesComplejas as cMc

class TestCalculadoraMatricesComplejas(unittest.TestCase):

    def test_adicionVect(self):
        a=[(6,-4),(7,3),(4.2,-8.1),(0,-3)]
        b=[(16,2.3),(0,-7),(6,0),(0,-4)]
        self.assertEqual(cMc.adiVect(a,b),[(22,-1.70),(7,-4),(10.2,-8.1),(0,-7)])

    def test_inverVect(self):
        a=[(6,-4),(7,3),(4.2,-8.1),(0,-3)]
        self.assertEqual(cMc.inverVect(a),[(-6,4),(-7,-3),(-4.2,8.1),(0,3)])

    def test_escalarMultiVect(self):
        escalar = (3,2)
        a=[(6,3),(0,0),(5,1),(4,0)]
        self.assertEqual(cMc.escalarMultVect(escalar,a),[(12,21),(0,0),(13,13),(12,8)])

    def test_adiMatrix(self):
        a = [[(1, -1), (3, 0)], [(2, 2), (4, 1)]]
        b = [[(5, 6), (20, -2)], [(10, -4.2), (27, -12)]]
        c = [[(5, 6), (20, -2),(1,1)], [(10, -4.2), (27, -12),(-1,-1)]]
        self.assertEqual(cMc.adiMatrix(a,b), [[(6,5),(23,-2)],[(12,-2.2),(31,-11)]])
        self.assertEqual(cMc.adiMatrix(a,c), "Indefinido")

    def test_inverMatrix(self):
        a = [[(1, -1), (3, 0)], [(2, 2), (4, 1)]]
        self.assertEqual(cMc.inverMatrix(a),[[(-1, 1), (-3, 0)], [(-2, -2), (-4, -1)]])

    def test_escalarMultMatrix(self):
        escalar = (3,2)
        a = [[(1, -1), (3, 0)], [(2, 2), (4, 1)]]
        self.assertEqual(cMc.escalarMultMatrix(escalar,a),[[(5, -1), (9, 6)], [(2, 10), (10, 11)]])
        
    def test_transMatrix(self):
        a = [[(6, -3), (2, 12), (0,-19)], [(0, 0), (5, 2.1), (17, 0)], [(1, 0), (2, 5), (3, -4.5)]]
        self.assertEqual(cMc.transMatrix(a),[[(6, -3), (0, 0), (1, 0)], [(2, 12), (5, 2.1), (2, 5)], [(0,-19), (17, 0), (3, -4.5)]])

    def test_conjuMatrix(self):
        a = [[(6, -3), (2, 12), (0,-19)], [(0, 0), (5, 2.1), (17, 0)], [(1, 0), (2, 5), (3, -4.5)]]
        self.assertEqual(cMc.conjuMatrix(a), [[(6, 3), (2, -12), (0,19)], [(0, 0), (5, -2.1), (17, 0)], [(1, 0), (2, -5), (3, 4.5)]])

    def test_adjMatrix(self):
        a = [[(6, -3), (2, 12), (0,-19)], [(0, 0), (5, 2.1), (17, 0)], [(1, 0), (2, 5), (3, -4.5)]]
        self.assertEqual(cMc.adjMatrix(a),[[(6, 3), (0, 0), (1, 0)], [(2, -12), (5, -2.1), (2, -5)], [(0, 19), (17, 0), (3, 4.5)]])

    def test_productMatrix(self):
        a = [[(3, 2), (0, 0), (5, -6)], [(1, 0), (4, 2),(0, 1)], [(4, -1), (0,0), (4, 1)]]
        b = [[(5, 0), (2, -1), (6, -4)], [(0, 0), (4, 5),(2,0)], [(-7, -4), (2, 7), (0, 0)]]
        c = [[(1, -1), (3, 0)], [(2, 2), (4, 1)]]
        self.assertEqual(cMc.productMatrix(a,b), [[(-44, 32), (60, 24), (26, 0)], [(9, -7), (1, 29), (14, 0)], [(-4, -28), (8, 24), (20, -22)]])
        self.assertEqual(cMc.productMatrix(a,c), "Indefinido")
    
    def test_accionMatrixVector(self):
        a = [[(6, -3), (2, 12), (0,-19)], [(0, 0), (5, 2.1), (17, 0)], [(1, 0), (2, 5), (3, -4.5)]]
        v = [(16,2.3),(0,-7),(6,0)]
        b = [(16,2.3),(0,-7)]
        self.assertEqual(cMc.accionMatrixVector(a,v),[(186.9, -162.2), (116.7, -35.0), (69.0, -38.7)])
        self.assertEqual(cMc.accionMatrixVector(a,b), "Indefinido")

    def test_prodIntVec(self):
        a = [[(1, 0)], [(0, 1)], [(1, -3)]]
        b = [[(2, 1)], [(0, 1)], [(2, 0)]]
        self.assertEqual(cMc.prodIntVec(a,b), (5, 7))

    def test_normaVec(self):
        a = [[(3.1, 5.7)], [(4.9, -3.7)]]
        self.assertEqual(cMc.normaVec(a), 79.8 ** (1 / 2))

    def test_distVec(self):
        a = [(3.1, -5.7), (4.9, -3.7)]
        b = [(4.2, 6.8), (7.5, 18)]
        self.assertEqual(cMc.distVect(a,b), (635.11 ** (1 / 2)))

    def test_matrixUnitaria(self):
        a = [[(0,1/2**(1/2)),(0,-1/2**(1/2))],[(0,1/2**(1/2)),(0,1/2**(1/2))]]
        b = [[(1,3), (0, 5 / 15 ** (1 / 2)), (12, 1)], [(-5, 0), (0, 6), (2 / 2 * (19 ** (1 / 2)), -8 / 2 * (19 ** (1 / 2)))], [(0, -4.5), (20, 0), (2, 1)]]
        self.assertTrue(cMc.matrixUnitaria(a))
        self.assertFalse(cMc.matrixUnitaria(b))

    def test_matrixHermitiana(self):
        a = [[(5,0),(4,5),(6,-16)], [(4,-5),(13,0),(7,0)], [(6,16),(7,0),(-2.1,0)]]
        b = [[(5,0),(4,5),(6,-16)], [(4,-15),(13,0),(7,0)], [(6,6),(-7,0),(-2.1,0)]]
        self.assertTrue(cMc.matrixHermitiana(a))
        self.assertFalse(cMc.matrixHermitiana(b))
        
    def test_producTensorVector(self):
        a = [(3,-1),(4,5),(7,3)]
        b = [(-1,1),(2,0)]
        self.assertEqual(cMc.producTensorVector(a,b),[(-2,4),(6,-2),(-9,-1),(8,10),(-10,4),(14,6)])

    def test_producTensorMatrix(self):
        a = [[(0,0), (1,0)], [(1,0),(0,0)]]
        b = [[(1,0),(3,4)], [(0,0),(1,0)]]
        self.assertEqual(cMc.productTensorMatrix(a,b), [[(0,0),(0,0),(1,0),(3,4)],
                                                        [(0,0),(0,0),(0,0),(1,0)],
                                                        [(1,0),(3,4),(0,0),(0,0)],
                                                        [(0,0),(1,0),(0,0),(0,0)]])

    
if __name__=='__main__':
    unittest.main()
