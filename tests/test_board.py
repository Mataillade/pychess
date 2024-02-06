import pytest

from pychess.board import Cell, ChessBoard
from pychess.colors import Colors
from pychess.coordinates import Coordinates
from pychess.exceptions import CannotMoveError
from pychess.piece import Piece


class FakePiece(Piece):
    def can_move(self, coordinates: Coordinates, target: Coordinates) -> bool:
        return True


class MotionlessPiece(Piece):
    def can_move(self, coordinates: Coordinates, target: Coordinates) -> bool:
        return False


class TestBoard:
    @pytest.fixture(scope="function")
    def board(self) -> ChessBoard:
        return ChessBoard.empty()

    def test_put_with_success(self, board):
        piece = FakePiece(Colors.WHITE)
        coord = Coordinates(4, 4)

        assert board.put(piece, coord) is None

    def test_put_with_coord_outside_board_raise_index_error(self, board):
        piece = FakePiece(Colors.WHITE)
        coord = Coordinates(-100, 100)

        with pytest.raises(IndexError):
            board.put(piece, coord)

    def test_move_with_success(self, board):
        coord = Coordinates(3, 4)
        board.put(FakePiece(Colors.WHITE), coord)
        target = Coordinates(4, 4)

        assert board.move(coord, target) is None

    def test_move_with_empty_cell_raise_cannot_move_error(self, board):
        coord = Coordinates(3, 4)
        target = Coordinates(4, 4)

        with pytest.raises(CannotMoveError):
            board.move(coord, target)

    def test_move_with_piece_cannot_go_here_raise_cannot_move_error(self, board):
        coord = Coordinates(3, 4)
        board.put(MotionlessPiece(Colors.WHITE), coord)
        target = Coordinates(4, 4)

        with pytest.raises(CannotMoveError):
            board.move(coord, target)

    def test_move_with_coord_outside_board_raise_cannot_move_error(self, board):
        coord = Coordinates(3, 4)
        board.put(FakePiece(Colors.WHITE), coord)
        target = Coordinates(-100, 100)

        with pytest.raises(CannotMoveError):
            board.move(coord, target)

    def test_move_with_same_color_raise_cannot_move_error(self, board):
        coord1 = Coordinates(3, 4)
        coord2 = Coordinates(4, 4)
        board.put(FakePiece(Colors.WHITE), coord1)
        board.put(FakePiece(Colors.WHITE), coord2)

        with pytest.raises(CannotMoveError):
            board.move(coord1, coord2)

    def test_move_with_other_color_raise_cannot_move_error(self, board):
        coord1 = Coordinates(3, 4)
        coord2 = Coordinates(4, 4)
        board.put(FakePiece(Colors.WHITE), coord1)
        board.put(FakePiece(Colors.BLACK), coord2)

        assert board.move(coord1, coord2) is None

    def test_empty_with_success_return_board(self):
        board = ChessBoard.empty()
        assert isinstance(board, ChessBoard)
        assert len(board._matrix) == 8

        for row in board._matrix:
            assert len(row) == 8

            for cell in row:
                assert isinstance(cell, Cell)
                assert cell.is_empty
