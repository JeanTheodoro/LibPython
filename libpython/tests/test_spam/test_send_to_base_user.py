from unittest.mock import Mock

import pytest

from libpython.spam.main import SendOfSpam
from libpython.spam.modelos import User
from libpython.spam.send_email import SendEmail


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            User(name='Renzo', email='renzo@python.br'),
            User(name='Luciano', email='luciano@python.br')
        ],
        [
            User(name='Renzo', email='renzo@python.br'),
        ]
    ]
)
def test_qde_of_spam(session, usuarios):

    for user in usuarios:
        session.save(user)
    send = Mock()
    send_spam = SendOfSpam(session, send)
    send_spam.send_emails(
        'renzo@python.br',
        'Curso Python',
        'Confira os modulos fantásticos',
    )
    assert len(usuarios) == send.enviar.call_count


class SendEmailMock(SendEmail):

    def __init__(self):
        super().__init__()
        self.qtd_email_send = 0
        self.params_of_send = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.params_of_send = (remetente, destinatario, assunto, corpo)
        self.qtd_email_send += 1


def test_params_of_spam(session):

    user = User(name='Renzo', email='renzo@python.br')
    session.save(user)
    send = Mock()
    send_spam = SendOfSpam(session, send)
    send_spam.send_emails(
        'luciano@python.br',
        'Curso Python',
        'Confira os modulos fantásticos'
    )
    send.enviar.assert_called_once_with(
        'luciano@python.br',
        'renzo@python.br',
        'Curso Python',
        'Confira os modulos fantásticos'
    )
