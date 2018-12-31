from setuptools import setup

setup(
    name="pollite",
    version="0.0.0",
    author="Carvell Scott",
    author_email="carvell.scott@gmail.com",
    keywords=["poll", "polling", "rate limited", "rate_limiting"],
    py_modules=["pollite"],
    url="https://github.com/CarvellScott/pollite",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Productivity",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5"
        "Programming Language :: Python :: 3.6"
    ],
    description="",
    long_description=open("README.md").read(),
)
