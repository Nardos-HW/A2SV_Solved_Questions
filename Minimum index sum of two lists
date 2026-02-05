class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        my_list = []
        mini = 2001

        for i in range(len(list1)):

            if list1[i] in list2:

                x = i + list2.index(list1[i])

                if x < mini:
                    my_list = []
                    my_list.append(list1[i])
                    mini = x
                elif x == mini:
                    my_list.append(list1[i])
                else:
                    continue

        return my_list
                


