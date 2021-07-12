import setuptools
import pathlib


def get_version(rel_path):
    """Get the version of library
    Args:
        rel_path (str): Relative path to __init__.py with version.
    Returns:
        str: Version of library
    """
    for line in pathlib.Path(rel_path).open('r').read().splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


# Parse README.md for long_description
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="classutilities",
    version=get_version('src/classutilities/__init__.py'),
    description="Class utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/david-salac/classutilities",
    packages=setuptools.find_packages(where='src'),
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
