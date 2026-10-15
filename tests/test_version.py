import unittest

import sandbox


class VersionTest(unittest.TestCase):
    def test_the_package_has_a_version(self) -> None:
        self.assertRegex(sandbox.__version__, r"^\d+\.\d+\.\d+$")


if __name__ == "__main__":
    unittest.main()
