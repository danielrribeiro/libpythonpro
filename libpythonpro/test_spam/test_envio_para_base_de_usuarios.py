import pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadordeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Daniel', email='danielrodriguesr@gmail.com'),
            Usuario(nome='Geraldo', email='jgrsilva55@gmail.com')
        ],
        [
            Usuario(nome='Daniel', email='danielrodriguesr@gmail.com'),
        ]
    ]
)
def test_qtd_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadordeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'danielrodriguesr@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.qtd_email_enviados


class EnviadorMock(Enviador):

    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados += 1


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Daniel', email='danielrodriguesr@gmail.com')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadordeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'jgrsilva55@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert enviador.parametros_de_envio == (
        'jgrsilva55@gmail.com',
        'danielrodriguesr@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
