def uniqueOccurrences(arr):
        freq = {}

        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        seen_freqs = set()
    
        for count in freq.values():
            if count in seen_freqs:
                return False
            seen_freqs.add(count)

        return True
        
arr = [1, 2, 2, 1, 3]
print(uniqueOccurrences(arr)) # False