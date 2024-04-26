from setuptools import setup, find_packages, Extension
import os


module = Extension(
    "pylatform",
    # all c files in the lib/src directory
    sources=[
        os.path.join("lib", "src", f) for f in os.listdir("lib/src") if f.endswith(".c")
    ],
    include_dirs=["lib/include"],
    extra_compile_args=["-O3", "-Wall", "-Wextra", "-Werror", "-std=c11"],
    extra_link_args=["-O3", "-Wall", "-Wextra", "-Werror", "-std=c11"],
)


setup(
    name="pylatform",
    version="0.1.0",
    packages=find_packages("src", exclude=["tests"]),
    setup_requires=[
        "build",
    ],
    install_requires=[],
    extras_require={
        "dev": [
            "unittest",
            "black",
            "build",
        ]
    },
    # only include from source directory
    package_dir={"": "src"},
    ext_modules=[module],
)
