from setuptools import setup, find_packages

setup(
    name="bitcoinql",
    use_scm_version=True,
    license="MIT",
    description="",
    long_description="",
    author="Brett Dawidowski",
    author_email="brett@codedawi.com",
    url="https://github.com/codedawi/bitcoinql-python",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    project_urls={
        "Changelog": "https://github.com/codedawi/python-bitcoinql/blob/master/CHANGELOG.md",
        "Issue Tracker": "https://github.com/codedawi/python-bitcoinql/issues",
    },
    keywords=[
        "bitcoin", "graphql"
    ],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*",
    install_requires=[
        "aiohttp>=3.6.2",
        "graphene>=2.1.8",
        "pydantic>=1.5.1",
    ],
    extras_require={
        "dev": [
            "pytest>=5.2",
        ],
    },
    setup_requires=[
        "setuptools_scm>=3.3.1",
    ],
    entry_points={
        "console_scripts": [
            "bitcoinql = bitcoinql.cli:main",
        ]
    },
)
