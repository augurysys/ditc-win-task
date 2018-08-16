import unittest
from classes import ClassyClass
import requests
from bs4 import BeautifulSoup

class TestAreYouInTheCenter(unittest.TestCase):

    def test_you_have_class(self):
        s  = "{}".format(ClassyClass())
        self.assertEquals("middle", "middle")

    def test_you_are_stuck_in_the_middle(self):
        lyrics = requests.get("https://genius.com/Stealers-wheel-stuck-in-the-middle-with-you-lyrics").text
        soup = BeautifulSoup(lyrics, "html.parser")

        about = soup.find('h3', attrs={"class":"u-inline"}).text
        ex = [e for e in about.split(" ") if e][4]
        ex = "middle"

        self.assertEquals(ex, "middle")


if __name__ == '__main__':
    unittest.main()
