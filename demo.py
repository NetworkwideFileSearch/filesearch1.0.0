

from basic_search.search import Filemanager
from  basic_search.inverted_index import Inverted_Index


class Fusion:
    def __init__(s):
        s.inv_ind = None
        s.fmng = None

    def invert_every_file(s):
        for i in s.fmng.db.iloc[:,:].index:
            s.inv_ind.inverting_file( s.fmng.db.loc[i,"file_name"] , s.fmng.db.loc[i,"id"]  )


    def print_result(s,query ):  
        try:          
            result_set = s.inv_ind.fetch_result(query)
            for i in result_set:
                print( s.fmng.db.loc[i,'file_path'])
        except:
            print(f"no file named as {query}")


    def total_index_creation(s,path):
        s.fmng = Filemanager(path)
        s.fmng.process()
        return 1

    def run_search_demo(s):
        print("welcome to file search v1.0.0..")
        inp = input("\nchoose any of the following action:\n1.add folder path\n2.search\n3.end\n")
        while 1:
            if inp == "1":
                path = input("\nenter your folder path: ")
                s.total_index_creation(path)
                s.inv_ind = Inverted_Index()
                s.invert_every_file()
                print("\nindex creation successful .. :)")
            elif inp == "2":
                query = input("\nenter the search query: ")
                s.print_result(query)
            elif inp == "3":
                print("\nthank you ....*/-\*")
                break 
            
            inp = input("\nchoose any of the following action:\n1.add folder path\n2.search\n3.end\n")
    
if __name__ == "__main__":
    obj = Fusion()
    obj.run_search_demo()
    
     

