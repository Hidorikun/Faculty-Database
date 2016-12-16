class Util(object):

    @staticmethod
    def filter(container, requirement):
        '''
        Filters the container in the following manner:
        -The elements that respect the requirement function stay
        -The rest are deleted
        :param container:
        :param requirement:
        :return: None
        '''

        i = 0
        while i < len(container):
            if not requirement(container[i]):
                del container[i]
            else:
                i += 1

    @staticmethod
    def shellSort(container, cmp):
        '''
        Sorts the ordered conainer based on the comp function
        :param container:
        :param cmp:
        :return: None
        '''

        n = len(container)
        gap = n
        while gap != 1:
            gap = gap // 2
            for i in range(n):
                j = i
                temp = container[i]
                while j >= gap and cmp(temp, container[j - gap]):
                    container[j] = container[j - gap]
                    j = j - gap
                container[j] = temp


