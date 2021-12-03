import pytest

@pytest.fixture(scope="function")
def resource():
    print("\nfixture initialization")
    yield "i am the resource"
    print("\nfixture finalization")

@pytest.fixture(scope="session")
def another_resource(resource):
    # This will not work, because fixture with broader scope ("session")
    # cannot use fixture with narrower scope ("function")
    print("\nanother_resource init")
    yield "i am another resource"
    print("\nanother_resource finit")

def test(another_resource):
    print("\nexecuting test case")

def test2(another_resource):
    print("\nexecuting test case 2")


