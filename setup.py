from setuptools import setup, find_packages

setup(
    name='django-ezutils',
    version=__import__('django_ezutils').__version__,
    description='Django easy to use utility.',
    long_description=open('README.rst').read(),
    author='bmcool',
    author_email='bloggerbm@gmail.com',
    url='https://github.com/bmcool/django-ezutils',
    download_url='http://pypi.python.org/pypi/django-ezutils',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'Django==1.4.5',
        'Mezzanine==1.4.6',
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
