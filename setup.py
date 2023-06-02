from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='desc_stats',
    version='0.0.1',
    description="Descriptive Statistics comprises of Measures of Central Tendency, Dispersion, Symmetry, Association, Normal Distribution, Misc.",
    py_modules=['desc_stats'],  
    install_requires=[
        'numpy',
        'pandas',
        'scipy',
        'statsmodels'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    extras_require={
        "dev": [
            "pytest",
            "twine",
        ],
    },
    test_suite='tests',
    package_dir={'': 'src'},
    packages = find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vinayvinu500/desc_stats",
    author="Vinay Govardhanam",
    author_email="vinayvinu500@gmail.com",
)
