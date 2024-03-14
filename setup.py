from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirments
    '''
    requirements=[]
    
    with open(file_path) as file_obj:
        requirments = file_obj.readlines()
        requirments= [req.replace('\n',"") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirments.remove(HYPHEN_E_DOT)
        
    return requirments


setup(
    name = 'mlproject',
    version = '0.0.1',
    author='tijo',
    author_email='thomastijo2000@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')
    
)