a = '''
    Notes for pytest:
    - pytest is a testing framework for Python that makes it easy to write simple and scalable tests.
    - It allows you to write test functions using simple assert statements.
    Example:
    def test_addition():
        assert 2 + 3 == 5



'''

import pytest
from app import app 

def salery(amount , tax=0.2):
    return amount + 1000 - (amount * tax)


@pytest.fixture # Decorator to define a fixture which can be used in tests 
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, World!' in response.data

def test_about(client):
    response = client.get('/about')
    assert response.status_code == 200
    assert b'This is the   about page.' in response.data

def test_greet(client):
    response = client.get('/greet/Alice')
    assert response.status_code == 200
    assert b'Hello, Alice!' in response.data










@pytest.fixture
def sample_fixture_List():
    return [1, 2, 3, 4, 5]

@pytest.fixture
def sample_fixture_Dict():
    return {'a': 1, 'b': 2, 'c': 3}



def test_1(sample_fixture_List):
    assert sum(sample_fixture_List) == 15
    
def test1234124(sample_fixture_List):
    assert sum(sample_fixture_List) == 15    
    
def test_2(sample_fixture_List): 
    print("List Fixture:", sample_fixture_List)
    assert sample_fixture_List == []
    
    
def test_3(sample_fixture_Dict):
    assert sample_fixture_Dict['a'] == 1