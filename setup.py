import setuptools

setuptools.setup(
    name="database-connector",
    version="0.0.1",
    python_requires=">=3.11",
    packages=setuptools.find_packages(),
    install_requires=[
        'snowflake-sqlalchemy',
        'pandas',
        'PyMySQL',
        'python-dotenv'
    ]
)