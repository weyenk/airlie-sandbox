import unittest
from sandbox.text import slugify

class SlugifyTest(unittest.TestCase):
    def test_slugify_mixed_case(self):
        """Given a title with mixed case, when slugify is called, then every alphabetic character is lowercased."""
        self.assertEqual(slugify("Hello"), "hello")
        self.assertEqual(slugify("HELLO"), "hello")
        self.assertEqual(slugify("HelloWorld"), "helloworld")

    def test_slugify_accented_characters(self):
        """Given a title containing accented letters, when slugify is called, then each accented letter becomes its unaccented equivalent."""
        self.assertEqual(slugify("Café"), "cafe")
        self.assertEqual(slugify("Wörld"), "world")
        self.assertEqual(slugify("naïve"), "naive")
        self.assertEqual(slugify("résumé"), "resume")

    def test_slugify_punctuation_and_spaces(self):
        """Given a title containing spaces, punctuation, or other non-alphanumeric characters, when slugify is called, then each run of such characters becomes a single dash."""
        self.assertEqual(slugify("  Hello, Wörld!  "), "hello-world")
        self.assertEqual(slugify("Hello   World"), "hello-world")
        self.assertEqual(slugify("Hello-World"), "hello-world")
        self.assertEqual(slugify("Hello_World"), "hello-world")

    def test_slugify_leading_trailing_dash(self):
        """Given a title that begins or ends with a non-alphanumeric character, when slugify is called, then the result has no leading or trailing dash."""
        self.assertEqual(slugify("  Hello World"), "hello-world")
        self.assertEqual(slugify("Hello World   "), "hello-world")
        self.assertEqual(slugify("-Hello World"), "hello-world")
        self.assertEqual(slugify("Hello World-"), "hello-world")

    def test_slugify_empty_string(self):
        """Given an empty title, when slugify is called, then it returns an empty string."""
        self.assertEqual(slugify(""), "")
        self.assertEqual(slugify("   "), "")

if __name__ == "__main__":
    unittest.main()