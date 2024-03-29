import os
from typing import Any

from src.core.modules import matching
from src.main import Assistant


def print_results(cmd_input: Any, result: Any, expected: Any) -> None:
    """
    Prints the result from a specific test

    Args:
        cmd_input (Any): The input given to the test
        result (Any): The test result
        expected (Any): The expected test result
    """

    print("\n[i] Input: {0}".format(cmd_input))
    print("[i] Result: {0}".format(result))
    print("[i] Expected: {0}".format(expected))


class TestMatching:
    """
    Tests the matching module for normal operation
    """

    def setup(self):
        self.instance = Assistant()
        self.instance.setup()

    @staticmethod
    def test_cmd_date() -> None:
        mock_input = "what's the date"
        expected_match = {"name": "date", "text": mock_input, "input": mock_input}

        matched_cmd = matching.get_match(mock_input)

        print_results(mock_input, matched_cmd, expected_match)

        assert matched_cmd == expected_match

    @staticmethod
    def test_cmd_time() -> None:
        mock_input = "what's the time"
        expected_match = {"name": "time", "text": mock_input, "input": mock_input}

        matched_cmd = matching.get_match(mock_input)

        print_results(mock_input, matched_cmd, expected_match)

        assert matched_cmd == expected_match

    @staticmethod
    def test_cmd_about_me() -> None:
        mock_input = "who are you"
        expected_match = {"name": "me_info", "text": mock_input, "input": mock_input}

        matched_cmd = matching.get_match(mock_input)

        print_results(mock_input, matched_cmd, expected_match)

        assert matched_cmd == expected_match

    @staticmethod
    def test_cmd_echo() -> None:
        mock_input = "repeat testing"
        expected_match = {"name": "echo", "text": "repeat", "input": mock_input}

        matched_cmd = matching.get_match(mock_input)

        print_results(mock_input, matched_cmd, expected_match)

        assert matched_cmd == expected_match

    # check if running on Github Actions
    # for now, the test below will not work and will throw an error

    if "GITHUB_ACTIONS" not in os.environ:

        @staticmethod
        def test_cmd_google_search() -> None:
            mock_input = "how old is Elon Musk"
            expected_match = {
                "name": "google_search",
                "text": mock_input,
                "input": mock_input,
            }

            matched_cmd = matching.get_match(mock_input)

            print_results(mock_input, matched_cmd, expected_match)

            assert matched_cmd == expected_match

    @staticmethod
    def test_cmd_google_news() -> None:
        mock_input = "tell me the news"
        expected_match = {"name": "news", "text": mock_input, "input": mock_input}

        matched_cmd = matching.get_match(mock_input)

        print_results(mock_input, matched_cmd, expected_match)

        assert matched_cmd == expected_match

    @staticmethod
    def test_cmd_note_add() -> None:
        mock_input = "new note i'm testing"
        expected_match = {"name": "note_add", "text": "new note", "input": mock_input}

        matched_cmd = matching.get_match(mock_input)

        print_results(mock_input, matched_cmd, expected_match)

        assert matched_cmd == expected_match

    @staticmethod
    def test_cmd_note_read() -> None:
        mock_input = "read my notes"
        expected_match = {"name": "note", "text": mock_input, "input": mock_input}

        matched_cmd = matching.get_match(mock_input)

        print_results(mock_input, matched_cmd, expected_match)

        assert matched_cmd == expected_match

    @staticmethod
    def test_cmd_note_clear() -> None:
        mock_input = "clear my notes"
        expected_match = {"name": "note_clear", "text": mock_input, "input": mock_input}

        matched_cmd = matching.get_match(mock_input)

        print_results(mock_input, matched_cmd, expected_match)

        assert matched_cmd == expected_match

    @staticmethod
    def test_cmd_weather() -> None:
        mock_input = "what's the weather"
        expected_match = {"name": "weather", "text": mock_input, "input": mock_input}

        matched_cmd = matching.get_match(mock_input)

        print_results(mock_input, matched_cmd, expected_match)

        assert matched_cmd == expected_match

    @staticmethod
    def test_cmd_register_install() -> None:
        mock_input = "register install"
        expected_match = {
            "name": "register_install",
            "text": mock_input,
            "input": mock_input,
        }

        matched_cmd = matching.get_match(mock_input)

        print_results(mock_input, matched_cmd, expected_match)

        assert matched_cmd == expected_match

    @staticmethod
    def test_cmd_coronavirus() -> None:
        mock_input = "covid cases"
        expected_match = {"name": "covid", "text": mock_input, "input": mock_input}

        matched_cmd = matching.get_match(mock_input)

        print_results(mock_input, matched_cmd, expected_match)

        assert matched_cmd == expected_match

    @staticmethod
    def test_cmd_commands() -> None:
        mock_input = "the commands"
        expected_match = {"name": "commands", "text": mock_input, "input": mock_input}

        matched_cmd = matching.get_match(mock_input)

        print_results(mock_input, matched_cmd, expected_match)

        assert matched_cmd == expected_match
