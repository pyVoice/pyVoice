from src.main import Assistant
from src.core.modules import matching


class TestMatching:
    """
    Tests the matching module for normal operation
    """

    def setup(self):
        self.instance = Assistant()
        self.instance.setup()

    def test_cmd_date(self) -> None:
        mock_input: str = "what's the date"
        output_dict = {
            "name": "date",
            "text": "what's the date",
            "input": mock_input
        }

        assert matching.check_match(mock_input) == output_dict

    def test_cmd_about_me(self):
        mock_input: str = "who are you"
        output_dict = {
            "name": "me_info",
            "text": "who are you",
            "input": mock_input
        }

        assert matching.check_match(mock_input) == output_dict
