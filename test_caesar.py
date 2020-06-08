import unittest

from caesar import cipher


class CipherTestCase(unittest.TestCase):

    def test_coding_type(self):

        result = cipher("e", "Aa. Bb!", 1)
        self.assertEqual(result, "Bb. Cc!")

        result = cipher("e", "Aa. Bb!", 10)
        self.assertEqual(result, "Kk. Ll!")

        result = cipher("d", "Aa. Bb!", 1)
        self.assertEqual(result, "Zz. Aa!")

        result = cipher("d", "Aa. Bb!", 10)
        self.assertEqual(result, "Qq. Rr!")

        result = cipher("", "Aa. Bb!", 10)
        self.assertEqual(result, "Function expects either command '-e' to encode or '-d' to decode")

        result = cipher(0, "Aa. Bb!", 10)
        self.assertEqual(result, "Function expects either command '-e' to encode or '-d' to decode")

        result = cipher(-1, "Aa. Bb!", 10)
        self.assertEqual(result, "Function expects either command '-e' to encode or '-d' to decode")

        result = cipher(0.532254654332, "Aa. Bb!", 10)
        self.assertEqual(result, "Function expects either command '-e' to encode or '-d' to decode")

        result = cipher("A string", "Aa. Bb!", 10)
        self.assertEqual(result, "Function expects either command '-e' to encode or '-d' to decode")

        result = cipher(False, "Aa. Bb!", 10)
        self.assertEqual(result, "Function expects either command '-e' to encode or '-d' to decode")

        result = cipher(True, "Aa. Bb!", 10)
        self.assertEqual(result, "Function expects either command '-e' to encode or '-d' to decode")

    def test_user_key(self):

        result = cipher("e", "Aa. Bb!", 0)
        self.assertEqual(result, "user key must be an integer between 1 and 25")

        result = cipher("e", "Aa. Bb!", -1)
        self.assertEqual(result, "user key must be an integer between 1 and 25")

        result = cipher("e", "Aa. Bb!", 0.532254654332)
        self.assertEqual(result, "user key must be an integer between 1 and 25")

        result = cipher("e", "Aa. Bb!", 26)
        self.assertEqual(result, "user key must be an integer between 1 and 25")

        result = cipher("e", "Aa. Bb!", 2643254645865734532453264357533643513243543635748768745353242143234532566547456)
        self.assertEqual(result, "user key must be an integer between 1 and 25")

        result = cipher("e", "Aa. Bb!", "A string")
        self.assertEqual(result, "user key must be an integer between 1 and 25")

        result = cipher("e", "Aa. Bb!", "")
        self.assertEqual(result, "user key must be an integer between 1 and 25")

        result = cipher("e", "Aa. Bb!", False)
        self.assertEqual(result, "user key must be an integer between 1 and 25")

        result = cipher("e", "Aa. Bb!", True)
        self.assertEqual(result, "user key must be an integer between 1 and 25")

        result = cipher("d", "Aa. Bb!", 0)
        self.assertEqual(result, "user key must be an integer between 1 and 25")

        result = cipher("d", "Aa. Bb!", -1)
        self.assertEqual(result, "user key must be an integer between 1 and 25")

        result = cipher("d", "Aa. Bb!", 0.532254654332)
        self.assertEqual(result, "user key must be an integer between 1 and 25")

        result = cipher("d", "Aa. Bb!", 26)
        self.assertEqual(result, "user key must be an integer between 1 and 25")

        result = cipher("d", "Aa. Bb!", 2643254645865734532453264357533643513243543635748768745353242143234532566547456)
        self.assertEqual(result, "user key must be an integer between 1 and 25")

        result = cipher("d", "Aa. Bb!", "A string")
        self.assertEqual(result, "user key must be an integer between 1 and 25")

        result = cipher("d", "Aa. Bb!", "")
        self.assertEqual(result, "user key must be an integer between 1 and 25")

        result = cipher("d", "Aa. Bb!", False)
        self.assertEqual(result, "user key must be an integer between 1 and 25")

        result = cipher("d", "Aa. Bb!", True)
        self.assertEqual(result, "user key must be an integer between 1 and 25")

