import PyInstaller.__main__

PyInstaller.__main__.run([
    'People Map.pyw',
    r'--icon=C:\Users\Camilo\Downloads\12. People Map\Recursos\Imagenes\Logo-Banco.ico',
    r'--splash=C:\Users\Camilo\Downloads\12. People Map\Recursos\Imagenes\splash2.jpg',
    '--noconsole',
    r'--hidden-import=pandas',
    r'--hidden-import=pil'
])

