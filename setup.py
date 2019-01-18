import os

import sys
from setuptools import setup


if sys.version_info.major < 3:
    sys.exit('Sorry, Python < 3 is not supported')

DIR = os.path.dirname(__file__)
REQUIREMENTS = os.path.join(DIR, 'requirements.txt')


with open(REQUIREMENTS) as f:
    reqs = f.read()

setup(
    name='fc_console',
    version='0.1.0',
    description='console for python',
    license='MIT Licence',
    url='https://github.com/fangqk1991/py-console',
    author='fang',
    author_email='me@fangqk.com',
    packages=['fc_console'],
    include_package_data=True,
    platforms='any',
    install_requires=reqs.strip().split('\n'),
)
