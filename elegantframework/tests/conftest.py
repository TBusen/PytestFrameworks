from pytest import fixture
from selenium import webdriver
import json

data_path = 'test_data.json'

@fixture(params=[webdriver.Chrome, webdriver.Safari])
def browser(request):
    driver = request.param
    drvr = driver()
    yield drvr #yielding instead of return so we can shut it down when we are done
    drvr.quit()

def load_test_data(path):
    with open(path) as data_file:
        data = json.load(data_file)
        return data

@fixture(params=load_test_data(data_path))
def tv_brand(request):
    data = request.param
    return data
