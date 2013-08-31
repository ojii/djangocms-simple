from setuptools import setup, find_packages

version = __import__('djangocms_simple').__version__

setup(
    name = 'djangocms-simple',
    version = version,
    description = 'Simpler APIs for django CMS',
    author = 'Jonas Obrist',
    author_email = 'ojiidotch@gmail.com',
    url = 'http://github.com/ojii/djangocms-simple',
    packages = find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires = [
        'django-cms',
    ],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
    ]
)
