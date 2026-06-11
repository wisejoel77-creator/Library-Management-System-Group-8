import pytest
from MODELS.book import Book

#Test case that raises an error when author is empty
def test_empty_author_raises_error():
    with pytest.raises(ValueError):
        Book("1984", "", "Dystopian")

#Test case that raises an error when genre is empty
def test_empty_genre_raises_error():
    with pytest.raises(ValueError):
        Book("1984", "George Orwell", "")