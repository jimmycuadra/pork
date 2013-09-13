from pork.cli import CLI

from mock import Mock

class TestCLI:
    def it_has_a_data_attribute(self):
        assert CLI().data is not None
