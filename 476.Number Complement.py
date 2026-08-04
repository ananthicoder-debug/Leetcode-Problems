class Solution:
    def findComplement(self, num: int) -> int:
        l = list()
        
        # Fix 1: Update 'num' inside the loop to avoid infinite loop
        while num > 0:
            r = num % 2
            l.append(r)
            num = num // 2  # This safely reduces num down to 0
            
        # Reverse the list to get the correct binary order
        m = l[::-1]
        
        # Fix 2: Use range(len(m)) to safely modify values by index
        for i in range(len(m)):
            if m[i] == 0:
                m[i] = 1
            else:
                m[i] = 0
        
        # Fix 3: Initialize 'h', reverse 'm', and sum up properly
        n = m[::-1]
        h = 0  # Define h before using +=
        for i in range(len(n)):
            h += n[i] * (2 ** i)  # Read from list 'n' instead of 'a'
            
        return h
