from calculator import calculer_moyenne

def test_calculer_moyenne():
    assert calculer_moyenne([1, 2, 3, 4, 5]) == 5.0
    assert calculer_moyenne([10, 20, 30, 40, 50]) == 30.0
    assert calculer_moyenne([0, 0, 0, 0, 0]) == 0.0
