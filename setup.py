"""
fish-hook
"""
import codecs
import os
import re
from setuptools import setup


with codecs.open(os.path.join(os.path.abspath(os.path.dirname(
        __file__)), 'fishhook', '__init__.py'), 'r', 'latin1') as fp:
    try:
        version = re.findall(r"^__version__ = '([^']+)'\r?$",
                             fp.read(), re.M)[0]
    except IndexError:
        raise RuntimeError('Unable to determine version.')

setup(
    name='fish-hook',
    version=version,
    url='https://github.com/dcalsky/fish-hook/',
    license='MIT',
    author='Dcalsky',
    author_email='dcalsky@gmail.com',
    description='A console tool which manages your github webhooks efficiently.',
    packages=['fishhook'],
    platforms='any',
    install_requires=[
        'click>= 6.7',
        'sanic>=0.3.1',
        'colorama'
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Build Tools'
    ],
    entry_points={
        'console_scripts': [
            'fish-hook = fishhook.command:main'
        ]
    },
)