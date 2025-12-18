# gorping of testsfuctions under classes

# test class name should start with Test 

class TestMathOperations:
    def test_addition(self):
        assert 2 + 3 == 5

    def test_subtraction(self):
        assert 5 - 2 == 3
        
class TestStringOperations:
    def test_concatenation(self):
        assert "Hello, " + "World!" == "Hello, World!"

    def test_uppercase(self):
        assert "hello".upper() == "HELLO"
        
class Test_asfasf : 
    def test_asdfasf(self):
        assert 1 + 1 == 2
        
# making a  helperfuction under TestClas and grouping with different test functions

class TestHelperFunctions:
    def helper_multiply(self, a, b):
        return a * b

    def test_multiply_positive(self):
        assert self.helper_multiply(2, 3) == 6

    def test_multiply_negative(self):
        assert self.helper_multiply(-2, 3) == -6
        
    
