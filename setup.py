from setuptools import setup, find_packages
from azuretablelogging import __version__

setup(
    name="azuretablelogging",
    version=__version__,
    url="https://github.com/uezo/azure-table-storage-logging",
    author="uezo",
    author_email="uezo@uezo.net",
    maintainer="uezo",
    maintainer_email="uezo@uezo.net",
    description="A handler class which writes formatted logging records to Azure Table Storage",
    packages=find_packages(exclude=["examples*"]),
    install_requires=["azure-cosmosdb-table"],
    license="Apache v2",
    classifiers=[
        "Programming Language :: Python :: 3"
    ]
)
