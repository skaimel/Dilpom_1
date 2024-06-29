from praktikum.database import Database


class TestDataBase:

    def test_available_buns(self):
        database = Database()
        # Проверяем, что количество доступных булочек равно 3
        assert len(database.available_buns()) == 3

    def test_available_ingredients(self):
        database = Database()
        # Проверяем, что количество доступных ингредиентов равно 6
        assert len(database.available_ingredients()) == 6