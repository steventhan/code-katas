# -*- coding: utf -8*-
from setuptools import setup

setup(
    name="Proper Parenthetics",
    description="Proper Parenthetics for code challenge",
    version=0.1,
    license='MIT',
    author="Steven Than",
    author_email="steventhan11@gmail.com",
    py_modules=['linked_list', 'stack', 'check_parentheses'],
    package_dir={' ': '.'},
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-cov', 'tox']},
)
