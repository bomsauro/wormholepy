from setuptools import setup

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='wormholepy',
    version='0.2.0',
    description='A package to check Wormhole airdrop',
    url='https://github.com/bomsauro/wormholepy',
    author='Bomsauro',
    author_email='bomsauro@gmail.com',
    license='BSD 2-clause',
    packages=['wormholepy'],
    install_requires=['requests'],
    long_description=long_description,
    long_description_content_type='text/markdown'
)