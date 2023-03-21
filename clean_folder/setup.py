from setuptools import setup

setup(
    name="clean_folder",
    version="0.1",
    scripts=["clean_folder/clean_folder/clean.py"],
    install_requires=["click"],
    entry_points="""
        [console_scripts]
        clean-folder=clean_folder.clean:clean_folder
    """
)