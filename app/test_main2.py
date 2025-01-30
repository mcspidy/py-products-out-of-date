import datetime
import pytest
from app.main import outdated_products
from unittest import mock
from typing import Any


@pytest.mark.parametrize(
    "product_list, today_date, expected_output",
    [
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2024, 12, 21),
                    "price": 600.0
                }
            ],
            datetime.date(2024, 12, 22),
            ["salmon"],
            id="Check for 1 outdated product"
        ),
        pytest.param(
            [
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 5),
                    "price": 120.0
                },
                {
                    "name": "beef",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 120.0
                }
            ],
            datetime.date(2024, 12, 22),
            ["chicken", "beef"],
            id="Check for 2 outdated product"
        ),
        pytest.param(
            [
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 5),
                    "price": 120.0
                },
                {
                    "name": "beef",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 120.0
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 2),
                    "price": 160.0
                }
            ],
            datetime.date(2024, 12, 22),
            ["chicken", "beef", "duck"],
            id="Check for 3 outdated product"
        ),
        pytest.param(
            [
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2024, 12, 23),
                    "price": 120.0
                },
                {
                    "name": "beef",
                    "expiration_date": datetime.date(2024, 12, 23),
                    "price": 120.0
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2024, 12, 23),
                    "price": 160.0
                }
            ],
            datetime.date(2024, 12, 22),
            [],
            id="Check for no outdated products"
        ),
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2024, 12, 22),
                    "price": 600
                },
            ],
            datetime.date(2024, 12, 22),
            [],
            id="today's date is not expired"
        ),
    ],
)
@mock.patch("datetime.date")
def test_outdated_products(
    mocked_date: Any,
    product_list: Any,
    today_date: Any,
    expected_output: Any
) -> None:
    mocked_date.today.return_value = today_date
    assert outdated_products(product_list) == expected_output
