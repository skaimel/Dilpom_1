class TestBun:

    def test_get_name_bun(self, get_mock_bun):
        assert get_mock_bun.name == "Черная дыра"

    def test_get_price_bun(self, get_mock_bun):
        assert get_mock_bun.price == 888