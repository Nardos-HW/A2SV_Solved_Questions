class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        symbol_list = { 1: ["V" , "I"], 10 : ["L" , "X"], 100 : ["D" , "C"], 1000: ["M"]}
        num_list = { 1: [5 , 1], 10 : [ 50 , 10], 100 : [ 500 , 100], 1000: [1000]}

        n = len(str(num)) 
        output = ""

        stri = str(num)

        for i in stri:

            digit = (10 ** (n-1))

            x = int(i) * digit

            if i != "4" and i != "9":

                while x > 0:

                    if x  - num_list[digit][0] < 0:

                        output += symbol_list[digit][1]

                        x -= num_list[digit][1]

                    else:

                        output += symbol_list[digit][0]
                        
                        x -= num_list[digit][0]

            else:

                if i == "4":

                    output = output + symbol_list[digit][1] + symbol_list[digit][0]
                
                elif i == "9" and digit < 100:

                    output = output + symbol_list[digit][1] + symbol_list[digit*10][1]

                elif i == "9" and digit == 100:

                    output = output + symbol_list[digit][1] + symbol_list[digit*10][0]



            n = n - 1

        
        return output

                    
                           



                        
                        
                         


        