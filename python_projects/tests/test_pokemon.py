import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2/'
HEADER = {
    'Content-Type': 'application/json',
    'trainer_token': 'TOKEN'
}
TRAINER_ID = '22318'

def test_status_code():
    response_status = requests.get(url = f'{URL}trainers')
    assert response_status.status_code == 200

def test_trainer_name():
    response_name = requests.get(url = f'{URL}trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_name.json()["data"][0]["trainer_name"] == 'makeml'