from pork.cli import CLI, main

from mock import Mock, patch
from StringIO import StringIO

patch.TEST_PREFIX = 'it'

@patch('pork.cli.Data')
class TestCLI:
    def it_has_a_data_attribute(self, Data):
        assert CLI().data is not None

    def it_sets_keys(self, Data):
        cli = CLI()
        cli.start(['foo', 'bar'])
        Data.return_value.set.assert_called_with('foo', 'bar')

    def it_gets_keys(self, Data):
        cli = CLI()
        cli.start(['foo'])
        Data.return_value.get.assert_called_with('foo')

    def it_deletes_keys(self, Data):
        cli = CLI()
        cli.start(['-d', 'foo'])
        Data.return_value.delete.assert_called_with('foo')

    @patch('sys.stdout', new_callable=StringIO)
    def it_prints_help_when_there_is_no_data(self, stdout, Data):
        Data.return_value.is_empty.return_value = True
        cli = CLI()
        cli.start([])
        assert "Usage:" in stdout.getvalue()

    @patch('sys.stdout', new_callable=StringIO)
    def it_lists_all_keys_when_there_is_data(self, stdout, Data):
        Data.return_value.is_empty.return_value = False
        Data.return_value.list.return_value = { 'foo': 'bar', 'asdf': 'fdsa'}
        cli = CLI()
        cli.start([])
        assert ' foo: bar\nasdf: fdsa\n' == stdout.getvalue()

@patch('pork.cli.CLI')
class TestMain:
    def it_calls_start_on_a_new_CLI_object(self, CLI):
        main()
        CLI.return_value.start.assert_called()
