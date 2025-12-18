import pytest

@pytest.fixture
def students():
    return {"names": ["ravi", "raj"], "ages": [12, 9]}

@pytest.mark.check
def test_name(students):
    assert "ravi" in students['names']

@pytest.mark.check
def test_age(students):
    assert students['ages'][0] > 9

def test_check(students): #deselected
    assert "raj" not in students['names']
# pytest -m check
print(students)
