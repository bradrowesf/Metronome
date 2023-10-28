import argparse


def main():

    parser = argparse.ArgumentParser(description="Metronome Testbed")
    parser.add_argument("command")
    args = parser.parse_args()

    print(args.command)


if __name__ == "__main__":
    main()
