import pytest
from src.checkout import calculate_discounted_price

def test_calculate_discounted_price_valid():
    price = 100
    discount_percent = 20

    result = calculate_discounted_price(price, discount_percent)

    assert result == 80.00


@pytest.mark.parametrize(
    ("price", "discount_percent"),
    [
        (-1, 10),  # negative price
        (10, 101),  # discount too high
    ],
)
def test_calculate_discounted_price_invalid(price, discount_percent):
    with pytest.raises(ValueError):
        calculate_discounted_price(price, discount_percent)
