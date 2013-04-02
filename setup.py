from setuptools import setup

setup(
    name='xkcdbrute',
    version='0.1.0',
    install_requires=['pyskein', 'requests'],
    packages=['xkcdbrute'],
    entry_points="""
    [console_scripts]
    xkcdbrute-server = xkcdbrute:run_server
    xkcdbrute-client = xkcdbrute:run_client
    """)
