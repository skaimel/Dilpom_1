import pytest
from unittest.mock import Mock

from praktikum.burger import Burger


class TestBurger:
    def test_add_ingredient(self):
        burger = Burger()
        # Создаем моки для ингредиентов разных типов
        sauce_mock = Mock()
        filling_mock = Mock()
        burger.add_ingredient(sauce_mock)
        burger.add_ingredient(filling_mock)

        assert sauce_mock in burger.ingredients
        assert filling_mock in burger.ingredients

    def test_remove_ingredient(self):
        burger = Burger()
        # Создаем моки для ингредиентов указав их тип
        first_ingredient_mock = Mock()
        first_ingredient_mock.get_type.return_value = 'SAUCE'
        second_ingredient_mock = Mock()
        second_ingredient_mock.get_type.return_value = 'FILLING'
        burger.add_ingredient(first_ingredient_mock)
        burger.add_ingredient(second_ingredient_mock)
        # Удаляем первый ингредиент
        burger.remove_ingredient(0)
        # Проверяем, что первый ингредиент был удален, и второй ингредиент занял его место
        assert (burger.ingredients[0].get_type()) == 'FILLING'

    def test_move_ingredient(self):
        burger = Burger()
        # Создаем моки для ингредиентов
        first_ingredient_mock = Mock()
        second_ingredient_mock = Mock()
        burger.add_ingredient(first_ingredient_mock)
        burger.add_ingredient(second_ingredient_mock)
        # Перемещаем первый ингредиент на новую позицию
        burger.move_ingredient(0, 1)
        # Проверяем, что ингредиенты были перемещены и поменялись местами
        assert burger.ingredients == [second_ingredient_mock, first_ingredient_mock]

    def test_get_price_burger(self):
        burger = Burger()
        # Создаем мок-объект булочки
        bun_mock = Mock()
        bun_mock.get_price.return_value = 888
        # Создаем моки для ингредиентов и устанавливаем цену
        first_ingredient_mock = Mock()
        second_ingredient_mock = Mock()
        first_ingredient_mock.get_price.return_value = 66
        second_ingredient_mock.get_price.return_value = 99
        burger.set_buns(bun_mock)
        burger.add_ingredient(first_ingredient_mock)
        burger.add_ingredient(second_ingredient_mock)
        # Проверяем правильность расчета цены (цена булочки удваивается)
        assert burger.get_price() == 1941

    # При расчете цены не забыть, что цену булочки нужно удвоить
    @pytest.mark.parametrize("ingredient_data, expected_result", [
        ([("sauce", "No Way", 66), ("filling", "Infinity", 99)],
         "(==== Black Hole ====)\n= sauce No Way =\n= filling Infinity =\n(==== Black Hole ====)\n\nPrice: 1941"),
    ])
    #
    def test_get_receipt(self, ingredient_data, expected_result):
        burger = Burger()
        # Создаем мок-объект булочки, задаем ей наименование и цену
        bun_mock = Mock()
        bun_mock.get_name.return_value = "Black Hole"
        bun_mock.get_price.return_value = 888
        burger.set_buns(bun_mock)

        # Добавляем ингредиенты в бургер
        for ingredient_type, ingredient_name, ingredient_price in ingredient_data:
            ingredient_mock = Mock()
            ingredient_mock.get_type.return_value = ingredient_type
            ingredient_mock.get_name.return_value = ingredient_name
            ingredient_mock.get_price.return_value = ingredient_price
            # Добавляем созданный мок ингредиента в бургер
            burger.add_ingredient(ingredient_mock)

        assert burger.get_receipt() == expected_result