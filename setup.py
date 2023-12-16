from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read() 

INSTALL_REQUIRES = []

def doSetup(install_requires):
    setup(
        name='Code',
        version='0.15',
        author=' Ehsan Aalaei ',
        author_email='eaalaei',
        url='https://github.com/eaalaei/BioE537',
        description='Fluid flow Simulation in Tissue',
        long_description=long_description,
        long_description_content_type='text/markdown',
        packages=['Code'],
        package_dir={'Code':
            'Code'},
        install_requires=install_requires,
        include_package_data=True,
        classifiers=[
            'Development Status :: 3 - Alpha',  
            'Intended Audience :: Science/Research',
            'Topic :: Scientific/Engineering',
            'License :: OSI Approved :: MIT License', 
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Programming Language :: Python :: 3.11',
        ],
    )

if __name__ == '__main__':
  doSetup(INSTALL_REQUIRES)
