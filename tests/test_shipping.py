from shipping import postage_price

def test_letter_up_to_50g():
    assert postage_price(25) == 22

def test_letter_up_to_100g():
    assert postage_price(75) == 44

def test_letter_up_to_250g():
    assert postage_price(200) == 66

def test_letter_up_to_500g():
    assert postage_price(450) == 88

def test_letter_up_to_1000g():
    assert postage_price(900) == 132

def test_letter_up_to_2000g():
    assert postage_price(1500) == 154

def test_letter_with_negative_weight():
    try:
        postage_price(-1)
    except ValueError as e:
        assert str(e) == "Weight must be positive"
    else:
        assert False, "Expected ValueError for negative weight"

def test_letter_exceeds_max_weight():
    try:
        postage_price(2500)
    except ValueError as e:
        assert str(e) == "Weight exceeds the maximum limit"
    else:
        assert False, "Expected ValueError for weight exceeding maximum limit"