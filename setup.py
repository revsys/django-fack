from setuptools import setup, find_packages

setup(
    name = 'django-faq',
    version = '0.1.0',
    description = 'A simple FAQ application for Django sites.',
    long_description = open('README.rst').read(),
    
    author  ='Kevin Fricovsky',
    author_email = 'kfricovsky@gmail.com',
    url = 'http://github.com/howiworkdaily/django-faq',
    
    packages = find_packages(exclude=['example']),
    zip_safe = False,
    
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    
    install_requires = ['setuptools', 'Django >= 1.3'],
)
