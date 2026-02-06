class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        directory = ""   
        file_list=[] 
        file_dict = dict() 

        for j in paths:   
            temp = j.split(" ") 
            directory = temp[0] 
            file_list = temp[1::]

            for i in file_list:

                temp = i.split("(")
                
                temp[1] = list(temp[1])
                temp[1].pop()
                temp[1] = ("").join(temp[1])
                content = temp[1]
                name = temp[0]

                if content in file_dict:

                    file_dict[content].append(directory + "/" + name)
                else:
                    empt = []
                    empt.append(directory + "/" + name)
                    file_dict[content] = empt

        return_list = []
        for i in file_dict :

            if len(file_dict[i]) > 1:
                return_list.append(file_dict[i])
        
        return return_list
            