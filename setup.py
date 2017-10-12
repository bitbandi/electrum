#!/usr/bin/env python2

# python setup.py sdist --format=zip,gztar

from setuptools import setup
import os
import sys
import platform
import imp
import argparse

version = imp.load_source('version', 'lib/version.py')

if sys.version_info[:3] < (2, 7, 0):
    sys.exit("Error: Electrum requires Python version >= 2.7.0...")

data_files = []

if platform.system() in ['Linux', 'FreeBSD', 'DragonFly']:
    parser = argparse.ArgumentParser()
    parser.add_argument('--root=', dest='root_path', metavar='dir', default='/')
    opts, _ = parser.parse_known_args(sys.argv[1:])
    usr_share = os.path.join(sys.prefix, "share")
    if not os.access(opts.root_path + usr_share, os.W_OK) and \
       not os.access(opts.root_path, os.W_OK):
        if 'XDG_DATA_HOME' in os.environ.keys():
            usr_share = os.environ['XDG_DATA_HOME']
        else:
            usr_share = os.path.expanduser('~/.local/share')
    data_files += [
        (os.path.join(usr_share, 'applications/'), ['electrum-dmd.desktop']),
        (os.path.join(usr_share, 'pixmaps/'), ['icons/electrum-dmd.png'])
    ]

setup(
    name="Electrum-DMD",
    version=version.ELECTRUM_VERSION,
    install_requires=[
        'pyaes',
        'ecdsa>=0.9',
        'pbkdf2',
        'requests',
        'qrcode',
        'protobuf',
        'dnspython',
        'jsonrpclib',
        'PySocks>=1.6.6',
    ],
    packages=[
        'electrum_dmd',
        'electrum_dmd_gui',
        'electrum_dmd_gui.qt',
        'electrum_dmd_plugins',
        'electrum_dmd_plugins.audio_modem',
        'electrum_dmd_plugins.cosigner_pool',
        'electrum_dmd_plugins.email_requests',
        'electrum_dmd_plugins.greenaddress_instant',
        'electrum_dmd_plugins.hw_wallet',
        'electrum_dmd_plugins.keepkey',
        'electrum_dmd_plugins.labels',
        'electrum_dmd_plugins.ledger',
        'electrum_dmd_plugins.trezor',
        'electrum_dmd_plugins.digitalbitbox',
        'electrum_dmd_plugins.trustedcoin',
        'electrum_dmd_plugins.virtualkeyboard',
    ],
    package_dir={
        'electrum_dmd': 'lib',
        'electrum_dmd_gui': 'gui',
        'electrum_dmd_plugins': 'plugins',
    },
    package_data={
        'electrum_dmd': [
            'currencies.json',
            'www/index.html',
            'wordlist/*.txt',
            'locale/*/LC_MESSAGES/electrum.mo',
        ]
    },
    scripts=['electrum-dmd'],
    data_files=data_files,
    description="Lightweight Diamond Wallet",
    author="Thomas Voegtlin",
    author_email="thomasv@electrum.org",
    license="MIT Licence",
    url="https://electrum-dmd.org",
    long_description="""Lightweight Diamond Wallet"""
)
