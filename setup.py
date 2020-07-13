# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

setup(
    name="redisfe",
    version="0.0.1",
    packages=find_packages(),
    entry_points={"console_scripts": ("redisfe=redisfe.main:main",)},
)
