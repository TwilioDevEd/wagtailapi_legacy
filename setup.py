#!/usr/bin/env python

import sys

from setuptools import setup, find_packages

from wagtailapi_legacy import __version__


setup(
    name='wagtailapi_legacy',
    version=__version__,
    description='',
    author='Samuel Mendes',
    author_email='smendes@twilio.com',
    url='https://github.com/TwilioDevEd/wagtailapi_legacy',
    packages=find_packages(),
    include_package_data=True,
    license='BSD',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ],
    install_requires=[
        'six>=1.10.0',
    ],
    extras_require={
        'testing': [
            'Django>=3.0',
            'wagtail>=2.9',
            'mock>=1,<2',
        ],
    },
    zip_safe=False,
)
