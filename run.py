"""
Start script
"""

from src.main import Assistant

from memory_profiler import profile

f = open("memory.log", "w+")


@profile(stream=f)
def main():
    instance = Assistant()
    instance.run()


if __name__ == '__main__':
    main()
