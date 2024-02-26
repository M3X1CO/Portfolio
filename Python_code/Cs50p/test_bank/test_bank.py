from bank import value

def main():
    # Call test functions
    test_return_zero()
    test_return_20()
    test_return_100()

# Test return 0
def test_return_zero():
    assert value('hello gi') == 0
    assert value('Hello') == 0
    assert value('HeLlo Gi') == 0

# Test return 20
def test_return_20():
    assert value('Hi') == 20
    assert value('hey') == 20

# Test return 100
def test_return_100():
    assert value("What's up?") == 100
    assert value('Good morning') == 100

if __name__ == "__main__":
    main()