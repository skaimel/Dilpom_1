import pytest
from unittest.mock import Mock

from praktikum.burger import Burger


class TestBurger:
    def test_add_ingredient(self, get_burger_with_ingredients):
        burger, sauce_mock, filling_mock = get_burger_with_ingredients

        assert sauce_mock in burger.ingredients
        assert filling_mock in burger.ingredients

    def test_remove_ingredient(self, get_burger_with_different_ingredients):
        burger, sauce_mock, filling_mock = get_burger_with_different_ingredients
        burger.remove_ingredient(0)

        assert burger.ingredients == [filling_mock]

    def test_move_ingredient(self, get_burger_with_different_ingredients):
        burger, sauce_mock, filling_mock = get_burger_with_different_ingredients
        burger.move_ingredient(0, 1)

        assert burger.ingredients == [filling_mock, sauce_mock]

    def test_get_price_burger(self, get_burger_with_buns_and_ingredients):
        burger, bun_mock, first_ingredient_mock, second_ingredient_mock = get_burger_with_buns_and_ingredients

        assert burger.get_price() == 1941

    @pytest.mark.parametrize("ingredient_data, expected_result", [
        ([("sauce", "No Way", 66), ("filling", "Infinity", 99)],
         "(==== Black Hole ====)\n= sauce No Way =\n= filling Infinity =\n(==== Black Hole ====)\n\nPrice: 1941"),
    ])
    def test_get_receipt(self, ingredient_data, expected_result):
        burger = Burger()
        bun_mock = Mock()
        bun_mock.get_name.return_value = "Black Hole"
        bun_mock.get_price.return_value = 888
        burger.set_buns(bun_mock)

        for ingredient_type, ingredient_name, ingredient_price in ingredient_data:
            ingredient_mock = Mock()
            ingredient_mock.get_type.return_value = ingredient_type
            ingredient_mock.get_name.return_value = ingredient_name
            ingredient_mock.get_price.return_value = ingredient_price
            burger.add_ingredient(ingredient_mock)

        assert burger.get_receipt() == expected_result