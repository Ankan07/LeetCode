import string
class Solution(object):

    def __init__(self):
        self.hash = {}
        self.main_hash = {}
        for letter in string.ascii_lowercase:
            self.hash[letter] = 0
            self.main_hash [letter] = 0

    def findAnagrams(self, s, p):
        start_index = 0
        length = len(p)
        end_index = start_index + length-1
        array = []
        self.make_hash(p[0:len(p)])
        self.make_first_hash(s[start_index:end_index+1])
        if self.checkanagram() == True:
                array.append(0)
        for i in range(1,len(s)-length+1):
            self.make_hash_for_one_movement(s[start_index],'start')
            start_index+=1
            end_index+=1
            if end_index <= len(s)-1:
                self.make_hash_for_one_movement(s[end_index],'end')
            if self.checkanagram() == True:
                array.append(i)        
        return array
    def checkanagram (self):
        if self.hash == self.main_hash:
          return True
        else:
          return False      
    def make_hash (self,s):
        for i in range(len(s)):
                self.main_hash[s[i]]+= 1
    def make_first_hash(self,s):
         for i in range(len(s)):
                self.hash[s[i]]+= 1

    def make_hash_for_one_movement(self,char,type):
        if  type == 'start':
            self.hash[char] -= 1
        if type == 'end':
             self.hash[char] += 1
      

        
            


print(Solution().findAnagrams("abab","ab"))
