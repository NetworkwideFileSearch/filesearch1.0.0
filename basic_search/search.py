 

from logging import error
import os
import time
# import pandas as pd
from  basic_search.queryDB import engine_db as mtd




class Filemanager:

    def __init__(self,path = "C:/users/hp/desktop/" ):  ## each distinct object will require path of folder whose files u wanna fetch
        self.path = path
        self.lis  = []
        self.db   = None
        self.mtd = mtd()
        self.ignore_file_dict = {'.git':0,  ## add file types that you dont want to search
                                "__pycache__":0}  


    def get_list_of_files(self,folder_path):
        try:
            return os.listdir(folder_path)
        except:
            return -1



    def DFS_method(self,path):  ## use DFS recursion as folder file structure is basically a tree structure
        
        lis_of_dirs = self.get_list_of_files(path)  ## get list of files in directory
        if lis_of_dirs != -1:
            for file in lis_of_dirs:
                if file in self.ignore_file_dict: # check if file type is to be ignored or not
                    continue

                fpath = path + "/" + file

                # if  not self.is_file_accessable(fpath): ## check if file is accessible to mode like read , write
                #     continue
                
                if os.path.isdir(fpath):  ## check if path is folder
                    self.get_folder_metadata(fpath,foldername=file)
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



    def get_folder_metadata(self, folderpath,foldername ):  ## it appends all metadata of a single file in lis of dictiories named as self.dic
        # try:
        metadata =   {
            "file_name"         : foldername, 
            "file_location"     : folderpath,
            "accessed_date"     : time.ctime(os.path.getatime(folderpath)),
            'modification_date' : time.ctime(os.path.getmtime(folderpath)),
            'creation_date'     : time.ctime(os.path.getctime(folderpath)),
            'file_size'         : os.path.getsize(folderpath),
            'file_type'         : "folder"
        }
        # self.lis.append(metadata)
            
        # except error:
        #     print(error)
        #     pass
        self.mtd.insert_one(metadata)


    def get_file_metadata(self, filepath,filename ):  ## it appends all metadata of a single file in lis of dictiories named as self.dic
        # try:
        metadata =   {
            "file_name"              : filename ,#.split(".")[0]   if "." in filename    else  filename,
            "file_location"          : filepath,
            "accessed_date"          :time.ctime(os.path.getatime(filepath)),
            'modification_date'      : time.ctime(os.path.getmtime(filepath)),
            'creation_date'          : time.ctime(os.path.getctime(filepath)),
            'file_size'              : os.path.getsize(filepath) ,
            'file_type'              : filepath.split(".")[-1]   if "." in filepath    else  filepath
        }
        # self.lis.append(metadata)
            
             
        # except error:
        #     # print(f"{filepath} is not accessible to read..")
        #     print(error)
        #     pass
        self.mtd.insert_one(metadata)
            

    # def get_df(self):   ## this method will convert lis of dictionaries (metadata ) into dataframe
    #     return pd.DataFrame(self.lis,columns = ["file_name","file_location",'accessed_date','modification_date',
    #                                             'creation_date','file_size','file_type' ])
        

    def process(self):  
        self.DFS_method(self.path)
        # self.db = self.get_df()
        # self.db['file_name_lower'] = self.db['file_name'].str.lower()
        # self.db['id'] = self.db.index


    # def search_query(self,query):
    #     return self.db[self.db['file_name_lower'].str.contains(query)].iloc[:,:-1].sort_values(['Modified_time'],ascending=False)



 
if __name__ == "__main__":
    self = Filemanager(path = "c:/users/hp/desktop")
    self.DFS_method(self.path)
    
        
