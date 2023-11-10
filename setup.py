import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.1"

REPO_NAME = "extract_wc_data"
AUTHOR_USER_NAME = "hrisikesh-neogi"
SRC_REPO = "ExtractWCData"
AUTHOR_EMAIL = "hrisikesh.neogi@gmail.com"


setuptools.setup( 
    name = REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description= "A single Package to extract wc 2023 data.",
    long_description=long_description,
    long_description_content_type = "text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    classifiers= [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires = ">=3.8",

    install_requires = [
        'chromedriver-binary',
       ' requests==2.31.0',
        'selenium==4.15.2',
        'six==1.14.0',
        'pandas==2.0.0'

    ],

)