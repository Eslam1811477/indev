# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['indev.py'],
    pathex=[],
    binaries=[],
    datas=[('C:\\\\Users\\\\eslam\\\\AppData\\\\Local\\\\Packages\\\\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\\\\LocalCache\\\\local-packages\\\\Python312\\\\site-packages\\\\pyfiglet/fonts', 'pyfiglet/fonts')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='indev',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['ex.ico'],
)
