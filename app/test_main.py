import datetime
import pytest
from app.main import outdated_products
from unittest import mock
from typing import Any


@pytest.mark.parametrize(
    "products,result",
    [
        ([{"name": "salmon",
           "expiration_date": datetime.date(2024, 12, 31),
           "price": 600.0}],
         ["salmon"]),
        ([{"name": "chicken",
           "expiration_date": datetime.date(2025, 1, 30),
           "price": 120.0}],
         []),
        ([{"name": "duck",
           "expiration_date": datetime.date(2025, 2, 3),
           "price": 160.0}],
         []),
        ([{"name": "tuna",
           "expiration_date": datetime.date(2024, 12, 31),
           "price": 95.0}],
         ["tuna"]),
        ([{"name": "beef",
           "expiration_date": datetime.date(2025, 1, 30),
           "price": 200.0},
          {"name": "pork",
           "expiration_date": datetime.date(2025, 2, 3),
           "price": 150.0},
          {"name": "crab",
           "expiration_date": datetime.date(2024, 2, 28),
           "price": 650.0},
          {"name": "horse",
           "expiration_date": datetime.date(2020, 7, 30),
           "price": 950.0}],
         ["crab", "horse"]),
    ],
)
@mock.patch("app.main.datetime")
def test_outdated_products(
    mock_today: Any,
    products: Any,
    result: Any
) -> None:
    mock_today.date.today.return_value = datetime.date(2025, 1, 3)
    assert outdated_products(products) == result
