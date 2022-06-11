from abc import ABC

from pydantic import BaseModel

from .model import AbstractJsonModel


class AbstractJsonIndex(BaseModel, ABC):
    source: dict[str, AbstractJsonModel] = {}

    def __contains__(self, item):
        return item in self.source

    def __getitem__(self, item):
        return self.source[item]

    def __setitem__(self, key, value):
        self.source[key] = value

    def get(self, key, default=None):
        return self.source.get(key, default)