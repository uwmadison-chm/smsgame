"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.db import IntegrityError
from . import models
import random
import datetime


class ParticipantTest(TestCase):

    def setUp(self):
        random.seed(0)
        self.today = datetime.date(2011, 7, 1) # Not really today.
        self.exp = models.Experiment.objects.create(task_days=7, game_days=5)
        self.p1 = models.Participant.objects.create(
            experiment=exp, start_date=self.today)


class PhoneNumberTest(TestCase):

    def testCreation(self):
        num = "6085551212"
        ph = models.PhoneNumber(num)
        self.assertEqual(num, ph.cleaned)

    def testStripNonNumeric(self):
        num = " 608555asjdha!dna1#}(212 "
        cleaned = "6085551212"
        ph = models.PhoneNumber(num)
        self.assertEqual(cleaned, ph.cleaned)

    def testStripLeadingOne(self):
        num = " 16085551212"
        cleaned = "6085551212"
        ph = models.PhoneNumber(num)
        self.assertEqual(cleaned, ph.cleaned)

    def testSaveOriginalString(self):
        num = "6085551212sldfkdsfj"
        ph = models.PhoneNumber(num)
        self.assertEqual(num, ph.original_string)

    def testDontFormatOddLengths(self):
        num = "55512"
        ph = models.PhoneNumber(num)
        self.assertEqual(num, str(ph))

    def testDoSevenDigitFormatting(self):
        num = "5551212"
        formatted = "555-1212"
        ph = models.PhoneNumber(num)
        self.assertEqual(formatted, str(ph))

    def testDoTenDigitFormatting(self):
        num = "6085551212"
        formatted = "(608) 555-1212"
        ph = models.PhoneNumber(num)
        self.assertEqual(formatted, str(ph))


class TaskDayTest(TestCase):

    def setUp(self):
        self.today = datetime.date(2011, 7, 1) # Not really today.
        self.exp = models.Experiment.objects.create()
        self.p1 = models.Participant.objects.create(
            experiment=self.exp, start_date=self.today)

    def testCantCreateTaskDayTwice(self):
        td1 = self.p1.taskday_set.create(task_day=self.today)
        with self.assertRaises(IntegrityError):
            td2 = self.p1.taskday_set.create(task_day=self.today)