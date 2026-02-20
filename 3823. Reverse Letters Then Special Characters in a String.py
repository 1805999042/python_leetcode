
class Solution:
    def reverseByType(self, s: str) -> str:
        elements = list(s)
        elements_len = len(elements)
        left = 0
        right = elements_len - 1
        # letter first
        while left < right:
            while left < elements_len  :
                if elements[left].isalpha():
                    break
                left += 1
            while right >= 0:
                if elements[right].isalpha():
                    break
                right -= 1
            if left <= right:
                elements[left], elements[right] = elements[right], elements[left]
                left+=1
                right-=1
        left = 0
        right = elements_len - 1
        while left < right:
            while left < elements_len  :
                if not elements[left].isalpha():
                    break
                left += 1
            while right >= 0:
                if not elements[right].isalpha():
                    break
                right -= 1
            if left <= right:
                elements[left], elements[right] = elements[right], elements[left]
                left+=1
                right-=1
        return ''.join(elements)

print(Solution().reverseByType(s=")ebc#da@f("))