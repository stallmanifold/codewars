import collections
from codewars.kyu3.base64_encoding import from_base_64, to_base_64

CaseData = collections.namedtuple('CaseData', 'data expected')

class TestBase64Encoding():

    def __test_cases_to_base64(self):
        test_cases = [
            CaseData("this is a string!!", "dGhpcyBpcyBhIHN0cmluZyEh"),
            CaseData("this is a test!", "dGhpcyBpcyBhIHRlc3Qh"),
            CaseData("now is the time for all good men to come to the aid of their country.","bm93IGlzIHRoZSB0aW1lIGZvciBhbGwgZ29vZCBtZW4gdG8gY29tZSB0byB0aGUgYWlkIG9mIHRoZWlyIGNvdW50cnku"),
            CaseData("1234567890  ", "MTIzNDU2Nzg5MCAg"),
            CaseData("ABCDEFGHIJKLMNOPQRSTUVWXYZ ", "QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVog"),
            CaseData("the quick brown fox jumps over the white fence. ", "dGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSB3aGl0ZSBmZW5jZS4g"),
            CaseData("dGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSB3aGl0ZSBmZW5jZS4", "ZEdobElIRjFhV05ySUdKeWIzZHVJR1p2ZUNCcWRXMXdjeUJ2ZG1WeUlIUm9aU0IzYUdsMFpTQm1aVzVqWlM0"),
            CaseData("VFZSSmVrNUVWVEpPZW1jMVRVTkJaeUFna", "VkZaU1NtVnJOVVZXVkVwUFpXMWpNVlJWVGtKYWVVRm5h"),
            CaseData("TVRJek5EVTJOemc1TUNBZyAg", "VFZSSmVrNUVWVEpPZW1jMVRVTkJaeUFn"),
        ]

        return test_cases

    def __test_cases_from_base64(self):
        test_cases = [
            CaseData("dGhpcyBpcyBhIHN0cmluZyEh", "this is a string!!"),
            CaseData("dGhpcyBpcyBhIHRlc3Qh", "this is a test!"),
            CaseData("bm93IGlzIHRoZSB0aW1lIGZvciBhbGwgZ29vZCBtZW4gdG8gY29tZSB0byB0aGUgYWlkIG9mIHRoZWlyIGNvdW50cnku", "now is the time for all good men to come to the aid of their country."),
            CaseData("MTIzNDU2Nzg5MCAg", "1234567890  "),
            CaseData("QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVog", "ABCDEFGHIJKLMNOPQRSTUVWXYZ "),
            CaseData("dGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSB3aGl0ZSBmZW5jZS4g", "the quick brown fox jumps over the white fence. "),
            CaseData("ZEdobElIRjFhV05ySUdKeWIzZHVJR1p2ZUNCcWRXMXdjeUJ2ZG1WeUlIUm9aU0IzYUdsMFpTQm1aVzVqWlM0", "dGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSB3aGl0ZSBmZW5jZS4"),
            CaseData("VkZaU1NtVnJOVVZXVkVwUFpXMWpNVlJWVGtKYWVVRm5h", "VFZSSmVrNUVWVEpPZW1jMVRVTkJaeUFna"),
            CaseData("VFZSSmVrNUVWVEpPZW1jMVRVTkJaeUFn", "TVRJek5EVTJOemc1TUNBZyAg"),
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
