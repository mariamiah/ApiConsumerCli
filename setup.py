from setuptools import setup

setup(
    name='apiconsumercli',
    version='1.0',
    py_modules=['api'],
    install_requires=['click'],
    entry_points='''[console_scripts]
                     api = api:cli ''',
)
