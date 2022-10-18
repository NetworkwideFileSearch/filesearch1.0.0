

from   basic_search.search import Filemanager
from   basic_search.queryDB import engine_db as edb


class Fusion:
    def __init__(self):
        self.edb = edb() 
        self.fmng = None

    # def invert_every_file(s):
    #     for i in s.fmng.db.iloc[:,:].index:
    #         s.inv_ind.inverting_file( s.fmng.db.loc[i,"file_name"] , s.fmng.db.loc[i,"id"]  )

    def index_files(self,path = "c:/users/hp/desktop" ):
        self.fmng = Filemanager( path )
        self.fmng.DFS_method(path)

    def print_result(self,query ):  
        try:          
            # result_set = s.inv_ind.fetch_result(query)
            print("----------------------requiresd files-------------------")
            for ind,row in enumerate(self.edb.search_filename(query)):
                print( ind ,"=>", row[-2] )
            print("--------------------------------------------------------")
        except:
            print(f"no file named as {query}")


    # def total_index_creation(s,path):
    #     s.fmng = Filemanager(path)
    #     s.fmng.process()
    #     return 1

    def run_search_demo(self):
        print("welcome to file search v1.0.0..")
        inp = input("\nchoose any of the following action:\n1.add folder path\n2.search\n3.end\n")
        while 1:
            if inp == "1":
                path = input("\nenter your folder path: ")
                self.index_files(path)
                print("\nindex creation successful .. :)")
            elif inp == "2":
                query = input("\nenter the search query: ")
                self.print_result(query)
            elif inp == "3":
                print("\nthank you ....*/-\*")
                break 
            
            inp = input("\nchoose any of the following action:\n1.add folder path\n2.search\n3.end\n")
    
if __name__ == "__main__":
    obj = Fusion()
    obj.run_search_demo()
    
     

