from setuptools import setup

setup(
    name='personalTrainer',
    version='0.1',
    python = 'python 3.6'
    packages=[
        'personalTrainer',
        ],
    install_requires=[
        "requests",
        "psycopg2",
        "django",
        "Jinja2",
        # "pandas",
        ],

    author='Boris V',

    packages=find_packages(exclude=['tests*']),

    long_description=open('README.md').read(),
    # ...
)
