"""Setup the package creation and installation."""
import os
from setuptools import setup, find_packages, Command


class CleanCommand(Command):
    """Custom clean command to tidy up the project root."""

    user_options = []

    def initialize_options(self):  # noqa
        pass

    def finalize_options(self):  # noqa
        pass

    def run(self):  # noqa
        os.system('rm -vrf ./build ./dist '  # nosec
                  './*.pyc ./*.tgz ./*.egg-info')


setup(
    zip_safe=True,
    name="precogs",
    version="1.1.7",
    description=("Traces by Analytics desctiption."),
    keywords='',
    license="MIT License",
    packages=find_packages(exclude=['contrib', 'docs', 'tests*', 'examples*']),
    url='',
    author='Agustin March',
    author_email='agustin.march@gmail.com',
    long_description='Python application to process aviationstack data',
    python_requires='>=3.6, !=3.0.*, !=3.1.*, !=3.2.*, <4',
    install_requires=[
        "psycopg2-binary==2.8.6"
    ],
    # package_data={"precogs": ["sink/conf/default.yaml"]},
    classifiers=[
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: MIT License",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8"
    ],
    cmdclass={
        'clean': CleanCommand,
    })
