import palindrome
import unittest 

cases = ["bobdhv","jbihbob", "noonsjhkj","sdkbjnoon","jksdfbobanfb", "absvnoonsjdf","bobnoonsjhvdbobasdnoonjavdbobahnoon"]
#unittest class to test module palindrome.py
class testPalindrome(unittest.TestCase):
    
    #odd palindrome at start of string
    def test_pal_odd_start(self): 
        self.assertEqual(palindrome.pal(cases[0]),["bob"],"incorrect output")
    
    #odd palindrome at end of string
    def test_pal_odd_end(self):
        self.assertEqual(palindrome.pal(cases[1]),["bob"],"incorrect output")
    
    #even palindrome at start of string
    def test_pal_even_start(self):
        self.assertEqual(palindrome.pal(cases[2]),["noon"],"incorrect output")
    
    #even palindrome at end of string
    def test_pal_even_end(self):
        self.assertEqual(palindrome.pal(cases[3]),["noon"],"incorrect output")
    
    #odd palindrome at middle of string
    def test_pal_odd_middle(self):
        self.assertEqual(palindrome.pal(cases[4]),["bob"],"incorrect output")

    #even palindrome at middle of string
    def test_pal_even_middle(self):
        self.assertEqual(palindrome.pal(cases[5]),["noon"],"incorrect output")

    #even and odd palindromes throughout string
    def test_pal_odd_even(self):
        self.assertEqual(palindrome.pal(cases[6]),["bob","noon","bob","noon","bob","noon"],"incorrect output")

if __name__ == '__main__': #allows code to run within the interpreter
    unittest.main()

