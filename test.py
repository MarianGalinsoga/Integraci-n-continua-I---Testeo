from main import par

def test_par():
    assert par(2) is True
    assert par(0) is True
    assert par(100) is True
    assert par(-4) is True

def test_impar():
    assert par(3) is False
    assert par(7) is False
    assert par(11) is False
    assert par(-5) is False
