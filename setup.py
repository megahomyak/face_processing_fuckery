from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read()

setup(
    name='is_that_you',
    version='0.0.1',
    url='https://github.com/megahomyak/is_that_you',
    author='megahomyak',
    author_email='g.megahomyak@gmail.com',
    description='A vtuber program with emotion recognition',
    packages=find_packages(),    
    install_requires=requirements.strip().splitlines(),
)
