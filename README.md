# Lab 4: Automated Unit Testing
## Files
    helpers.py                  code under test (do NOT edit)
    test_helpers.py             YOUR file: write your tests here
    PYTEST_CHEATSHEET.md        quick reference
    requirements.txt            pytest
    pytest.ini                  pytest settings (leave as is)
    run_tests.bat               double-click to run all tests (Windows)
    Lab4_Automated_Unit_Testing.pptx   lab slides

## Setup (Windows PowerShell)
    python --version
    python -m pip install -r requirements.txt
    python -m pytest --version

If `pip` or `pytest` is "not recognized", always put `python -m` in front.

## Do the lab
1. Unzip this folder, open PowerShell inside it (cd to the folder).
2. Run `python -m pytest -v`. The 4 example tests should pass.
3. Open test_helpers.py and work through the TODO list at the bottom.
4. Use plain assert tests, at least one @pytest.mark.parametrize test,
   and at least one Test* class.
5. Cover edge cases and use pytest.raises for expected errors.
6. Run `python -m pytest -v` until everything passes.

## Submit
- test_helpers.py with at least 15 unit tests
- A screenshot of `python -m pytest -v` with all tests passing
