from setuptools import setup, find_packages

setup(
    name='django-ezutils',
    version=__import__('django_ezutils').__version__,
    description='Django easy to use utility.',
    long_description=open('README.md').read(),
    author='bmcool',
    author_email='bloggerbm@gmail.com',
    url='https://github.com/bmcool/django-ezutils',
    download_url='http://pypi.python.org/pypi/django-ezutils',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'django-facebook-api>=0.1.4',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
