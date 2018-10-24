from setuptools import setup, find_packages

setup(
    name='umarell',
    version='1.0',
    description='Lightweight decorator that can be seamlessly integrated in all your Python '
                'projects to log the performance of your functions',
    author='Alessandro Bessi',
    author_email='alessandro.bessi@mail.com',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Pick your license as you wish
        'License :: MIT',

        # Specify the Python versions you support here.
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    keywords='umarell logging performance',
    packages=find_packages(exclude=['build', 'data', 'dist', 'docs', 'tests']),
    python_requires='>=3.6'
)
