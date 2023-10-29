"""Classes for settings/config retention"""


class MetronomeConfig:
    """Class for the settings/config of a single metronome"""

    def __init__(self, name, bpm):

        self.config = {
            "Name": name,
            "BPM": bpm
        }

    def get_name(self):
        """Access to Name setting"""

        return self.config["Name"]

    def set_name(self, new_name):
        """Set Name"""

        self.config["Name"] = new_name

    def get_bpm(self):
        """Access to bpm"""

        return self.config["BPM"]

    def set_bpm(self, new_bpm):
        """Set Name"""

        self.config["BPM"] = new_bpm

    def get_config(self):
        """Return the setting dictionary"""

        return self.config


class MetronomeConfigs:
    """Manager of the settings file content"""

    def __init__(self):

        self.configs = []

    def add_config(self, config: MetronomeConfig):
        """Append a new config"""

        self.configs.append(config.get_config())

    def get_configs(self):
        """Return the configs list"""

        return self.configs
