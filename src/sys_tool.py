import sys


def main():
    if "--help" in sys.argv:
        print("Використання: python src/sys_tool.py [--help]")
        return

    print("командна строка")


if __name__ == "__main__":
    main()