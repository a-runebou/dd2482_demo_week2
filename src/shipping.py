# shipping.py
# Authors: Love Lindgren, Alexander Runebou
# Modified: 2026-09-06

from dataclasses import dataclass


@dataclass
class Package:
    product_price: int
    weight: int
    destination: str
    service: str
    sale: bool


def weight_price(weight: int) -> int:
    """Calculate the surcharge for the package's weight.
    https://www.postnord.se/privat/priser-och-villkor/portotabeller/portotabell-brev/

    Args:
        weight (int): The weight of the package in grams.

    Returns:
        int: The package's weight cost.
    """
    if not isinstance(weight, int):
        raise TypeError("Weight must be an integer")
    if weight <= 0:
        raise ValueError("Weight must be a positive integer")

    if weight <= 50:
        return 22
    elif weight <= 100:
        return 44
    elif weight <= 250:
        return 66
    elif weight <= 500:
        return 88
    elif weight <= 1000:
        return 132
    elif weight <= 2000:
        return 154
    else:
        raise ValueError("Weight exceeds the maximum limit for our delivery service")


def destination_price(destination: str) -> int:
    """Calculates the surcharge for the package's destination"""
    match destination:
        case "domestic":
            return 25
        case "international":
            return 50
        case "global":
            return 100
        case _:
            raise ValueError("Unknown destination")


def service_price(service: str) -> int:
    """Calculates the surcharge for the package's delivery method"""
    match service:
        case "standard":
            return 0
        case "express":
            return 100
        case _:
            raise ValueError("Unknown delivery option")



def shipping_price(weight: int, destination: str, service: str) -> int:
    """Calculate the shipping cost based on the weight in grams, destination, and delivery method"""
    price = weight_price(weight)
    price += destination_price(destination)
    price += service_price(service)

    return price


def discount_price(product_price: int, sale: bool) -> int:
    """Calculate the total discount applied to a package"""
    if not isinstance(product_price, int):
        raise TypeError("Price must be an integer")
    if product_price <= 0:
        raise ValueError("Price must be a positive integer")
    if not isinstance(sale, bool):
        raise TypeError("Sale must be a boolean")

    discount_price = 0

    if product_price >= 500:                            # Value-based discount
        discount_price += (product_price * 10 // 100)
    if sale:                                            # Promotional discount
        discount_price += min(100, product_price)
    return discount_price


def calculate_total_cost(package: Package) -> int:
    """Calculate the total cost of a package, including shipping price and discounts"""
    price = package.product_price
    price += shipping_price(package.weight, package.destination, package.service)
    price -= discount_price(package.product_price, package.sale)

    return price
