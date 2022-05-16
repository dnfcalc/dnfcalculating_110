# -*- mode: python ; coding: utf-8 -*-

import os

# -*- spec_root = os.path.abspath(os.path.join(SPECPATH, '../../')) -*-

spec_root = os.path.abspath(SPECPATH)

print(spec_root)

hideList = ['uvicorn.lifespan.off','uvicorn.lifespan.on','uvicorn.lifespan',
'uvicorn.protocols.websockets.auto','uvicorn.protocols.websockets.wsproto_impl',
'uvicorn.protocols.websockets_impl','uvicorn.protocols.http.auto',
'uvicorn.protocols.http.h11_impl','uvicorn.protocols.http.httptools_impl',
'uvicorn.protocols.websockets','uvicorn.protocols.http','uvicorn.protocols',
'uvicorn.loops.auto','uvicorn.loops.asyncio','uvicorn.loops.uvloop','uvicorn.loops',
'uvicorn.logging']
for fileName in os.listdir(r'./core/characters/'):
    if fileName.endswith(".py") and fileName!="__init__.py":
        hideList.append("core.characters."+fileName.replace(".py",""))

block_cipher = None

a = Analysis(['main.py'],
             pathex=[spec_root],
             binaries=[],
             hiddenimports=hideList,
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
