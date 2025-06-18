import praw

reddit = praw.Reddit(
    client_id="jmu7SKmRBHvAoW_zg2eCng",
    client_secret="yBn-8aaXOOSZpriSz4_wP9rpbq7TsA",
    user_agent="MoodMap: AI Reddit sentiment analyzer"
)

def get_posts(subreddit_name):
    try:
        posts = reddit.subreddit(subreddit_name).hot(limit=15)
        return [post.title for post in posts if not post.stickied]
    except Exception as e:
        return [f"Error fetching subreddit: {e}"]