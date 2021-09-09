from distutils.core import setup

setup(
    name='partnerizeapi',
    packages=['partnerizeapi'],
    version='0.1',
    license='MIT',
    description='A python library for performing common Partnerize API tasks.',
    author='Cris Griffith',
    author_email='cris.griffith@partnerize.com',
    url='https://github.com/webmasterjunkie/partnerizeapi',
    download_url='https://github.com/webmasterjunkie/partnerizeapi/archive/refs/tags/v0.1.tar.gz',
    keywords=['partnerize', 'affiliate', 'api'],
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
)
