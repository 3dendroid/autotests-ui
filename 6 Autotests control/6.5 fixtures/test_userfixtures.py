import pytest


@pytest.fixture
def clear_book_database() -> None:
    print("[FIXTURE] deleting all data")


@pytest.fixture
def fill_book_database() -> None:
    print("[FIXTURE] creating new data")


@pytest.mark.usefixtures('fill_book_database')
def test_read_all_books_in_library(clear_book_database, fill_book_database):
    print("Reading all books")


@pytest.mark.usefixtures(
    'clear_book_database',
    'fill_book_database')
class TestLibrary:
    def test_read_book_from_library(self):
        pass

    def test_delete_book_from_library(self):
        pass
