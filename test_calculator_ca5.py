# -*- coding: utf-8 -*-
"""
Created on 16_09_2018
@author: 10042994
"""
import unittest
from calculator_ca5 import add, divide, exponent, multiply,subtract,square_root,square,power,cube,factorial,PowTwoGen,getOddNum

class CalculatorTest(unittest.TestCase):

    def testAdd(self):
        self.assertEqual(10, add([1, 2, 3, 4]))
        self.assertEqual(3, add([1, 2]))
    
    def testDivide(self):
        self.assertEqual(2.0, divide([16, 4, 2, 1]))

    def testExponent(self):
        self.assertEqual(4294967296, exponent([16, 4, 2, 1]))
    

    def testMultiply(self):
        self.assertEqual(24, multiply([1, 2, 3, 4]))
   

    def testSubtract(self):
        self.assertEqual(9, subtract([16, 4, 2, 1]))
     
        
    def testSquare_root(self):
        self.assertSequenceEqual([4.0, 2.0, 1.4142135623730951, 1.0], square_root([16, 4, 2, 1]))
       

    def testSquare(self):
            self.assertSequenceEqual([1, 4, 9, 16], square([1, 2, 3, 4]))
          
            
            
    def testPower(self):
            self.assertEqual(1, power([1, 2, 3, 4]))
      
            
    def testCube(self):
            self.assertSequenceEqual([1, 8, 27, 64], cube([1, 2, 3, 4]))
       
            
    def testFactorial(self):
            self.assertSequenceEqual([120, 24, 2, 1], factorial([5, 4, 2, 1]))
           
    def testPowTwoGen(self):
            self.assertSequenceEqual([1,2,4], list(PowTwoGen(3)))
            
        
    def testGetOddNum(self):
            self.assertSequenceEqual([1,3], getOddNum([1,3,4,6,8]))
    
    
    unittest.main()
  
