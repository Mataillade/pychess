from abc import ABC, abstractmethod

from pychess.colors import Colors
from pychess.coordinates import Coordinates


class Piece(ABC):
    def __init__(self, color: Colors):
        self.color = color

    @abstractmethod
    def can_move(self, coordinates: Coordinates, target: Coordinates) -> bool:
        raise NotImplementedError


class King(Piece):
    def can_move(self, coordinates: Coordinates, target: Coordinates) -> bool:
        pass


class Queen(Piece):
    def can_move(self, coordinates: Coordinates, target: Coordinates) -> bool:
        pass


class Rooks(Piece):
    def can_move(self, coordinates: Coordinates, target: Coordinates) -> bool:
        pass


class Bishop(Piece):
    def can_move(self, coordinates: Coordinates, target: Coordinates) -> bool:
        pass


class Knight(Piece):
    def can_move(self, coordinates: Coordinates, target: Coordinates) -> bool:
        pass


class Pawn(Piece):
    def can_move(self, coordinates: Coordinates, target: Coordinates) -> bool:
        pass
