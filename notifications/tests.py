from django.core import mail
from django.test import TestCase, Client


class SendMailTestCase(TestCase):
    def test_send_mail(self):
        data = {'message': 'asd', 'recipient': 'test@test.com'}

        client = Client()
        response = client.post('/mails/send', data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'New email message title')


# def test_fail_invalid_data_send_mail():
#     data = {'message': 'Hello'}
#     # TODO wysylka maila
#     # sprawdzamy czy dostalismy 400 i odpwiednia messsage w odpwiedzi


# TODO ORM, ile jest kwiatow o takiej samej nazwie,
# ile jest kwiatow o takiej samej nazwie i kolorze
