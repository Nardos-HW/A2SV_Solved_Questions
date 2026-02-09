class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """

        add_rep = {}

        for i in cpdomains:

            lst = i.split(" ")
            countt = lst[0]
            address = lst[1]
            
            add_list = address.split(".")
            n = len(add_list)
            add = ""

            for j in range(n-1,-1,-1):

                if j != n-1:
                
                    add = add_list[j] + "." + add
                else:
                    add = add_list[j]

                if add in add_rep:
                    
                    add_rep[add] = int(add_rep[add]) + int(countt)

                else:
                    add_rep[add] = countt
                    

        output = []
        

        for key in add_rep:

            k = str(key)
            v = str(add_rep[key])
            x = v + " " + k
            output.append(x)

        return output

        