import os
from setuptools import setup, find_packages

app_version = os.getenv("DOCKER_ANDROID_VERSION", "test-version")

with open("requirements.txt", "r") as f:
    reqs = f.read().splitlines()

setup(
    name="docker-android",
    version=app_version,
    url="https://github.com/wangzw/docker-android",
    description="CLI for docker-android",
    author="Budi Utomo",
    author_email="budtmo.os@gmail.com",
    install_requires=reqs,
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={"console_scripts": ["docker-android=app:cli"]},
)
