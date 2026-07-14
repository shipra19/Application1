import FreeSimpleGUI as a
import zipfile
from zip_creator import make_archive

label1=a.Text("Select files to compress")
input1=a.Input()
button1=a.FilesBrowse("Upload", key="Files")

label2=a.Text("Select destination folder")
input2=a.Input()
input2=a.Input()
button2=a.FolderBrowse("Choose",key="Folder")

compress_button=a.Button("Compress")
output_label=a.Text(key="Output")

window1=a.Window("File Compressor",
                 layout=[[label1,input1,button1],
                         [label2,input2,button2],
                         [compress_button],[output_label] ])

while True:
    event, values = window1.Read()
    print(event,values)
    filepath=values["Files"].split(";")
    folder=values["Folder"]
    make_archive(filepath,folder)
    window1["Output"].update(value="Compression Completed!")




window1.read()
window1.close()

