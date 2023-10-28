"""Testbed for application"""


def test_method():
    """A test method to validate that the CLI is working"""

    print("Test Method Executed")


def do_help(valid_commands):
    """Output all our commands"""

    for command in valid_commands:
        print(f"{command[0]} :      {command[1]}")

    print("----")
    print("Help :    Print this list")
    print("Exit :    Terminate")


def main():
    """Main method of script"""

    while True:

        valid_commands = []
        valid_commands.append(["Test", "Run the test_method()", test_method])

        # Get and parse the commands
        instruction = input("Command: ")
        instructions = instruction.split(" ")

        # Have to enter something
        if len(instructions) == 0:
            continue

        # Should we exit?
        command = instructions[0].lower()
        if command == "exit":
            break

        # Print out the help menu
        if command == "help":
            do_help(valid_commands)
            continue

        for command_option in valid_commands:

            if command_option[0].lower() == command:
                command_option[2]()


if __name__ == "__main__":
    main()
