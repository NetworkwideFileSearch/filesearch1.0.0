 

class Inverted_Index( ):
    
    def __init__(self,token_dict = {}):
        self.token_dict = token_dict

    def tokenize_file_name(self,filename):
        token_list = {}
        word = ""
        for i in filename:
            if i.isalnum():
                word += i.lower()
            else:
                if word in token_list:
                    token_list[word] += 1
                else:
                    token_list[word] = 1
                word = ""
        if word in token_list:
            token_list[word] += 1
        else:
            token_list[word] = 1
        return token_list  

    def add_file_to_token_dict(self,lis,doc_id):
        for ind,token in enumerate(lis):
            token = token.lower()
            if token in self.token_dict:
                self.token_dict[token].append(doc_id)
            else:
                self.token_dict[token] = [doc_id]

    def inverting_file(self,filename,doc_id):
        token_lis = self.tokenize_file_name(filename)
        self.add_file_to_token_dict(token_lis,doc_id)

    def fetch_result(self,query ):
        query = query.lower()
        res = []
        for key in self.token_dict.keys():
            if key.startswith(query):
                res += self.token_dict[key]
        return res




if __name__ == "__main__":
    obj = Inverted_Index()
    obj.inverting_file(filename="Criminal.Justice.Episode.6.720p.moviebaba.mkv",doc_id=10)
    print(obj.token_dict)

    