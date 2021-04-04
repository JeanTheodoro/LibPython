class SendEmail:
    qtd_email_send = 0

    def enviar(self, remetente, destinatario, assunto, corpo):
        if '@' not in remetente:
            raise EmailInvalido(f'Email de rementente inválido {remetente}')
        self.qtd_email_send += 1
        return remetente


class EmailInvalido(Exception):
    pass
