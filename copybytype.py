import pathlib as pl
import time, shutil

def copybytype(srcInput, destInput, typesInput):
    src = pl.Path(srcInput).rglob(typesInput)
    dest = pl.Path(destInput)
    ok = 0
    erno = 0
    for file in src:
        if not pl.Path(file).is_dir() and '__MACOSX' not in str(file):
            filename = file.name
            i = 0
            while pl.Path(str(dest) + '\\' + filename).exists():
                i-=-1
                filename = '{}_{}.{}'.format(file.stem, str(i), file.suffix)
            try:
                shutil.copy2(file, str(dest) + '\\' + filename)
                time.sleep(0.01)
                if pl.Path(str(dest) + '\\' + filename).exists():
                    print('ok:', str(file).replace(srcInput, ''))
                    ok -= -1
                else:
                    print('erno:', str(file).replace(srcInput, ''))
                    erno -= -1
            except IOError:
                print('erno:', str(file).replace(srcInput, ''))
                erno -= -1
    print('\n{} OK || {} ERNO\n'.format(ok, erno))



if __name__ == "__main__":
    src = input('Soruce Folder to Grab Files:\n')
    dest = input('\nDestination Folder:\n')
    types = input('\nFiletype: (*.png or *.*\n')

    src = src.replace('"','')
    dest = dest.replace('"','')

    print('')

    if (pl.Path(src).exists() and pl.Path(src).is_dir()) and (pl.Path(dest).exists() and pl.Path(src).is_dir()): copybytype(src, dest, types)
    else: print('Error path not found or is not a folder')
    input('Press to End...')
