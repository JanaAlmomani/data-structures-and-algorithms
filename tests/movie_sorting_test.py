from sorting.sort_movies import*
import pytest

@pytest.fixture
def movies():
    return [
        {'title': 'Movie 1', 'year': 2022, 'genres': ['Genre 1', 'Genre 2']},
        {'title': 'Movie 2', 'year': 2021, 'genres': ['Genre 2', 'Genre 3']},
        {'title': 'Movie 3', 'year': 2023, 'genres': ['Genre 1', 'Genre 3']}
    ]

def test_sort_by_year(movies):
    sorted_movies = sort_by_year(movies)
    assert sorted_movies == [
        {'title': 'Movie 3', 'year': 2023, 'genres': ['Genre 1', 'Genre 3']},
        {'title': 'Movie 1', 'year': 2022, 'genres': ['Genre 1', 'Genre 2']},
        {'title': 'Movie 2', 'year': 2021, 'genres': ['Genre 2', 'Genre 3']}
    ]

def test_sort_by_title(movies):
    sorted_movies = sort_by_title(movies)
    assert sorted_movies == [
        {'title': 'Movie 1', 'year': 2022, 'genres': ['Genre 1', 'Genre 2']},
        {'title': 'Movie 2', 'year': 2021, 'genres': ['Genre 2', 'Genre 3']},
        {'title': 'Movie 3', 'year': 2023, 'genres': ['Genre 1', 'Genre 3']}
    ]
