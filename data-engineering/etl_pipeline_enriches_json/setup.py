from setuptools import setup

setup(
    name="geocode",
    version="0.1",
    py_modules=["geocode_util", "reader", "writer"],
    install_requires=["requests"],
)
