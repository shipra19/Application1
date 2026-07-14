import zipfile
import pathlib

def make_archive(filepaths, dest_folder):
    dest_folder=pathlib.Path(dest_folder,"compressed.zip")
    with zipfile.ZipFile(dest_folder,"w") as archive:
        for i in filepaths:
            i=pathlib.Path(i)
            archive.write(i,arcname=i.name)

if __name__=="__main__":
    make_archive(filepaths=["functions.py", "todos.txt"], dest_folder="Compress_Dest")