# what is the purpose? place to put fixtures
# similar to argparse below 

from config import Config
from pytest import fixture

def pytest_addoption(parser):
    parser.addoption("--env", action = "store", help="Environment to run tests against")
    
@fixture(scope='session')
def env(request)-> str: #request is just given to us by pytest.  request holds all info given on command line
    return request.config.getoption("--env") 

@fixture(scope='session')
def app_config(env):
    cfg = Config(env)
    return cfg
