from vg_repo import get_repo_info
import unittest

class TestGetRepo(unittest.TestCase):
    def test_normal_response(self):
        expected = ['User: ywang567',
                    'Repo: test1 Number of commits: 3',
                    'Repo: test2 Number of commits: 2',
                    'Repo: Triangle567 Number of commits: 1']
        self.assertEqual(get_repo_info(), expected)

    def test_bad_user_name(self):
        self.assertEqual(get_repo_info('aaaabbbbcccc'),'can not fetch repos from user')
        self.assertEqual(get_repo_info(''),'can not fetch repos from user')


if __name__ == '__main__':
    unittest.main()