import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "text-summarizer-NLP"
AUTHOR_USER_NAME = "Arpitha-Rajeev1"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "arpitha.rajeev37@gmail"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for text summarization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Arpitha-Rajeev1/textSummarizer-NLP",
    project_urls={
        "Bug Tracker": "https://github.com/Arpitha-Rajeev1/textSummarizer-NLP/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)