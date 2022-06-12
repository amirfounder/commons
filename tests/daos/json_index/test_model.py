from __future__ import annotations
import uuid
from datetime import datetime
from typing import Optional, TypeVar

from commons.daos.json_index import JsonIndexModel, JsonIndex


class Recruiter(JsonIndexModel):
    name: Optional[str]
    company: Optional[str]
    headline: Optional[str]
    username: Optional[str]
    last_contacted: Optional[datetime]


class Company(JsonIndexModel):
    name: str
    url: str


K = TypeVar('K', bound=str)
V = TypeVar('V', bound=Recruiter)


class Index(JsonIndex[str, Recruiter]):
    pass


def test_index_model_works():
    index = Index()
    preset_uuid = uuid.uuid4()

    index['amir'] = Recruiter(id=preset_uuid, name='Amir')
    index['dior'] = Recruiter(name='Dior')

    j = index.json()
    i = Index.parse_raw(j)

    assert i.source['amir'].id == preset_uuid
    print(i)
