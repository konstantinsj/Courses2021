import pytest


def calculator(operation, a, b):
    if operation == "sum":
        return a + b
    elif operation == "sub":
        return a - b
    elif operation == "mul":
        return a * b
    elif operation == "div":
        return a / b
    else:
        raise ValueError("unknown operation")


# write the test cases for above method
@pytest.mark.parametrize("operation, a, b, expected",
                         [("sum", 2, 2, 4), ("sub", -2, 2, -4), ("mul", -2, -3, 6), ("div", 5, 2.5, 2)])
def test(operation, a, b, expected):
    assert calculator(operation, a, b) == expected


@pytest.mark.parametrize("a, exc", [("null", ValueError), ("div", ZeroDivisionError)])
def test_exceptions(a, exc):
    with pytest.raises(exc):
        calculator(a, 1, 0)