#!/usr/bin/env python3
from distutils.core import setup
from pdfminer import __version__

setup(
    name='pdfminer3k',
    version=__version__,
    description='PDF parser and analyzer',
    long_description='''pdfminer3k is a Python 3 port of pdfminer.
PDFMiner is a tool for extracting information from PDF documents.
Unlike other PDF-related tools, it focuses entirely on getting 
and analyzing text data. PDFMiner allows to obtain
the exact location of texts in a page, as well as 
other information such as fonts or lines.
It includes a PDF converter that can transform PDF files
into other text formats (such as HTML). It has an extensible
PDF parser that can be used for other purposes instead of text analysis.''',
    license='MIT/X',
    author='Yusuke Shinyama',
    author_email='yusuke at cs dot nyu dot edu',
    maintainer='Virgil Dupras',
    maintainer_email='hsoft@hardcoded.net',
    url='http://bitbucket.org/hsoft/pdfminer3k',
    install_requires=[
        'pytest>=2.0',
        'ply>=3.4',
    ],
    packages=[
    'pdfminer',
    'pdfminer.cmap',
    ],
    package_data={
    'pdfminer.cmap': ['*.pickle.gz'],
    },
    scripts=[
    'tools/pdf2txt.py',
    'tools/dumppdf.py',
    'tools/latin2ascii.py',
    ],
    keywords=['pdf parser', 'pdf converter', 'layout analysis', 'text mining'],
    classifiers=[
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
    'Topic :: Text Processing',
    ],
)
