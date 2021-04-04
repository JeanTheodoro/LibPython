class SendOfSpam:
    def __init__(self, session, send):
        self.session = session
        self.send = send

    def send_emails(self, remetente, assunto, corpo):
        for user in self.session.list():
            self.send.enviar(
                remetente,
                user.email,
                assunto,
                corpo
            )
