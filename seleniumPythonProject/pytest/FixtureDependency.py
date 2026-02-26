# fixture dependency - the second fixture will only work when the first fixture

import pytest
def test(fixture_b):
    assert fixture_b == "Data from A + Data from B"