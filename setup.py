from setuptools import setup



setup(
    name='brain2lib',
    version='0.0.1',
    description='brain2 package',
    url='git@github.com:Samlarn/2blib.git',
    author='Samlarn',
    author_email='samlarn@example.com',
    license='MIT',
    packages=['src/brain2lib'],
    install_requires=[
        "SQLAlchemy==2.0.25",
    ],
    zip_safe=False
)
