import pytest
from src.checkout import calculate_delivery_fee

@pytest.mark.parametrize(
    ("order_total", "distance_km", "expected_fee"),
    [
        (20, 3, 3.99),  # up to 5 km
        (20, 8, 5.99),  # up to 10 km
        (50, 3, 0.0),  # free delivery for orders of $50 or more
        (20, 15, 8.99),  # above 10 km
    ],
)
def test_calculate_delivery_fee(order_total, distance_km, expected_fee):
    assert calculate_delivery_fee(order_total, distance_km) == expected_fee


@pytest.mark.parametrize(
    ("order_total", "distance_km"),
    [
        (-1, 5),  # negative order total
        (20, 0),  # zero distance
        (20, 26),  # beyond 25 km
    ],
)
def test_calculate_delivery_fee_invalid(order_total, distance_km):
    with pytest.raises(ValueError):
        calculate_delivery_fee(order_total, distance_km)

