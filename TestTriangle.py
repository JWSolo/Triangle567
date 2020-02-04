# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
@author: jw
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')#fail

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')#fail
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')#fail
    
    def testInvalidInputA(self):
        self.assertEqual(classifyTriangle(0,0,0),'InvalidInput','0,0,0 is an invalid input')#pass

    def testInvalidInputB(self):
        self.assertEqual(classifyTriangle(201,210,300),'InvalidInput','201,210,200 is an invalid input')#pass

    def testInvalidInputC(self):
        self.assertEqual(classifyTriangle(1.9,2.1,3.9),'InvalidInput','1.9,2.1,3.9 is an invalid input')#pass
    
    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(4,6,11),'NotATriangle','4,6,11 should not be a triangle')#fail
    
    def testIsoceles(self):
        self.assertEqual(classifyTriangle(6,6,10),'Isoceles','6,6,10 should be Isoceles')#fail
    
    def testScalene(self):
        self.assertEqual(classifyTriangle(2,3,4),'Scalene','2,3,4 should be Scalene')#fail
        

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

