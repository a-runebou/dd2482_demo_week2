# Pricing specification

## Weight price

| Weight      |  Price |
| ----------- | -----: |
| 1–50 g      |  22 kr |
| 51–100 g    |  44 kr |
| 101–250 g   |  66 kr |
| 251–500 g   |  88 kr |
| 501–1000 g  | 132 kr |
| 1001–2000 g | 154 kr |

Weight must be a positive integer and may not exceed 2000 g.

## Destination

| Destination   |  Price |
| ------------- | -----: |
| domestic      |  25 kr |
| international |  50 kr |
| global        | 100 kr |

## Service

| Service  |  Price |
| -------- | -----: |
| standard |   0 kr |
| express  | 100 kr |

## Discounts

| Condition              |                                Discount |
| ---------------------- | --------------------------------------: |
| product price < 500 kr |                                    0 kr |
| 500–1999 kr            |            25 kr + 10% of product price |
| 2000–4999 kr           |            100 kr + 5% of product price |
| ≥ 5000 kr              |            200 kr + 1% of product price |
| sale = true            | additional `min(100 kr, product price)` |

Percentage calculations use integer arithmetic, so fractional kronor are discarded.

## Shipping price

shipping price = weight price + destination price + service price

## Total cost

total cost = product price + shipping price - discount