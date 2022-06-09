def largest_palindrome(string):
    def findOdd(string):
        max = 1
        total = string[0]
        for Middle in range(len(string)):
            leftBorder = Middle - 1
            rightBorder = Middle + 1
            while (leftBorder >= 0 and rightBorder < len(string) and string[leftBorder] == string[rightBorder]):
                new_str = string[leftBorder:rightBorder + 1]
                if len(new_str) > max:
                    total = new_str
                    max = len(new_str)
                leftBorder -= 1
                rightBorder += 1

        if string[-1] == string[-2] and len(string[::-1][:2]) > max:
            total = string[::-1][:2]
        elif string[-1] == string[-2] == string[-3] and len(string[::-1][:3]):
            total = string[::-1][:3]

        return total

    def findEven(string):
        max = 1
        total = string[0]
        for Middle in range(len(string)):
            leftBorder = Middle
            rightBorder = Middle + 1
            while (leftBorder >= 0 and rightBorder < len(string) and string[leftBorder] == string[rightBorder]):
                new_str = string[leftBorder:rightBorder + 1]
                if len(new_str) > max:
                    total = new_str
                    max = len(new_str)
                leftBorder -= 1
                rightBorder += 1

        if string[-1] == string[-2] and len(string[::-1][:2]) > max:
            total = string[::-1][:2]
        elif string[-1] == string[-2] == string[-3] and len(string[::-1][:3]):
            total = string[::-1][:3]
        return total

    return max([findOdd(string), findEven(string)])
