import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='Git Bundle Plus',  
     version='0.9.1',
     author="Ansèlm Joseph",
     author_email="anselmjosephs@gmail.com",
     description="Bundle a local Git project with all uncommitted changes and stashes (git bundle on steroids).",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/an23lm/GitBundlePlus",
     scripts=['gitbundleplus'],
     packages=['modules'],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
