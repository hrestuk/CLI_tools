import fire

from utils import greet, goodbye

def main():
    fire.Fire({
        "greet": greet,
        "goodbye": goodbye,
    })

if __name__ == "__main__":
    main()