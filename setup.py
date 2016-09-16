from setuptools import setup

setup(
    name="code-katas",
    description="",
    version=0.1,
    author="Steven Than",
    author_email="",
    license="MIT",
    install_requires=["networkx"],
    extras_requires={"test": ["pytest", "pytest-watch", "pytest-cov", "tox"]},
    entry_points={
        "console_scripts": [
        ]
    }
)
