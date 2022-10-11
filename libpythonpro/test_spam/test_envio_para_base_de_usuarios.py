from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadordeSpam


def test_envio_de_spam(sessao):
    enviador_de_spam = EnviadordeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        'danielrodriguesr@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
