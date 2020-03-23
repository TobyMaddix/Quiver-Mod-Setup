class mod():
    def __init__(self,baseDir,modDir):#where the base files are, where to copy them to
        self.baseDir = baseDir
        self.modDir = modDir
        print(self.baseDir)
        print(self.modDir)
    #extracts the mod files to the required location
    def mod_extract(self):
        import zipfile
        import os
        if (not os.path.exists(self.modDir)):
            os.makedirs(self.modDir)
        unzip = zipfile.ZipFile(self.baseDir, "r")
        unzip.printdir()
        unzip.extractall(self.modDir)
        del unzip
    def mod_link(self):
        import os
        link = os
        os.symlink()