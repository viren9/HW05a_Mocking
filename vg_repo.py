"""author: viren ghori"""

import json
import requests

def get_repo_info(usr_name='ywang567'):
    """get users repository"""
    output = []
    usr_url = 'https://api.github.com/users/{}/repos'.format(usr_name)
    res = requests.get(usr_url)
    repos = json.loads(res.text)
    output.append('User: {}'.format(usr_name))

    try:
        repos[0]['name']
    except (TypeError, KeyError, IndexError):
        return 'can not fetch repos from user'

    try:
        for repo in repos:
            repo_name = repo['name']
            repo_url = 'https://api.github.com/repos/{}/{}/commits'.format(usr_name, repo_name)
            repo_if = requests.get(repo_url)
            repo_if_json = json.loads(repo_if.text)
            output.append('Repo: {} Number of commits: {}'.format(repo_name, len(repo_if_json)))
    except (TypeError, KeyError, IndexError):
        return 'can not fetch commits from repo'
    return output


if __name__ == '__main__':
    """call main function"""
    for entry in get_repo_info():
        print(entry)