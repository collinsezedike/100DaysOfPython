import requests


class Post:
    def __init__(self):
        response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
        self.posts = response.json()

    def get_all_posts(self):
        return self.posts

    def get_post_by_id(self, post_id):
        for post in self.posts:
            if post["id"] == post_id:
                return post
