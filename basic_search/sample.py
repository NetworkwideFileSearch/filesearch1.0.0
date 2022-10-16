 
import os
import time
import pandas as pd
 

class Filemanager:

    def __init__(self,path = "C:/users/hp/desktop/" ):  ## each distinct object will require path of folder whose files u wanna fetch
        self.path = path
        self.lis  = []
        self.ignore_file_dict = {'.git':0,  ## add file types that you dont want to search
                                "__pycache__":0}  


    def DFS_method(self,path):  ## use DFS recursion as folder file structure is basically a tree structure
        
        lis_of_dirs = os.listdir(path)  ## get list of files in directory

        for file in lis_of_dirs:
            if file in self.ignore_file_dict: # check if file type is to be ignored or not
                continue

            fpath = path + "/" + file

            # if  not self.is_file_accessable(fpath): ## check if file is accessible to mode like read , write
            #     continue
            
            if os.path.isdir(fpath):  ## check if path is folder
                self.DFS_method(fpath)
            
            elif os.path.isfile(fpath): ## check if path is file 
                self.get_file_metadata(fpath,filename=file)


    def is_file_accessable(self,file_path):
        if os.path.exists(file_path):
            # path exists
            if os.path.isfile(file_path): # is it a file or a dir?
                # also works when file is a link and the target is writable
                return os.access(file_path, os.R_OK)
            else:
                return False # path is a dir, so cannot write as a file
        # target does not exist, check perms on parent dir
        pdir = os.path.dirname(file_path)
        if not pdir: pdir = '.'
        # target is creatable if parent dir is writable
        return os.access(pdir, os.W_OK)


    def get_file_metadata(self, filepath,filename ):  ## it appends all metadata of a single file in lis of dictiories named as self.dic
        try:
            metadata =   {
                "file_name"    : filename.split(".")[0]   if "." in filename    else  filename,
                "file_path"    : filepath,
                'Access_time'  : time.ctime(os.path.getatime(filepath)),
                'Modified_time': time.ctime(os.path.getmtime(filepath)),
                'Change_time'  : time.ctime(os.path.getctime(filepath)),
                'Size'         : os.path.getsize(filepath) ,
                'type'         : filepath.split(".")[-1]   if "." in filepath    else  filepath
            }
            self.lis.append(metadata)
        except:
            # print(f"{filepath} is not accessible to read..")
            pass
            

    def get_df(self):   ## this method will convert lis of dictionaries (metadata ) into dataframe
        return pd.DataFrame(self.lis,columns = ["file_name","file_path",'Access_time','Modified_time','Change_time','Size','type' ])
        

if __name__ == "__main__":
    self = Filemanager(path = "C:/users/hp/downloads/")
    self.DFS_method(self.path,{})
     
