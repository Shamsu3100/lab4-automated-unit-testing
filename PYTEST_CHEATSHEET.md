# pytest Cheat Sheet (Lab 4)

## Run
    python -m pytest                 run everything
    python -m pytest -v              one line per test
    python -m pytest -k slugify      only tests with "slugify" in the name
    python -m pytest -x              stop at the first failure
    python -m pytest --collect-only  list tests without running them
    python -m pytest test_helpers.py::TestAddDays   run one class

## Naming (test discovery)
- file:      test_*.py
- function:  test_*
- class:     Test*  (methods test_*, no __init__)

## Assertions
    assert a == b
    assert cond
    assert not cond
    assert x is None
    assert x in y
    assert 0.1 + 0.2 == pytest.approx(0.3)

## Expected errors
    with pytest.raises(TypeError):
        format_currency("free")

## Parameterized test
    @pytest.mark.parametrize("value,expected", [(1, True), (0, False)])
    def test_priority(value, expected):
        assert is_valid_priority(value) == expected

## Test class (suite)
    class TestSlugify:
        def test_basic(self):
            assert slugify("Hi There") == "hi-there"
