
 
# from importlib import metadata
import sqlite3

class engine_db( ):
    def __init__(self,dbname = "file_Search.db"):
        self.dbname = dbname
        self.conn  =  None  
        self.cursor = None

    def connect_db(self):
        self.conn = sqlite3.connect(self.dbname) 
        self.cursor = self.conn.cursor()

    def process_query(self,query):
        # print(query)
        self.cursor.execute(query)
        self.conn.commit()

    def insert_one(self,metadata):
        self.connect_db()
        insert_query = """
                        INSERT INTO metadata  (file_name,
                                                file_type,
                                                file_size,
                                                creation_date,
                                                accessed_date,
                                                modification_date,
                                                file_location)
                        VALUES ( "{}","{}",{},"{}","{}","{}","{}" )
                        """.format( 
                                    metadata["file_name"],
                                    metadata['file_type'],
                                    metadata['file_size'],
                                    metadata['creation_date'],
                                    metadata['accessed_date'],
                                    metadata['modification_date'],
                                    metadata['file_location']
                                )
        self.process_query(insert_query)
        self.cursor.close()
        self.conn.close()


    def search_filename(self,query = ""):
        self.connect_db()
        search_query = f"""
                            select * from metadata where file_name like '%{query}%'
                        """
        self.process_query(search_query)
        res = self.cursor.fetchall()
        self.cursor.close()
        self.conn.close()
        return res

    
if __name__ == "__main__":
    # metadatai =   {
    #                 "file_name"    :  "kk", 
    #                 "file_location"    : "h",
    #                 'modification_date':  "kg",
    #                 'creation_date'  :  "mb",
    #                 "accessed_date":"mb",
    #                 'file_size'         :  0,
    #                 'file_type'         : "folder"
    #             }
    obj = engine_db()
    # obj.insert_one(metadatai)
    print(obj.search_filename("samp"))
    



