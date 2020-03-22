class mod():
    def __init__(self,baseDir,modDir):
        self.baseDir = baseDir
        self.modDir = modDir
    def mod_extract(self):
        import zipfile
        unzip = zipfile.ZipFile(self.baseDir,"r")
        PermissionError: "We do not have permission to do that."
        #try:
        #    print("An error occoured")
        unzip.extractall(modDir)
        PermissionError: "We do not have permission to do that."
        #try:
        #    print("An error occoured")
        del unzip