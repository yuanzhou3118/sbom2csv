from setuptools import setup, find_packages

setup(
    name='sbom2csv',
    version='1.0.0',
    author='Yuan Zhou',
    author_email='zhouyuan3118@gmail.com',
    packages=find_packages(),
    install_requires=[
    ],
    entry_points={
        'console_scripts': [
            'sbom2csv=sbom2csv.generator:main',
        ],
    },
    url='https://github.com/yuanzhou3118/sbom2csv',
    license='LICENSE',
    description='Transform SBOM contents into a formatted csv file.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown'
)
