import pytest
from heroes import Hero

@pytest.fixture
def create_hero(request):
    # print(f"this is request: {request.param['name']}")
    return Hero(request.param['name'], request.param['power'], request.param['health'], request.param['speed'])