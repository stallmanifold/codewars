from codewars.kyu6.in_array import in_array


class TestInArray():

    def test_in_array(self):
        array1   = ["live", "arp", "strong"] 
        array2   = ["lively", "alive", "harp", "sharp", "armstrong"]
        expected = ['arp', 'live', 'strong']
        result   = in_array(array1, array2)

        assert result == expected
