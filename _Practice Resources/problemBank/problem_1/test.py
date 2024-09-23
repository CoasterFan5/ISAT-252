
test_cases = [
    ["", "hello"]
]

def test(func):
    if func() == "hello":
        print("test passed")
        return True
    else:
        print("test failed")
        return False

do_test(test())
