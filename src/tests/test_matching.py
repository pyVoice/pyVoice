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
        expected_match = {
            "name": "date",
            "text": "what's the date",
            "input": mock_input
        }

        matched_cmd = matching.get_match(mock_input)

        # convert to separate method
        print("\n[i] Result: {0}".format(matched_cmd))
        print("[i] Expected: {0}".format(expected_match))

        assert matched_cmd == expected_match
        # assert matching.execute_match()
