from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from django.http import HttpResponseRedirect
from polls.models import Question, Choice


class VoteViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.question = Question.objects.create(
            question_text="What is your name?", pub_date=timezone.now())  # fmt: skip
        self.choice = Choice.objects.create(question=self.question, choice_text="John")

    def test_vote_view_with_valid_choice(self):
        """Test that the selected choice gets voted"""
        url = reverse("polls:vote", args=(self.question.id,))
        response = self.client.post(url, {"choice": self.choice.id})
        updated_choice = Choice.objects.get(pk=self.choice.pk)
        self.assertEqual(response.status_code, HttpResponseRedirect.status_code)
        self.assertEqual(updated_choice.votes, 1)
