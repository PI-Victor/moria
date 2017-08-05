from setuptools import setup, find_packages

VERSION='0.1'

long_description='A system monitoring service for Linux.'
packages=[
    'moria',
]
install_requires=[
    'flask',
    'flask-restful',
    'statsd',
    'click',
    'psutil',
]
def main():
    setup_info = dict(
        name='Moria',
        version=VERSION,
        author='https://github.com/PI-Victor',
        url='https://github.com/codeflavor/moria',
        description='Monitoring services.',
        long_description=long_description,
        license='Apache-2.0',
        packages=packages,
        install_requires=install_requires,
        zip_safe=False,
    )

    setup(**setup_info)

if __name__ == '__main__':
    main()
