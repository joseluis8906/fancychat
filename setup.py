from setuptools import setup

setup(
    name='fancychat',
    version='1.0.1',
    package_dir={'': 'venv/lib/python3.5/'},
    packages=[
        'distutils',
        'encodings',
        'importlib',
        'collections',
        'site-packages.pip',
        'site-packages.pip.req',
        'site-packages.pip.vcs',
        'site-packages.pip.utils',
        'site-packages.pip.compat',
        'site-packages.pip.models',
        'site-packages.pip._vendor',
        'site-packages.pip._vendor.idna',
        'site-packages.pip._vendor.certifi',
        'site-packages.pip._vendor.chardet',
        'site-packages.pip._vendor.chardet.cli',
        'site-packages.pip._vendor.distlib',
        'site-packages.pip._vendor.distlib._backport',
        'site-packages.pip._vendor.urllib3',
        'site-packages.pip._vendor.urllib3.util',
        'site-packages.pip._vendor.urllib3.contrib',
        'site-packages.pip._vendor.urllib3.contrib._securetransport',
        'site-packages.pip._vendor.urllib3.packages',
        'site-packages.pip._vendor.urllib3.packages.backports',
        'site-packages.pip._vendor.urllib3.packages.ssl_match_hostname',
        'site-packages.pip._vendor.colorama',
        'site-packages.pip._vendor.html5lib',
        'site-packages.pip._vendor.html5lib._trie',
        'site-packages.pip._vendor.html5lib.filters',
        'site-packages.pip._vendor.html5lib.treewalkers',
        'site-packages.pip._vendor.html5lib.treeadapters',
        'site-packages.pip._vendor.html5lib.treebuilders',
        'site-packages.pip._vendor.lockfile',
        'site-packages.pip._vendor.progress',
        'site-packages.pip._vendor.requests',
        'site-packages.pip._vendor.packaging',
        'site-packages.pip._vendor.cachecontrol',
        'site-packages.pip._vendor.cachecontrol.caches',
        'site-packages.pip._vendor.webencodings',
        'site-packages.pip._vendor.pkg_resources',
        'site-packages.pip.commands',
        'site-packages.pip.operations',
        'site-packages.wheel',
        'site-packages.wheel.tool',
        'site-packages.wheel.signatures',
        'site-packages.setuptools',
        'site-packages.setuptools.extern',
        'site-packages.setuptools._vendor',
        'site-packages.setuptools._vendor.packaging',
        'site-packages.setuptools.command',
        'site-packages.pkg_resources',
        'site-packages.pkg_resources.extern',
        'site-packages.pkg_resources._vendor',
        'site-packages.pkg_resources._vendor.packaging'],
    url='https://github.com/joseluis8906/fancychat',
    license='MIT',
    author='joseluis',
    author_email='joseluiscacere8906@gmail.com',
    description='fancy chat example',
    install_requires=[
        'pygobject',
        'paho-mqtt'
    ]
)
