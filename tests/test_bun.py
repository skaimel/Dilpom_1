from unittest.mock import Mock


class TestBun:

    def test_get_name_bun(self):
        # Создаем мок-объект булочки
        mock_bun = Mock()
        mock_bun.name = "Черная дыра"

        assert mock_bun.name == "Черная дыра"

    def test_get_price_bun(self):
        # Создаем мок-объект булочки
        mock_bun = Mock()
        mock_bun.price = 888

        assert mock_bun.price == 888