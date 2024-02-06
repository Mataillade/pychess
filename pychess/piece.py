from abc import ABC, abstractmethod

from pychess.colors import Colors
from pychess.coordinates import Coordinates


class Piece(ABC):
    def __init__(self, color: Colors):
        self.color = color

    @abstractmethod
    def can_move(self, coordinates: Coordinates, target: Coordinates) -> bool:
        raise NotImplementedError
