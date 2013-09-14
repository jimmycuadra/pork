from pork.data import Data

from mock import Mock, patch, mock_open
from StringIO import StringIO

patch.TEST_PREFIX = 'it'

class TestData:
    def it_loads_json_data_from_file(self):
        with patch("__builtin__.open", mock_open(read_data='{"foo":"bar"}'),
            create=True) as m:
            data = Data()
            assert data.get('foo') == 'bar'

    def it_sets_and_gets_keys(self):
        data = Data()
        data.set('foo', 'bar')
        assert data.get('foo') == 'bar'

    def it_deletes_existing_keys(self):
        data = Data()
        data.set('foo', 'bar')
        data.delete('foo')
        assert data.get('foo') is None

    def it_is_empty_if_there_are_no_keys(self):
        data = Data()
        assert data.is_empty()

    def it_returns_the_data_dict(self):
        data = Data()
        data.set('foo', 'bar')
        assert data.list() == { 'foo': 'bar' }

    def it_fails_silently_if_it_cannot_save(self):
        data = Data()
        with patch("__builtin__.open", side_effect=ValueError):
            data.set('foo', 'bar')
        assert True
