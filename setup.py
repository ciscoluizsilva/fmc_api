from setuptools import setup, find_packages

setup(
    name='fmc_api',
    version='0.1.1',
    packages=find_packages(),
    description='FMC API Framework for General Usage',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Luiz Lalanda Silva',
    author_email='luizsil@cisco.com',
    url='https://github.com/ciscoluizsilva/fmc_api',
    install_requires=[
        'pydantic==2.6.3',
        'requests==2.31.0'
    ],
    python_requires='>=3.10',  # Minimum version requirement of the package
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)