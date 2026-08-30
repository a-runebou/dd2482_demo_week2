

def letter_shipping_cost(weight_g: int) -> int:
    """Calculate the shipping cost based on the weight in grams.
    https://www.postnord.se/privat/priser-och-villkor/portotabeller/portotabell-brev/

    Args:
        weight_g (int): The weight of the package in grams.

    Returns:
        int: The shipping cost.
    """
    if weight_g <= 0:
        raise ValueError("Weight must be positive") 

    if weight_g <= 50:
        return 22
    elif weight_g <= 100:
        return 44
    elif weight_g <= 250:
        return 66
    elif weight_g <= 500:
        return 88
    elif weight_g <= 1000:
        return 132
    elif weight_g <= 2000:
        return 154
    else:
        raise ValueError("Weight exceeds the maximum limit")