from setuptools import find_packages,setup
from typing import List

def get_requirements()->list[str]:
    """
    This Function will return list of requirements
    """

    requirement_lst : List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            ##Read lines from the file:
            lines = file.readlines()
            ##Processing each line:
            for line in lines:
                requirement=line.strip()
                ## Ignore empty lines and -e .:
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Sangram Goje",
    packages=find_packages(),
    install_requires = get_requirements()
)  