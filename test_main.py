import unittest
import itertools
import numpy as np
from main import *

class UnitTests(unittest.TestCase) :
    def test_permutations(self) :
        for i in range(1,7) : 
            student_perms = permutations(i)
            self.assertTrue( len(student_perms)==np.math.factorial(i), "Your code is not generating all the permutations" )
            for seq in student_perms : self.assertTrue( len(seq)==i, "Your code is not generating all the permutations" )
  
            myinp = i*[0] 
            for j in range(i) : myinp[j] = j+1 
  
            for seq in itertools.permutations(myinp) : 
               found=False
               for sseq in student_perms : 
                  isseq=True 
                  for k in range(len(seq)) : 
                      if seq[k]!=sseq[k] : isseq=False
                  if isseq : 
                     found=True
                     break
               self.assertTrue( found, "Your code is not generating all the permutations" )
