#Unit test

import unittest
import feedparser
from redditfeed import reddit_rss

#Test that function reddit_rss() has a string length of greater than 5,00.
class TestReddit(unittest.TestCase):
    def test_reddit_rss(self):
        a = reddit_rss("https://reddit.com/r/rust.rss")
        self.assertGreater(len(a), 5,000)
