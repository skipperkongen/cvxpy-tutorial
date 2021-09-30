from setuptools import setup, find_packages

setup(
    name='cvxpytut',
    version='0.1.1',
    url='https://github.com/skipperkongen/cvxpy-tutorial.git',
    author='Pimin Konstantin Kefaloukos',
    author_email='skipperkongen@gmail.com',
    description='Small collection of CVXPY problems for learning',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=['cvxpy'],
)
