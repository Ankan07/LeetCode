from typing import Any, List 
import math

class Solution:
    def __init__(self) -> None:
        pass
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        firstList.sort()
        secondList.sort()
        first_length = len(firstList)
        second_length = len(secondList)
        i = 0
        j = 0
        result = []
        while i < first_length and j< second_length:
            result.append(self.find_interval(firstList[i],secondList[j]))
            j=j+1 if firstList[i][1] >= secondList[j][1] else i=i+1
        return result 

    def find_interval(self,first,second) -> List[int]:
        a = -math.inf
        b = +math.inf
        if first[0] >= second[0]:
            a = first[0]
        else:
            a = second[0]
        if first[1] <= second[1]:
            b = first[1]
        else:
            b = second[1]

        if a<=b:
          return [a,b]
        else:
          return[]
