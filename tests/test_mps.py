import unittest


rss_feed_url = 'http://www.parliament.nz/en-nz/syndication?posting=/en-nz/mpp/mps/current/'

class TestMPs(unittest.TestCase):
  def test_rss_responds(self):
    import requests
    response = requests.get(rss_feed_url)
    assert response.ok

  def test_num_mps(self):
    import feedparser
    response = feedparser.parse(rss_feed_url)
    assert len(response['entries']) == 121
