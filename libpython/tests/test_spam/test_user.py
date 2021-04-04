from libpython.spam.modelos import User


def test_salvar_user(session):

    user = User(name='Renzo', email='renzo@python.br')
    session.save(user)
    assert isinstance(user.id, int)


def test_list_user(session):

    list_users = [User(name='Renzo', email='renzo@python.br'), User(name='Luciano', email='luciano@python.br')]
    for user in list_users:
        session.save(user)
    assert list_users == session.list()
