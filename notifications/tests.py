from django.contrib.auth.models import User
from django.core import mail
from django.test import TestCase
from rest_framework.test import APIClient


class SendMailTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super(SendMailTestCase, cls).setUpClass()
        cls.api_client = APIClient()
        cls.user = User.objects.create_user(
            username='test', email='test@test.com', password='test'
        )
        cls.api_client.force_authenticate(user=cls.user)

    def test_send_mail(self):
        subject = 'Some subject'
        data = {'message': 'asd', 'recipient': 'test@test.com', 'subject': subject}
        response = self.api_client.post('/mails/send', data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, subject)

    def test_fail_invalid_data_send_mail(self):
        data = {'message': 'Hello'}
        response = self.api_client.post('/mails/send', data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(len(mail.outbox), 0)

        response = self.api_client.post('/mails/send')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(len(mail.outbox), 0)
