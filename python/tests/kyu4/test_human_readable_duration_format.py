from codewars.kyu4.human_readable_duration_format import format_duration


class TestHumanReadableDurationFormat():

    def test_human_readable_duration_format(self):
        assert format_duration(1)    == '1 second'
        assert format_duration(62)   == '1 minute and 2 seconds'
        assert format_duration(120)  == '2 minutes'
        assert format_duration(3600) == '1 hour'
        assert format_duration(3662) == '1 hour, 1 minute and 2 seconds'
