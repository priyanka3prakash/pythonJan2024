import zipfile

with open("tmp1.zip", "wb") as outfile:
    with zipfile.ZipFile(outfile, mode="w", compression=zipfile.ZIP_DEFLATED) as zfile:
        zfile.writestr("entry1.txt", "my heroes have always been cowboys")
        zfile.writestr("entry2.tsf", "and they still are it seems")
        zfile.writestr("entry3.csv", "sadly, in, search, of, and")
        
        zfile.writestr("entry4", "on step in back of")
        zfile.writestr('entry4', 'is is another line')
        # UserWarning: Duplicate name: 'entry4'

        zfile.writestr("entry5", "themselves and their slow moving ways")
        zfile.close()
    outfile.close()


# unzip -l tmp1.zip