from dataclasses import dataclass, field
from typing import ClassVar, Self

from pychess.coordinates import Coordinates
from pychess.exceptions import CannotMoveError
from pychess.piece import Piece


@dataclass(slots=True)
class Cell:
    piece: Piece | None = field(default=None)

    @property
    def is_empty(self) -> bool:
        return self.piece is None


@dataclass(frozen=True, slots=True)
class ChessBoard:
    _matrix: tuple[tuple[Cell, ...], ...]

    LENGTH: ClassVar[int] = 8

    def move(self, piece_coordinates: Coordinates, target: Coordinates):
        cell = self.__get_cell(piece_coordinates)

        if cell.piece is None:
            raise CannotMoveError("No piece here.")

        if not self.__in_board(*target):
            raise CannotMoveError("Invalid coordinates.")

        target_cell = self.__get_cell(target)

        if target_cell.piece is not None:
            if cell.piece.color == target_cell.piece.color:
                raise CannotMoveError("Cell occupied.")

        if not cell.piece.can_move(piece_coordinates, target):
            raise CannotMoveError("This piece can't go here.")

        cell.piece, target_cell.piece = None, cell.piece

    def put(self, piece: Piece, coordinates: Coordinates):
        self.__get_cell(coordinates).piece = piece

    def __get_cell(self, coordinates: Coordinates) -> Cell:
        return self._matrix[coordinates.x][coordinates.y]

    @classmethod
    def empty(cls) -> Self:
        matrix = tuple(
            tuple(Cell() for _ in range(cls.LENGTH)) for _ in range(cls.LENGTH)
        )
        return cls(matrix)

    @classmethod
    def __in_board(cls, *values: int) -> bool:
        for value in values:
            if 0 < value < cls.LENGTH:
                continue

            return False

        return True
