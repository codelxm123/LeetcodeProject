class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if (num>=1000):
            s="M"+self.intToRoman(num-1000)
        elif (num>=100):
            if (num>=900):
                s="CM"+self.intToRoman(num-900)
            elif (num>=500):
                s="D"+self.intToRoman(num-500)
            elif (num>=400):
                s="CD"+self.intToRoman(num-400)
            else:
                s="C"+self.intToRoman(num-100)
        elif (num>=10):
            if (num>=90):
                s="XC"+self.intToRoman(num-90)
            elif (num>=50):
                s="L"+self.intToRoman(num-50)
            elif (num>=40):
                s="XL"+self.intToRoman(num-40)
            else:
                s="X"+self.intToRoman(num-10)
        else:
            if (num==9):
                s="IX"
            elif (num>=5):
                s="V"+self.intToRoman(num-5)
            elif (num==4):
                s="IV"
            elif (num>1):
                s="I"+self.intToRoman(num-1)
            elif (num==1):
                s="I"
            else:
                s=""
        return s
