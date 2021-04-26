from os.path import dirname, realpath, expanduser
from random import sample

from fastapi.testclient import TestClient

from sys import path; path.append( dirname(dirname(realpath(expanduser(__file__)))))
from app.main import app

client = TestClient(app)

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'

def test_first_item():
	response = client.get('/patentes/AAAA000')
	assert response.status_code == 200

def test_good_item():
	lts, nums = ''.join(sample(letters, 4)), ''.join(sample(numbers, 3))
	response = client.get(f'/patentes/{lts}{nums}')
	
	assert response.status_code == 200
	assert 'patente' in response.json().keys()

def test_more_letters():
	lts, nums = ''.join(sample(letters, 5)), ''.join(sample(numbers, 3))
	response = client.get(f'/patentes/{lts}{nums}')
	
	print(response.text)
	assert response.status_code == 200
	assert 'error' in response.json().keys()

def test_more_numbers():
	lts, nums = ''.join(sample(letters, 4)), ''.join(sample(numbers, 4))
	response = client.get(f'/patentes/{lts}{nums}')
	
	print(response.text)
	assert response.status_code == 200
	assert 'error' in response.json().keys()

def test_mixed_letters():
	lts, nums = ''.join(sample(numbers, 4)), ''.join(sample(letters, 3))
	response = client.get(f'/patentes/{lts}{nums}')
	
	print(response.text)
	assert response.status_code == 200
	assert 'error' in response.json().keys()  

def test_mixed_numbers():
	lts, nums = ''.join(sample(letters, 4)), ''.join(sample(letters, 3))
	response = client.get(f'/patentes/{lts}{nums}')
	
	print(response.text)
	assert response.status_code == 200
	assert 'error' in response.json().keys()
  