from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from polls.models import Question, Choice


class VoteViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.question = Question.objects.create(
            question_text="What is your name?", pub_date=timezone.now())  # fmt: skip
        self.choice = Choice.objects.create(question=self.question, choice_text="John")

    def test_vote_view_with_invalid_choice(self):
        """Test that an error message is displayed when no choice is selected"""
        url = reverse("polls:vote", args=(self.question.id,))
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "You didn't select a choice.")
        self.assertQuerysetEqual(response.context["question"].choice_set.all(), [])
