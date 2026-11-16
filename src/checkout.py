def calculate_discounted_price(price, discount_percent):
    """Return the price after applying a percentage discount, rounded to cents."""
    if price < 0:
        raise ValueError("price cannot be negative")
    if not 0 <= discount_percent <= 100:
        raise ValueError("discount_percent must be between 0 and 100")

    return round(price * (1 - discount_percent / 100), 2)


def calculate_delivery_fee(order_total, distance_km):
    """Calculate delivery charge; orders of $50 or more ship free."""
    if order_total < 0:
        raise ValueError("order_total cannot be negative")
    if distance_km <= 0 or distance_km > 25:
        raise ValueError("distance_km must be greater than 0 and at most 25")

    if order_total >= 50:
        return 0.0
    if distance_km <= 5:
        return 3.99
    if distance_km <= 10:
        return 5.99
    return 8.99
