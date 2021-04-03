import pytest

from libpython.spam.send_email import SendEmail, EmailInvalido


def test_send_email():
    send = SendEmail()
    assert send is not None


@pytest.mark.parametrize(
    'destinatario',
    ['foo@br.com.br', 'renzo@python.pro.br']
)
def test_remetente(destinatario):
    send = SendEmail()
    result = send.enviar(
        destinatario,
        'luciano@python.pro.br',
        'Curso Python Pro',
        'Primeira turma Guido Von Rossum aberta.'
    )
    assert destinatario in result


@pytest.mark.parametrize(
    'remetente',
    ['', 'renzo']
)
def test_remetente_invalido(remetente):
    send = SendEmail()
    with pytest.raises(EmailInvalido):
        send.enviar(
            remetente,
            'luciano@python.pro.br',
            'Curso Python Pro',
            'Primeira turma Guido Von Rossum aberta.'

        )
