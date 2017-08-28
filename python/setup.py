import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to pytest")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ''

    def run_tests(self):
        import shlex
        # Import here, because imports outside the eggs aren't loaded.
        import pytest
        errno = pytest.main(shlex.split(self.pytest_args))
        sys.exit(errno)


config = {
    'description': 'Codewars',
    'author': 'Stallmanifold',
    'url': 'https://github.com/stallmanifold/codewars',
    'download_url': 'https://github.com/stallmanifold/codewars.git',
    'author_email': 'stallmanifold@gmail.com',
    'version': '0.1',
    'install_requires': ['pytest'],
    'package_dir': {'': 'src'},
    'packages': ['codewars'],
    'scripts': [],
    'name': 'codewars',
    'tests_require': ['pytest', 'pytest-bdd'],
    'cmdclass' : {'test': PyTest}
}

setup(**config)
