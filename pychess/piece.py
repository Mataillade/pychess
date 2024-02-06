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
        return (
            abs(coordinates.x - target.x) <= 1
            and abs(coordinates.y - target.y) <= 1
            and coordinates != target
        )


class Queen(Piece):
    def can_move(self, coordinates: Coordinates, target: Coordinates) -> bool:
        return (
            coordinates.x == target.x
            or coordinates.y == target.y
            or abs(coordinates.x - target.x) == abs(coordinates.y - target.y)
        ) and coordinates != target


class Rooks(Piece):
    def can_move(self, coordinates: Coordinates, target: Coordinates) -> bool:
        return (
            coordinates.x == target.x or coordinates.y == target.y
        ) and coordinates != target


class Bishop(Piece):
    def can_move(self, coordinates: Coordinates, target: Coordinates) -> bool:
        return (
            abs(coordinates.x - target.x) == abs(coordinates.y - target.y)
            and coordinates != target
        )


class Knight(Piece):
    def can_move(self, coordinates: Coordinates, target: Coordinates) -> bool:
        return (
            (abs(coordinates.x - target.x) == 2 and abs(coordinates.y - target.y) == 1)
            or (
                abs(coordinates.x - target.x) == 1
                and abs(coordinates.y - target.y) == 2
            )
        ) and coordinates != target


class Pawn(Piece):
    def can_move(self, coordinates: Coordinates, target: Coordinates) -> bool:
        if coordinates != target:
            if (
                self.color == Colors.WHITE
                and coordinates.x == target.x
                and target.y - coordinates.y == 1
            ):
                return True
            if (
                self.color == Colors.BLACK
                and coordinates.x == target.x
                and target.y - coordinates.y == -1
            ):
                return True
        return False
