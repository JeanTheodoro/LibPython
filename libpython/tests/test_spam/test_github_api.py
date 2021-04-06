from unittest.mock import Mock

import pytest
from pytest_mock import mocker

from libpython import github_api


def test_search_avatar(avatar_url):

    url = github_api.search_avatar('JeanTheodoro')
    assert avatar_url == url


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/69826260?v=4'
    resp_mock.json.return_value = {
        'login': 'JeanTheodoro', 'id': 69826260,
        'avatar_url': url,
    }
    get_mock = mocker.patch('libpython.github_api.requests.get')
    get_mock.return_value=resp_mock
    return url


def test_search_avatar_integration():

    url = github_api.search_avatar('JeanTheodoro')
    assert 'https://avatars.githubusercontent.com/u/69826260?v=4' == url
