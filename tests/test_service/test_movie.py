import pytest

from service.movie import MovieService

class TestMovieService:

    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert movies is not None
        assert len(movies) > 0

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie is not None
        assert movie.id is not None
        assert movie.title == "Movie 1"

    def test_create(self):
        movie_dict = {
            "title": "Movie 4",
            "description": "Des 1",
            "trailer": "Link 1",
            "year": 1000,
            "rating": 10.0,
            "genre_id": 1,
            "director_id": 1
        }

        movie = self.movie_service.create(movie_dict)

        assert movie.id is not None
        assert movie.description is not None
        assert movie.trailer is not None
        assert movie.year is not None
        assert movie.rating is not None
        assert movie.genre_id is not None
        assert movie.director_id is not None

    def test_update(self):
        movie_dict = {
            "id": 3,
            "title": "Movie Three",
            "description": "Des 1",
            "trailer": "Link 1",
            "year": 1000,
            "rating": 10.0,
            "genre_id": 1,
            "director_id": 1
        }

        assert self.movie_service.update(movie_dict)

    def test_delete(self):
        assert self.movie_service.delete(1) is None
