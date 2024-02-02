from setuptools import setup



setup(
    name='brain2lib',
    version='0.0.1',
    description='brain2 package',
    url='http://github.com/storborg/funniest',
    author='Samlarn',
    author_email='samlarn@example.com',
    license='MIT',
    packages=['src/brain2lib'],
    zip_safe=False,
    install_requires=[
        "SQLAlchemy==2.0.25",
    ]
)
