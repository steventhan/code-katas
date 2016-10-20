from setuptools import setup

setup(
    name="String Pyramid",
    description="Code Kata String Pyramid",
    version=0.1,
    author="Steven Than",
    author_email="steventhan11@gmail.com",
    license="MIT",
    py_modules=[],
    install_requires=[],
    extras_requires={"test": ["pytest", "pytest-watch", "pytest-cov", "tox"]},
    entry_points={
        "console_scripts": [
        ]
    }
)
