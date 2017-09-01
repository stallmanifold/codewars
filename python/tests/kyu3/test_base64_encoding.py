import collections
from codewars.kyu3.base64_encoding import from_base_64, to_base_64

TestCase = collections.namedtuple('TestCase', 'data expected')

class TestBase64Encoding():

    def __test_cases_to_base64(self):
        test_cases = [
            TestCase("this is a string!!", "dGhpcyBpcyBhIHN0cmluZyEh"),
            TestCase("this is a test!", "dGhpcyBpcyBhIHRlc3Qh"),
            TestCase("now is the time for all good men to come to the aid of their country.","bm93IGlzIHRoZSB0aW1lIGZvciBhbGwgZ29vZCBtZW4gdG8gY29tZSB0byB0aGUgYWlkIG9mIHRoZWlyIGNvdW50cnku"),
            TestCase("1234567890  ", "MTIzNDU2Nzg5MCAg"),
            TestCase("ABCDEFGHIJKLMNOPQRSTUVWXYZ ", "QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVog"),
            TestCase("the quick brown fox jumps over the white fence. ", "dGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSB3aGl0ZSBmZW5jZS4g"),
            TestCase("dGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSB3aGl0ZSBmZW5jZS4", "ZEdobElIRjFhV05ySUdKeWIzZHVJR1p2ZUNCcWRXMXdjeUJ2ZG1WeUlIUm9aU0IzYUdsMFpTQm1aVzVqWlM0"),
            TestCase("VFZSSmVrNUVWVEpPZW1jMVRVTkJaeUFna", "VkZaU1NtVnJOVVZXVkVwUFpXMWpNVlJWVGtKYWVVRm5h"),
            TestCase("TVRJek5EVTJOemc1TUNBZyAg", "VFZSSmVrNUVWVEpPZW1jMVRVTkJaeUFn"),
        ]

        return test_cases

    def __test_cases_from_base64(self):
        test_cases = [
            TestCase("dGhpcyBpcyBhIHN0cmluZyEh", "this is a string!!"),
            TestCase("dGhpcyBpcyBhIHRlc3Qh", "this is a test!"),
            TestCase("bm93IGlzIHRoZSB0aW1lIGZvciBhbGwgZ29vZCBtZW4gdG8gY29tZSB0byB0aGUgYWlkIG9mIHRoZWlyIGNvdW50cnku", "now is the time for all good men to come to the aid of their country."),
            TestCase("MTIzNDU2Nzg5MCAg", "1234567890  "),
            TestCase("QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVog", "ABCDEFGHIJKLMNOPQRSTUVWXYZ "),
            TestCase("dGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSB3aGl0ZSBmZW5jZS4g", "the quick brown fox jumps over the white fence. "),
            TestCase("ZEdobElIRjFhV05ySUdKeWIzZHVJR1p2ZUNCcWRXMXdjeUJ2ZG1WeUlIUm9aU0IzYUdsMFpTQm1aVzVqWlM0", "dGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSB3aGl0ZSBmZW5jZS4"),
            TestCase("VkZaU1NtVnJOVVZXVkVwUFpXMWpNVlJWVGtKYWVVRm5h", "VFZSSmVrNUVWVEpPZW1jMVRVTkJaeUFna"),
            TestCase("VFZSSmVrNUVWVEpPZW1jMVRVTkJaeUFn", "TVRJek5EVTJOemc1TUNBZyAg"),
        ]

        return test_cases


    def test_to_base64(self):
        test = self.__test_cases_to_base64()
        for test_case in test:
            result = to_base_64(test_case.data)
            expected = test_case.expected

            assert result == expected

    def test_from_base64(self):
        test = self.__test_cases_from_base64()
        for test_case in test:
            result = from_base_64(test_case.data)
            expected = test_case.expected

            assert result == expected

    def test_to_base64_should_be_invertible(self):
        test = self. __test_cases_to_base64()
        for test_case in test:
            result = from_base_64(to_base_64(test_case.data))
            expected = test_case.data

            assert result == expected

    def test_to_base64_should_be_invertible(self):
        test = self. __test_cases_from_base64()
        for test_case in test:
            result = to_base_64(from_base_64(test_case.data))
            expected = test_case.data

            assert result == expected
