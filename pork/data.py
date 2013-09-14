import json
import os


class Data:
    _data_path = os.path.join(os.environ['HOME'], '.pork')

    def __init__(self):
        try:
            with open(self._data_path) as f:
                self._data = json.load(f)
        except (IOError, ValueError):
            self._data = {}

    def get(self, key):
        if key in self._data:
            return self._data[key]

    def set(self, key, value):
        self._data[key] = value
        self._save()

    def delete(self, key):
        del self._data[key]
        self._save()

    def is_empty(self):
        return len(self._data) == 0

    def list(self):
        return self._data

    def _save(self):
        try:
            with open(self._data_path, 'w') as f:
                json.dump(self._data, f)
        except ValueError:
            pass
