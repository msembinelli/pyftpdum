from setuptools import setup

setup(
    name='pyftpdum',
    version='0.1',
    py_modules=['cli', 'pyftpdum', 'yaml_storage'],
    test_suite='test',
    install_requires=[
        'click',
        'pyyaml',
        'tinydb',
    ],
    entry_points='''
        [console_scripts]
        pyftpdum=cli:cli
    ''',
)
