"""Classes for settings/config retention"""

class MetronomeConfig:
    """Class for the settings/config of a single metronome"""

    def __init__(self, name):

        self.config = {
            "Name": name
        }

    def get_name(self):
        """Access to Name setting"""

        return self.config["Name"]

    def set_name(self, new_name):
        """Set Name"""

        self.config["Name"] = new_name

    def get_config(self):
        """Return the setting dictionary"""

        return self.config
