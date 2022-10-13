from unittest.mock import Mock

from libpythonpro import github_api


def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.retur_value = {
        'login': 'danielrribeiro', 'id': 113479421,
        'avatar_url': 'https://avatars.githubusercontent.com/u/113479421?v=4',
    }
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('danielrribeiro')
    assert 'https://avatars.githubusercontent.com/u/113479421?v=4' == url
