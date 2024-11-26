from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    




setup(
    name =" ML project",
    version = "0.0.1",
    author ='rsqr',
    author_email ='random',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)