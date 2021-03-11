

import unittest
import datetime as dt


class TestEvent(unittest.TestCase):
    end_day = start_night = dt.datetime(2021, 3, 5, 20, 0, 0)
    start_day = end_night = dt.datetime(2021, 3, 5, 6, 0, 0)

    def test_event_during_day(self):

        start_event = dt.datetime(2021, 3, 5, 8, 0, 0)
        end_event = dt.datetime(2021, 3, 5, 14, 0, 0)

        self.assertGreater(end_event, start_event, "the event is correct")
        self.assertEqual(start_event.date(), end_event.date(), "the event is during the same day")
        self.assertGreaterEqual(start_event, self.start_day, "the event starts after 6am")
        self.assertGreaterEqual(self.end_day, end_event, "the event ends before 10pm")

    def test_event_during_night(self):
        start_event = dt.datetime(2021, 3, 5, 23, 0, 0)
        end_event = dt.datetime(2021, 3, 6, 5, 0, 0)

        self.assertGreater(end_event, start_event, "the event is correct")
        self.assertNotEqual(start_event.date(), end_event.date(), "the event is during the same night")
        self.assertGreaterEqual(start_event, self.start_night, "the event starts after 10pm")
        self.assertGreaterEqual(end_event, self.end_night, "the event ends before 6am")


    def test_event_start_day_end_night(self):
        start_event = dt.datetime(2021, 3, 6, 10, 0, 0)
        end_event = dt.datetime(2021, 3, 6, 23, 0, 0)

        self.assertGreater(end_event, start_event, "the event is correct")
        self.assertGreaterEqual(start_event, self.start_day, "the event starts after 6am")
        self.assertGreaterEqual(end_event, self.start_night, "the event ends after 10pm")

    def test_event_start_night_end_day(self):
        start_event = dt.datetime(2021, 3, 6, 23, 0, 0)
        end_event = dt.datetime(2021, 3, 7, 10, 0, 0)

        self.assertGreater(end_event, start_event, "the event is correct")
        self.assertGreaterEqual(start_event, self.start_night, "the event starts after 10pm (at night)")
        self.assertGreaterEqual(end_event, self.start_day, "the event ends after 6am")


    def test_event_start_day_continues_night_ends_day(self):
        start_event = dt.datetime(2021, 3, 5, 12, 0, 0)
        end_event = dt.datetime(2021, 3, 6, 12, 0, 0)

        self.assertGreater(end_event, start_event, "the event is correct")
        self.assertNotEqual(start_event.date(), end_event.date(), "the event is not the same date")
        self.assertGreaterEqual(start_event, self.start_day, "the event starts after 10pm (at night)")
        self.assertGreaterEqual(end_event, self.start_day, "the event ends after 6am")

    def test_event_start_night_continues_day_ends_night(self):
        start_event = dt.datetime(2021, 3, 6, 2, 0, 0)
        end_event = dt.datetime(2021, 3, 7, 2, 0, 0)

        self.assertGreater(end_event, start_event, "the event is correct")
        self.assertNotEqual(start_event.date(), end_event.date(), "the event is not the same date")
        self.assertGreaterEqual(start_event, self.start_night, "the event starts after 10pm (at night)")
        self.assertGreaterEqual(end_event, self.start_night, "the event ends after 6am")

if __name__ == '__main__':
    unittest.main()