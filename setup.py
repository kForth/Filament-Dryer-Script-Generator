#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

with open("README.rst") as readme_file:
    readme = readme_file.read()

requirements = []

test_requirements = []

setup(
    author="Kestin Goforth",
    author_email="kgoforth1503@gmail.com",
    python_requires=">=3.6",
    description="Generates a gcode file to set your 3D printer's bed or enclosure to a specific temperature for a set amount of time in order to dry spools of filament.",
    entry_points={
        "console_scripts": [
            "filament_dryer_script_generator=filament_dryer_script_generator.__main__:main",
        ],
    },
    install_requires=requirements,
    license="GNU Affero General Public License v3",
    long_description=readme,
    long_description_content_type="text/x-rst",
    include_package_data=True,
    keywords="filament_dryer_script_generator",
    name="filament_dryer_script_generator",
    packages=find_packages(
        include=["filament_dryer_script_generator", "filament_dryer_script_generator.*"]
    ),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/kforth/Filament-Dryer-Script-Generator",
    version="0.2.0",
    zip_safe=False,
)
