import sys
import unittest

from conference_badges import *

class TestConferenceBadges(unittest.TestCase):

    def setUp(self):
        self.name = "Andrew"
        self.attendees = ["Edsger", "Ada", "Charles", "Alan", "Grace", "Linus", "Matz"]
        self.badges = [
                  "Hello, my name is Edsger.",
                  "Hello, my name is Ada.",
                  "Hello, my name is Charles.",
                  "Hello, my name is Alan.",
                  "Hello, my name is Grace.",
                  "Hello, my name is Linus.",
                  "Hello, my name is Matz."
               ]
        self.room_assignments = [
                            "Hello, Edsger! You'll be assigned to room 1!",
                            "Hello, Ada! You'll be assigned to room 2!",
                            "Hello, Charles! You'll be assigned to room 3!",
                            "Hello, Alan! You'll be assigned to room 4!",
                            "Hello, Grace! You'll be assigned to room 5!",
                            "Hello, Linus! You'll be assigned to room 6!",
                            "Hello, Matz! You'll be assigned to room 7!"
                         ]
        self.badges_and_room_assignments = """
Hello, my name is Edsger.
Hello, my name is Ada.
Hello, my name is Charles.
Hello, my name is Alan.
Hello, my name is Grace.
Hello, my name is Linus.
Hello, my name is Matz.
Hello, Edsger! You'll be assigned to room 1!
Hello, Ada! You'll be assigned to room 2!
Hello, Charles! You'll be assigned to room 3!
Hello, Alan! You'll be assigned to room 4!
Hello, Grace! You'll be assigned to room 5!
Hello, Linus! You'll be assigned to room 6!
Hello, Matz! You'll be assigned to room 7!
        """.strip()

    def test_badge_maker(self):
        self.assertEqual(badge_maker(self.name), "Hello, my name is Andrew.")

    def test_batch_badge_creator(self):
        self.assertEqual(batch_badge_creator(self.attendees), self.badges)

    def test_assign_rooms(self):
        self.assertEqual(assign_rooms(self.attendees), self.room_assignments)

    def test_printer(self):
        self.assertEqual(printer(self.attendees), self.badges_and_room_assignments)

if __name__ == '__main__':
    unittest.main()
