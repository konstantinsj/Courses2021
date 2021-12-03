Installation
============

## Install python 3.x from www.python.org

Download and install Python - https://www.python.org/downloads/. If Python is already installed and is fairly recent (3.8+),
that can be used as well.

When installing, select "Add Python x.x to PATH", so `python`, `pip` and other Python related binaries are accessible from the shell. 

Verify installation by launching shell and running `python` command.

Code editor with Python support is highly recommended - PyCharm, VS Code or anything else you are already familiar with will work.

## Install pytest

If Python is properly installed and available in shell, `pip` can be used to install `pytest`:
```
pip install pytest
```

Verify installation:
```
pytest --version
```

Hello world
===========

- basic test module with one test - [test_helloworld.py](test_helloworld.py)

Pytest invocation
=================

- verbose output - `pytest -v`
- stopping after failures
  - stop after first failure - `pytest -x`, `pytest --maxfail=1`
  - stop after first N failures - `pytest --maxfail=N`
- selecting tests to be run
  - default test look-up
  - run all tests in a Python module - `pytest test_helloworld.py`
  - run specific tests by specifying method or class
    - run specific test in the module - `pytest test_run_specific_test::test_pass`
    - run all tests in the class in the module - `pytest test_run_specific_test.py::TestSomething`
    - run specific test in the class in the module - `pytest test_run_specific_test::TestSomething::test_something`
  - filter by keywords
    - test name contains string - `pytest -k pass`
    - boolean operators: and, or, not etc - `pytest -k "not fail"`
  - filter by marks
- show stdout
  - automatically captured for failed tests - `pytest test_stdout_fail.py`
  - can be shown for passed tests - `pytest -s test_stdout_pass.py`


Test result
===========


Test parametrization
====================


Course outline
==============

* Marks
* Test parametrization
* Excercise 1
* conftest.py
* Fixtures
* Excercise 2
* Allure integration
* Pytest plug-ins and test config
* Excercise 3
