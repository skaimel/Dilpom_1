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

    def test_get_price_new_ingredient(self, get_sauce_ingredient):
        # Тестируем, что цена ингредиента с типом SAUCE равна 66
        assert get_sauce_ingredient.get_price() == 66

    def test_get_name_ingredient(self, get_sauce_ingredient):
        # Тестируем, что название ингредиента с типом SAUCE равно "No Way"
        assert get_sauce_ingredient.get_name() == "No Way"

    def test_get_type_ingredient(self, get_sauce_ingredient):
        # Тестируем, что тип ингредиента с типом SAUCE равен "SAUCE"
        assert get_sauce_ingredient.get_type() == "SAUCE"

    def test_get_another_ingredient(self, get_filling_ingredient):
        # Тестируем, что цена ингредиента с типом FILLING равна 99
        assert get_filling_ingredient.get_price() == 99