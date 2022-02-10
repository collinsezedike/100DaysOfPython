facebook_posts = [
    {"Likes":21, "Comment":2},
    {"Likes":13, "Comment":2, "Shares":1},
    {"Likes":33, "Comment":8, "Shares":3},
    {"Comment":4, "Shares":2},
    {"Comment":1, "Shares":1},
    {"Likes":19, "Comment":3},
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post["Likes"]
    except KeyError:
        pass

print(total_likes)