from setuptools import setup

setup(
    name='bulb',
    version='1.0.1',
    packages=[''],
    url='https://github.com/corka149/bulb',
    license='MIT',
    author='corka149',
    author_email='corka149@mailbox.org',
    description='A safe CLI for changing display brightness',
    install_requires=[
        "click",
        "colorama"
    ],
    entry_points={
        "console_scripts": [
            "bulb = bulb:main"
        ]
    }
)
