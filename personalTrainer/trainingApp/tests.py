from django.test import TestCase
import datetime
from django.utils import timezone
# from .models import Question


# class QuestionMethodTests(TestCase):
#
#     def test_was_published_recently_with_future_question(self):
#         """
#         was_published_recently() should return False for questions whose
#         pub_date is in the future.
#         """
#         time = timezone.now() + datetime.timedelta(days=30)
#         future_question = Question(pub_date=time)
#         self.assertIs(future_question.was_published_recently(), False)

# class TestMyViews(TestCase):
#     # multi_db = True
#         # By default (when multi_db=False), fixtures are only loaded into the default database.
#         # If multi_db=True, fixtures are loaded into all databases.
#     def test_index_page_view(self):
#         call_some_test_code()

from django.core import mail
from django.test import TestCase

# class EmailTest(TestCase):
#     mail.outbox = []
#     def test_send_email(self):
#         # Send message.
#         mail.send_mail(
#             'Subject here', 'Here is the message.',
#             'from@example.com', ['to@example.com'],
#             fail_silently=False,
#         )
#
#         # Test that one message has been sent.
#         self.assertEqual(len(mail.outbox), 1)
#
#         # Verify that the subject of the first message is correct.
#         self.assertEqual(mail.outbox[0].subject, 'Subject here')
