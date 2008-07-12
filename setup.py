#!/usr/bin/env python
# 
# setup for TakeNote
#
# use the following command to install TakeNote:
#   python setup.py install
#
#=============================================================================


# python and distutils imports
import os, sys, shutil
from distutils.core import setup, Extension

# py2exe module (if building on windows)
try:
    import py2exe
except ImportError:
    pass

#=============================================================================
# constants

TAKENOTE_VERSION = '0.4'


#=============================================================================
# resource files/data

# get images
image_dir = "takenote/images"
image_files = [os.path.join(image_dir, x) 
               for x in os.listdir("takenote/images")]


# get data files
if "py2exe" in sys.argv:
    data_files = [
        ('images', image_files),
        
        ('rc', ['takenote/rc/takenote.glade'])
    ]
    package_data = {}
else:
    data_files = []
    package_data = {'takenote': image_files + [
                                "rc/takenote.glade"]}


#=============================================================================
# setup

setup(
    name='takenote',
    version=TAKENOTE_VERSION,
    description='A cross-platform note taking application',
    long_description = """
        TakeNote is a cross-platform note taking application.  Its features 
        include:
        
        - rich text editing
        - hierarchical organization for notes
        - full text search
        - inline images
        - integrated screenshot
        - spell checking (via gtkspell)
        - backup and restore
    """,
    author='Matt Rasmussen',
    author_email='rasmus@mit.edu',
    url='http://rasm.ods.org/takenote/',
    download_url='http://rasm.ods.org/takenote/download/takenote-%s.tar.gz' % TAKENOTE_VERSION,
    
    classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Environment :: Win32 (MS Windows)',
          'Environment :: X11 Applications',
          'Intended Audience :: Developers',
          'Intended Audience :: Education',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: General Public License (GPL)',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          ],
    license="GPL",
    
    packages=['takenote', 'takenote.gui'],
    scripts=['bin/takenote'],
    data_files=data_files,
    package_data=package_data,
    
    windows=[{
        'script': 'bin/takenote',
        'icon_resources': [(1, 'takenote/images/takenote.ico')],
        }],
    options = {
        'py2exe' : {
            'packages':'encodings',
            'includes': 'cairo,pango,pangocairo,atk,gobject',
        },
        #'sdist': {
        #    'formats': 'zip',
        #}
    }
    )


# execute post-build script
if "py2exe" in sys.argv:
    execfile("post_py2exe.py")
