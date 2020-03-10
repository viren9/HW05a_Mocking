"""author: viren ghori"""
import unittest

from HW02_VGhori import classify_triangle

class TestTriangles(unittest.TestCase):

    def testEquilateralTriangle1(self): 
        self.assertEqual(classify_triangle(1,1,1),'Equilateral Triangle')

    def testEquilateralTriangle2(self): 
        self.assertEqual(classify_triangle(2,2,2),'Equilateral Triangle')

    def testIsocelesTriangle3(self): 
        self.assertEqual(classify_triangle(2,2,1),'Isosceles Triangle')
    
    def testIsocelesTriangle4(self):     
        self.assertEqual(classify_triangle(2,1,2),'Isosceles Triangle')

    def testRightTriangle5(self): 
        self.assertEqual(classify_triangle(1,2,3),'Right Angled Triangle')

    def testScaleneTriangleA(self): 
        self.assertEqual(classify_triangle(6,5,4),'Scalene Triangle')

if __name__ == '__main__':
    unittest.main()
