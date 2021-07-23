import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="troykahat",
    version="1.0.0",
    description="Raspberry Pi library for interaction with a Amperka TroykaHAT.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/amperka/TroykaHatPython",
    author="Amperka LLC",
    author_email="igor@amperka.com",
    license="GPLv3",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["troykahat"],
    install_requires=["wiringpi"],
)