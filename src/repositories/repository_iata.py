import abc
from typing import List, Tuple

import pandas as pd

from src.models.model import Airport


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def fetch_airports(self):
        raise NotImplementedError

    def fetch_airport(self, source):
        raise NotImplementedError


class FakeRepository(AbstractRepository):
    def __init__(self, airports: List[Airport]):
        self.airports = airports

    def fetch_airports(self) -> Tuple[Airport, ...]:
        return tuple(self.airports)

    def fetch_airport(self, iata_code: str):
        return next(airport for airport in self.airports if airport.code == iata_code)


class IataRepository(AbstractRepository):

    def fetch_airports(self) -> Tuple[dict, ...]:
        with open('resources/iata.csv') as csv_file:
            df = pd.read_csv(csv_file)

            dict_list = df.to_dict('records')
            dict_tuple = tuple(dict_list)

            return dict_tuple

    def fetch_airport(self, iata_code):
        with open('resources/iata.csv') as csv_file:
            df = pd.read_csv(csv_file)

            dict_list = df.to_dict('records')
            dict_tuple = tuple(dict_list)

            return next(airport for airport in dict_tuple if airport['code'] == iata_code)
