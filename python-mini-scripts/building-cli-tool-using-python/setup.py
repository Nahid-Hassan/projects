from setuptools import setup
setup(
    name='helloworld-cli',
    version='0.1.0',
    packages=['helloworld'],
    entry_points={
        'console_scripts': [
            'hellowold = helloworld.__main__:main'
        ]
    })
