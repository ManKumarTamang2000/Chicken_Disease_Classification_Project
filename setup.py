import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Chicken_Disease_Classification_Project"
AUTHOR_USER_NAME = "ManKumarTamang2000"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "nissanlama2020@gmail.com"


setuptools.setup(
    name="cnnClassifier",
    version="0.0.1",
    author="Man_Kumar_Tamang",
    author_email="nissanlama2020@.com",
    description="Chicken disease classification using CNN",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/ManKumarTamang2000/Chicken_Disease_Classification_Project",
    project_urls={
        "Bug Tracker": f"https://github.com/ManKumarTamang2000/Chicken_Disease_Classification_Project",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)