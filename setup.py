from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='rm_known_host',
    version='0.3.0',
    author='R. Keith Ellerbe',
    author_email='reellerb@cisco.com',
    description='A utility for removing dead host from ~/.ssh/known_host',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/rkellerbe/rm_known_host',
    packages=find_packages('src')
)