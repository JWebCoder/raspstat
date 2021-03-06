from setuptools import setup, find_packages  # Always prefer setuptools over distutils
from codecs import open  # To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='Raspstat',

    version='0.1.1',

    description='Python wrapper to get system stats in linux',

    url='https://github.com/JWebCoder/raspstat',

    author='JWebCoder',
    author_email='joao87moura@gmail.com',

    license='GNU GPLv2',

    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search'
    ],

    keywords='raspberry stats linux',

    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),


)