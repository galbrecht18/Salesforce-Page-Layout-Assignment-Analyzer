from setuptools import setup

setup(
    name='Page Layout Assignment Analyzer',
    author='George Albrecht',
    packages=['pageLayoutAssignmentAnalyzer'],
    install_requires=['xlsxwriter'],
    version='0.1',
    license='MIT',
    description='Used to analyze sfdx extracted layouts and determine if they are actively used',
)