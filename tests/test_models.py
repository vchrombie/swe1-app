from django.test import TestCase
from django.utils import timezone

from polls.models import Question, Choice


class QuestionModelTests(TestCase):

    def test_str_method(self):
        question = Question(question_text='What is your name?', pub_date=timezone.now())
        self.assertEqual(str(question), 'What is your name?')


class ChoiceModelTests(TestCase):

    def test_str_method(self):
        choice = Choice(choice_text='Yes', votes=0)
        self.assertEqual(str(choice), 'Yes')

    def test_votes_increase(self):
        question = Question.objects.create(question_text='What is your name?', pub_date=timezone.now())
        choice = Choice.objects.create(question=question, choice_text='John', votes=0)
        choice.votes += 1
        choice.save()
        updated_choice = Choice.objects.get(pk=choice.pk)
        self.assertEqual(updated_choice.votes, 1)
