from dataclasses import dataclass

from pychess.colors import Colors
from pychess.coordinates import Coordinates
from pychess.piece import King, Piece, Queen, Rooks, Bishop, Knight


@dataclass
class Move:
    position: Coordinates
    target: Coordinates


def assert_can_move(move_list: list[Move], expected: bool, piece: Piece):
    for move in move_list:
        assert piece.can_move(move.position, move.target) is expected


class TestKing:
    king = King(Colors.WHITE)

    def test_can_move_with_success_return_bool(self):
        king_can_move = [
            Move(Coordinates(4, 4), Coordinates(4, 5)),
            Move(Coordinates(4, 4), Coordinates(5, 5)),
            Move(Coordinates(4, 4), Coordinates(5, 4)),
        ]
        assert_can_move(king_can_move, True, self.king)

        king_cant_move = [
            Move(Coordinates(4, 4), Coordinates(5, 10)),
            Move(Coordinates(4, 4), Coordinates(4, 4)),
        ]
        assert_can_move(king_cant_move, False, self.king)


class TestQueen:
    queen = Queen(Colors.WHITE)

    def test_can_move_with_success_return_bool(self):
        queen_can_move = [
            Move(Coordinates(4, 4), Coordinates(4, 5)),
            Move(Coordinates(4, 4), Coordinates(5, 5)),
            Move(Coordinates(4, 4), Coordinates(5, 4)),
            Move(Coordinates(4, 4), Coordinates(4, 8)),
            Move(Coordinates(4, 4), Coordinates(8, 4)),
            Move(Coordinates(4, 4), Coordinates(1, 1)),
        ]
        assert_can_move(queen_can_move, True, self.queen)

        queen_cant_move = [
            Move(Coordinates(4, 4), Coordinates(5, 10)),
            Move(Coordinates(4, 4), Coordinates(4, 4)),
        ]
        assert_can_move(queen_cant_move, False, self.queen)


class TestRooks:
    rooks = Rooks(Colors.WHITE)

    def test_can_move_with_success_return_bool(self):
        rooks_can_move = [
            Move(Coordinates(4, 4), Coordinates(4, 5)),
            Move(Coordinates(4, 4), Coordinates(5, 4)),
            Move(Coordinates(4, 4), Coordinates(4, 8)),
            Move(Coordinates(4, 4), Coordinates(8, 4)),
        ]
        assert_can_move(rooks_can_move, True, self.rooks)

        rooks_cant_move = [
            Move(Coordinates(4, 4), Coordinates(5, 10)),
            Move(Coordinates(4, 4), Coordinates(4, 4)),
        ]
        assert_can_move(rooks_cant_move, False, self.rooks)


class TestBishop:
    bishop = Bishop(Colors.WHITE)

    def test_can_move_with_success_return_bool(self):
        bishop_can_move = [
            Move(Coordinates(4, 4), Coordinates(5, 5)),
            Move(Coordinates(4, 4), Coordinates(1, 1)),
        ]
        assert_can_move(bishop_can_move, True, self.bishop)

        bishop_cant_move = [
            Move(Coordinates(4, 4), Coordinates(4, 5)),
            Move(Coordinates(4, 4), Coordinates(5, 10)),
            Move(Coordinates(4, 4), Coordinates(4, 4)),
        ]
        assert_can_move(bishop_cant_move, False, self.bishop)


class TestKnight:
    knight = Knight(Colors.WHITE)

    def test_can_move_with_success_return_bool(self):
        knight_can_move = [
            Move(Coordinates(4, 4), Coordinates(6, 5)),
            Move(Coordinates(4, 4), Coordinates(2, 5)),
            Move(Coordinates(4, 4), Coordinates(5, 6)),
            Move(Coordinates(4, 4), Coordinates(3, 6)),
        ]
        assert_can_move(knight_can_move, True, self.knight)

        knight_cant_move = [
            Move(Coordinates(4, 4), Coordinates(4, 5)),
            Move(Coordinates(4, 4), Coordinates(5, 10)),
            Move(Coordinates(4, 4), Coordinates(4, 4)),
        ]
        assert_can_move(knight_cant_move, False, self.knight)


class TestPawn:
    pawn = Knight(Colors.WHITE)

    def test_can_move_with_success_return_bool(self):
        pawn_can_move = [
            Move(Coordinates(4, 4), Coordinates(4, 5)),
            Move(Coordinates(4, 4), Coordinates(3, 5)),
        ]
        assert_can_move(pawn_can_move, True, self.pawn)

        pawn_cant_move = [
            Move(Coordinates(4, 4), Coordinates(5, 10)),
            Move(Coordinates(4, 4), Coordinates(4, 4)),
        ]
        assert_can_move(pawn_cant_move, False, self.pawn)
