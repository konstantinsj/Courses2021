import pytest

class MyException(ValueError):
    def __init__(self, msg, code):
        super().__init__(msg)
        self.code = code

def test():
    with pytest.raises(MyException) as exc_info:
        raise MyException("error message", 43)

    assert exc_info.value.code == 42
