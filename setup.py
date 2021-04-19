import io

from setuptools import find_packages
from distutils.core import setup

readme = io.open("./README.md", encoding="utf-8").read()

setup(
    name="project",
    version="0.0.1",
    description="Webserver for Covidioten App",
    long_description=readme,
    long_description_content_type="text/x-rst",
    author="Christoph Könning",
    author_email="chris@casualcompany.de",
    url="https://github.com/Covidioten/WebServer",
    license="MIT License",
    python_requires=">=3.7,<3.8",
    install_requires=[
        "flask_cors",
        "flask_sqlalchemy"
    ],
    tests_require=[
        'pytest >= 3.7.4',
        'pytest-cov',
    ],
    entry_points={
    },
    packages=find_packages(
        exclude=["tests", "tests.*", "examples", "examples.*"]),
    include_package_data=True,
    package_data={
    },
    zip_safe=False,
)
