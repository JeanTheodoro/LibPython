import requests


def search_avatar(username):
    """"
        function that fetches the user's avatar on github
        :param username : str username's user
        :return: str vayar link
    """
    url = f'https://api.github.com/users/{username}'
    return requests.get(url).json()['avatar_url']


if __name__ == '__main__':
    user = str(input('informe o username do github: '))
    try:
        link_url = search_avatar(user)
    except KeyError:
        print(f'o avatar do usuário {user} não foi encontado')
    else:
        print('click no link:', link_url)
