import pytest
from unittest.mock import Mock

from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger

@pytest.fixture
def get_mock_bun():
    bun = Mock(spec=Bun)
    bun.name = "Черная дыра"
    bun.price = 888

    return bun

@pytest.fixture
def get_sauce_ingredient():
    return Ingredient("SAUCE", "No Way", 66)

@pytest.fixture
def get_filling_ingredient():
    return Ingredient("FILLING", "Infinity", 99)

@pytest.fixture
def get_burger_with_ingredients():
    burger = Burger()
    sauce_mock = Mock()
    filling_mock = Mock()
    burger.add_ingredient(sauce_mock)
    burger.add_ingredient(filling_mock)

    return burger, sauce_mock, filling_mock

@pytest.fixture
def get_burger_with_different_ingredients():
    burger = Burger()
    sauce_mock = Mock()
    filling_mock = Mock()
    burger.add_ingredient(sauce_mock)
    burger.add_ingredient(filling_mock)

    return burger, sauce_mock, filling_mock

@pytest.fixture
def get_burger_with_buns_and_ingredients():
    burger = Burger()
    bun_mock = Mock()
    bun_mock.get_price.return_value = 888
    burger.set_buns(bun_mock)
    first_ingredient_mock = Mock()
    second_ingredient_mock = Mock()
    first_ingredient_mock.get_price.return_value = 66
    second_ingredient_mock.get_price.return_value = 99
    burger.add_ingredient(first_ingredient_mock)
    burger.add_ingredient(second_ingredient_mock)

    return burger, bun_mock, first_ingredient_mock, second_ingredient_mock