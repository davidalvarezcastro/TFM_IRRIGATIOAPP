import typing
from abc import ABC, abstractmethod

from domain.models.area_types import AreaType
from exceptions.general import NotImplementedError
from exceptions.database import ExceptionDatabase


class InterfaceAreaTypesDAL(ABC):

    @abstractmethod
    def insert(area: AreaType) -> typing.Tuple[int, ExceptionDatabase]:
        raise NotImplementedError

    @abstractmethod
    def update(area: AreaType) -> ExceptionDatabase:
        raise NotImplementedError

    @abstractmethod
    def delete(area: AreaType) -> ExceptionDatabase:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(type: int) -> AreaType:
        raise NotImplementedError

    @abstractmethod
    def get_all() -> typing.List[AreaType]:
        raise NotImplementedError
