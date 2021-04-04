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
    send = SendEmail()
    send_spam = SendOfSpam(session, send)
    send_spam.send_emails(
        'renzo@python.br',
        'Curso Python',
        'Confira os modulos fantásticos',
    )
    assert len(usuarios) == send.qtd_email_send
