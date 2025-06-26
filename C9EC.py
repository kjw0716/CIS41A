# CIS 41A Jackie Wang C9EC Bug class that moves left and right

class Bug:
    def __init__(self, p):
        self._p = p
        self._d = 1
    
    def turn(self):
        self._d = -self._d
    
    def move(self):
        self._p += self._d
    
    def getPosition(self):
        return self._p

def test_bug():
    """Test the Bug class functionality"""
    
    # Test 1: Initial position
    b = Bug(10)
    expected = 10
    actual = b.getPosition()
    print(f"Test 1 - Initial position: Expected {expected}, Actual {actual}")
    assert actual == expected, f"Test 1 failed: Expected {expected}, got {actual}"
    
    # Test 2: move right
    b.move()
    expected = 11
    actual = b.getPosition()
    print(f"Test 2 - Move right: Expected {expected}, Actual {actual}")
    assert actual == expected, f"Test 2 failed: Expected {expected}, got {actual}"
    
    # Test 3: Turn and move left
    b.turn()
    b.move()
    expected = 10
    actual = b.getPosition()
    print(f"Test 3 - Turn and move left: Expected {expected}, Actual {actual}")
    assert actual == expected, f"Test 3 failed: Expected {expected}, got {actual}"
    
    # Test 4: Multiple moves left
    b.move()
    expected = 9
    actual = b.getPosition()
    print(f"Test 4 - Multiple moves left: Expected {expected}, Actual {actual}")
    assert actual == expected, f"Test 4 failed: Expected {expected}, got {actual}"
    
    # Test 5: Turn back to right and move
    b.turn()
    b.move()
    expected = 10
    actual = b.getPosition()
    print(f"Test 5 - Turn back to right: Expected {expected}, Actual {actual}")
    assert actual == expected, f"Test 5 failed: Expected {expected}, got {actual}"
    
    # Test 6: Another bug with different initial position
    b2 = Bug(5)
    expected = 5
    actual = b2.getPosition()
    print(f"Test 6 - Second bug initial position: Expected {expected}, Actual {actual}")
    assert actual == expected, f"Test 6 failed: Expected {expected}, got {actual}"
    
    # Test 7: Multiple moves right
    b2.move()
    b2.move()
    expected = 7
    actual = b2.getPosition()
    print(f"Test 7 - Multiple moves right: Expected {expected}, Actual {actual}")
    assert actual == expected, f"Test 7 failed: Expected {expected}, got {actual}"
    
    # Test 8: Turn and multiple moves left
    b2.turn()
    b2.move()
    b2.move()
    b2.move()
    expected = 4
    actual = b2.getPosition()
    print(f"Test 8 - Turn and multiple moves left: Expected {expected}, Actual {actual}")
    assert actual == expected, f"Test 8 failed: Expected {expected}, got {actual}"
    
    print("\nAll tests completed! Bug class is working correctly.")

if __name__ == "__main__":
    test_bug()
'''
Test 1 - Initial position: Expected 10, Actual 10
Test 2 - Move right: Expected 11, Actual 11
Test 3 - Turn and move left: Expected 10, Actual 10
Test 4 - Multiple moves left: Expected 9, Actual 9
Test 5 - Turn back to right: Expected 10, Actual 10
Test 6 - Second bug initial position: Expected 5, Actual 5
Test 7 - Multiple moves right: Expected 7, Actual 7
Test 8 - Turn and multiple moves left: Expected 4, Actual 4

All tests completed! Bug class is working correctly.
'''