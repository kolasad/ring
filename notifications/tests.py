from django.core import mail
from django.test import TestCase, Client


class SendMailTestCase(TestCase):
    def setUpClasss(self):
        self.client = Client()

    def test_send_mail(self):
        data = {'message': 'asd', 'recipient': 'test@test.com'}

        response = self.client.post('/mails/send', data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'New email message title')

    def test_fail_invalid_data_send_mail(self):
        data = {'message': 'Hello'}

        response = self.client.post('/mails/send', data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(len(mail.outbox), 0)

        response = self.client.post('/mails/send')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(len(mail.outbox), 0)
