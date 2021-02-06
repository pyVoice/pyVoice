"""
Check installation
"""


def check_for_missing_packages() -> bool:
    """
    Returns a boolean value after checking if all the packages are installed in the venv
    """
    missing_packages = False
    packages = ['speech_recognition']

    print("Checking packages...")
