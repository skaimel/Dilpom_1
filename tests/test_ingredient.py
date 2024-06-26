import pytest
from praktikum.ingredient import Ingredient


class TestIngredient:
    @pytest.mark.parametrize("ingredient_type, name, price", [
        ("SAUCE", "No Way", 66),
        ("FILLING", "Infinity", 99),
    ])
    def test_new_ingredient(self, ingredient_type, name, price):
        # Создаем новый ингредиент new_ingredient с переданными параметрами
        new_ingredient = Ingredient(ingredient_type, name, price)

        assert new_ingredient.get_type() == ingredient_type
        assert new_ingredient.get_name() == name
        assert new_ingredient.get_price() == price

    def test_get_price_new_ingredient(self):
        # Cоздаем новый ингредиент с ценой 66
        new_ingredient = Ingredient("SAUCE", "No Way", 66)

        assert new_ingredient.get_price() == 66

    def test_get_name_ingredient(self):
        # Cоздаем новый ингредиент с названием "No Way'
        new_ingredient = Ingredient("SAUCE", "No Way", 66)

        assert new_ingredient.get_name() == "No Way"

    def test_get_type_ingredient(self):
        # Cоздаем новый ингредиент с типом "SAUCE"
        new_ingredient = Ingredient("SAUCE", "No Way", 66)

        assert new_ingredient.get_type() == "SAUCE"