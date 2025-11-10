import praw
import csv
from datetime import datetime
from praw.models import Comment

class RedditCrawler:
    def __init__(self, client_id, client_secret, user_agent):
        self.reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent
        )

    def _convert_timestamp(self, timestamp):
        return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

    def search_and_scrape_comments(self, subreddit_name, query, csv_path="comments.csv", limit=20):
        subreddit = self.reddit.subreddit(subreddit_name)
        posts = subreddit.search(query, sort="relevance", limit=limit)
        with open(csv_path, mode="a", encoding="utf-8", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([
                "post_id", 
                "post_title", 
                "post_created_time",
                "comment_id", 
                "comment_body", 
                "comment_author",
                "comment_created_time"
            ])
            for post in posts:
                post.comments.replace_more(limit=None)
                post_created_time = self._convert_timestamp(post.created_utc)
                for comment in post.comments.list():
                    if isinstance(comment, Comment):
                        comment_created_time = self._convert_timestamp(comment.created_utc)
                        writer.writerow([
                            post.id,
                            post.title,
                            post_created_time,
                            comment.id,
                            comment.body,
                            str(comment.author),
                            comment_created_time
                        ])
