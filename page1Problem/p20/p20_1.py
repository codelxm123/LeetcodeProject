class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        m_dict={')':'(',']':'[','}':'{'}
        m_stack=[]
        n=len(s)
        for i in range(n):
            if s[i] in ['(','[','{']:
                m_stack.append(s[i])
            else:
                if len(m_stack)==0:
                    return False
                if not m_stack[-1]==m_dict[s[i]]:
                    return False
                m_stack.pop()
        if len(m_stack)==0:
            return True
        else:
            return False
