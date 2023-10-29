"""Main entry point into metronome"""

from application import Application


def main():
    """Main function of script"""

    # Instantiate the application
    app = Application()

    # Do the thing
    app.run()


if __name__ == "__main__":
    main()
