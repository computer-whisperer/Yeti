from os import path

import pytest


@pytest.fixture(scope="function")
def yeti():
    import yeti
    return yeti

@pytest.fixture(scope="function")
def engine(yeti):
    return yeti.Engine()

@pytest.fixture(scope="function")
def resources_dir():
    return path.join(path.dirname(path.realpath(__file__)), "resources")