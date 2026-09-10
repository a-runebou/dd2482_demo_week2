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

# Original: if 25 <= 50
# Mutation: if 25 < 50

@pytest.mark.parametrize("weight, expected",
    [
        (1, 22),
                (50, 22),
                (51, 44),
                (100, 44),
                (101, 66),
                (250, 66),
        
                (251, 88),
                (500, 88),
        
                (501, 132),
                (1000, 132),
        
                (1001, 154),
                (2000, 154)
    ])


def test_weight_price_boundaries(weight, expected):
    assert weight_price(weight) == expected

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

@pytest.mark.parametrize("destination, expected",
    [("domestic", 25),
     ("international", 50),
     ("global", 100)])
def test_destination_price_boundaries(destination, expected):
    assert destination_price(destination) == expected

def test_invalid_destination():
    with pytest.raises(ValueError, match="Invalid destination"):
        destination_price("bottom of the mariana trench")

##################### Service pricing #####################

@pytest.mark.parametrize("service, expected",
    [("standard", 0),
     ("express", 100)])
def test_service_price_boundaries(service, expected):
    assert service_price(service) == expected

def test_invalid_service():
    with pytest.raises(ValueError, match="Invalid delivery option"):
        service_price("Literally 1984")

##################### Shipping price #####################

@pytest.mark.parametrize("weight, destination, service, expected",
    [(25, "domestic", "standard", 47),
     (75, "international", "express", 194)])
def test_shipping_price_combinations(weight, destination, service, expected):
    assert shipping_price(weight, destination, service) == expected

##################### Discount price #####################

@pytest.mark.parametrize(
    "price, sale, expected",
    [(400, False, 0),
     (750, False, 100),
     (2500, False, 225),
     (6500, False, 265),
     (400, True, 100)])
def test_discount_price_boundaries(price, sale, expected):
    assert discount_price(price, sale) == expected

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

@pytest.mark.parametrize("package, expected",
    [(Package(1, 1, "domestic", "standard", False), 48)])
def test_calculate_total_cost(package, expected):
    assert calculate_total_cost(package) == expected