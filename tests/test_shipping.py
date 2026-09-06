# test_shipping.py
# Authors: Love Lindgren, Alexander Runebou
# Modified: 2026-09-06

import pytest
from shipping import (
    weight_price,
    destination_price,
    service_price,
    shipping_price,
    discount_price,
    Package,
    calculate_total_cost,
)


##################### Weight pricing #####################

def test_letter_up_to_50g():
    assert weight_price(25) == 22

def test_letter_up_to_100g():
    assert weight_price(75) == 44

def test_letter_up_to_250g():
    assert weight_price(200) == 66

def test_letter_up_to_500g():
    assert weight_price(450) == 88

def test_letter_up_to_1000g():
    assert weight_price(900) == 132

def test_letter_up_to_2000g():
    assert weight_price(1500) == 154

def test_weight_integer():
    with pytest.raises(TypeError, match="Weight must be an integer"):
        weight_price(50.5)

def test_letter_negative_weight():
    with pytest.raises(ValueError, match="Weight must be a positive integer"):
        weight_price(-1)

def test_letter_exceeds_max_weight():
    with pytest.raises(ValueError, match="Weight exceeds the maximum limit for our delivery service"):
        weight_price(2500)

##################### Destination pricing #####################

def test_domestic_destination():
    assert destination_price("domestic") == 25

def test_international_destination():
    assert destination_price("international") == 50

def test_global_destination():
    assert destination_price("global") == 100

def test_unknown_destination():
    with pytest.raises(ValueError, match="Unknown destination"):
        destination_price("bottom of the mariana trench")

##################### Service pricing #####################

def test_standard_service():
    assert service_price("standard") == 0

def test_express_service():
    assert service_price("express") == 100

def test_unknown_service():
    with pytest.raises(ValueError, match="Unknown delivery option"):
        service_price("today")

##################### Shipping price #####################

def test_standard_domestic_shipping():
    assert shipping_price(25, "domestic", "standard") == 47

def test_express_international_shipping():
    assert shipping_price(75, "international", "express") == 194

##################### Discount price #####################

def test_no_discount():
    assert discount_price(400, False) == 0

def test_sale_discount():
    assert discount_price(400, True) == 100

def test_value_based_and_sale_discount():
    assert discount_price(1000, True) == 200

def test_sale_discount_cannot_exceed_product_price():
    assert discount_price(67, True) == 67

def test_product_price_integer():
    with pytest.raises(TypeError, match="Price must be an integer"):
        discount_price(100.5, False)

def test_product_price_negative():
    with pytest.raises(ValueError, match="Price must be a positive integer"):
        discount_price(-1, False)

def test_sale_boolean():
    with pytest.raises(TypeError, match="Sale must be a boolean"):
        discount_price(420, 1)

##################### Total package cost #####################

def test_total_cost_minimal():
    package = Package(
        product_price = 1,
        weight = 1,
        destination = "domestic",
        service = "standard",
        sale = False,
    )

    assert calculate_total_cost(package) == 48