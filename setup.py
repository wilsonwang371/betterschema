from setuptools import setup, find_packages

setup(
    name="pylatform",
    version="0.1.0",
    packages=find_packages("src", exclude=["tests"]),
    setup_requires=[
        "build",
    ],
    install_requires=[
    ],
    extras_require={
        "dev": [
            "unittest",
            "black",
            "build",
        ]
    },
    # only include from source directory
    package_dir={"": "src"},
)
