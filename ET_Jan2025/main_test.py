import pytest

class TestGroup:
    def do_something(self, x, y):
        return x % y

    def test_one(self):
        assert self.do_something(10, 5) == 0, " Is 5 factor of 10? " # 10 % 5 == 0 true

    def test_two(self):
        assert self.do_something(32, 5) == 0, " Is 5 factor of 32 " # 32 % 5 == 0 false