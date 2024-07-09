import setuptools

setuptools.setup(
    name="OpenDTB-Framework",
    version="0.2.5",
    description="The underlying framework of CASIA's digital twin brain platform",
    author="Brain Net Group",
    url="https://github.com/OpenDTB/OpenDTB-Framework",
    install_requires=["traits>=6.4.1", "ulid-py"],
    packages=setuptools.find_packages(),
)
