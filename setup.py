from setuptools import setup

import pork

setup(
    name='pork',
    version=pork.__version__,
    description='Text snippets on the command line.',
    long_description=pork.__doc__,
    author='Jimmy Cuadra',
    author_email='jimmy@jimmycuadra.com',
    url='https://github.com/jimmycuadra/pork',
    license='MIT',
    packages=['pork'],
    install_requires=['docopt>=0.6,<1.0']
    entry_points={
        'console_scripts': ['pork = pork.cli:main']
    },
    zip_safe=True,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Utilities',
    ]
)
