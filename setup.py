from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='Page Layout Assignment Analyzer',
    # url='https://github.com/jladan/package_demo',
    author='George Albrecht',
    # Needed to actually package something
    packages=['pageLayoutAssignmentAnalyzer'],
    # Needed for dependencies
    install_requires=['xlsxwriter'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='Used to analyze sfdx extracted layouts and determine if they are actively used',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)