from config import CLIENT_ID, CLIENT_SECRET, USER_AGENT
from reddit_miner.reddit_crawler import RedditCrawler


def main():
    crawler = RedditCrawler(CLIENT_ID, CLIENT_SECRET, USER_AGENT)

    ev_keywords = [
        "ev", "evs"
    ]

    subreddit_list = [
        "melbourne"
    ]

    csv_path = "ev_comments.csv"

    for subreddit_name in subreddit_list:
        print(f"🔍 Crawling subreddit: {subreddit_name}")

        for kw in ev_keywords:
            crawler.search_and_scrape_comments(
                subreddit_name=subreddit_name,
                query=kw,
                csv_path=csv_path,
                limit=50
            )

if __name__ == "__main__":
    main()
