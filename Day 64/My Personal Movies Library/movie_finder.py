import requests


class MovieFinder:
    def __init__(self):
        self.api_key = "aad562bd609e217e5641cd2bd722bc75"

    def search_for_movie(self, movie):
        endpoint = "https://api.themoviedb.org/3/search/movie"
        params = {
            "api_key": self.api_key,
            "query": movie,
        }
        response = requests.get(endpoint, params=params)
        data = response.json()["results"]
        return data

    def get_movie_data(self, movie_id):
        endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
        params = {
            "api_key": self.api_key,
            "movie_id": movie_id,
        }
        response = requests.get(endpoint, params=params)
        data = response.json()
        return data
