# rather than writing my code per normal intuition/practice, I'm studying this solution presented (among others) that is written very differently from my style.
# note the lack of for loops, the while loop used, and the use of dict for memory storage/recall

def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        dict = {}

        i,j = 0,0
        n = len(s)

        while(j < n):
            c = s[j]     
            
            dict[c] = 1 if not c in dict else dict[c] + 1
            
            
            if dict[c] > 1:
                while(dict[c] > 1):
                    dict[s[i]] -= 1
                    i += 1
                    
            maxLength = max(maxLength, j - i + 1)
            j += 1

        return maxLength