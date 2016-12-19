"""Setup learning journal."""


from setuptools import setup

setup(
    name="learning journal",
    description="A learning journal built with Pyramid",
    version=0.1,
    author=["Rachel Wisecarver"],
    author_email="rachael.wisecarver@gmail.com",
    licencse="MIT",
    package_dir={'': 'src'},
    py_modules=["learning_journal"],
    extras_require={
        "test": ["pytest", "pytest-cov", "tox"]
    }
)
