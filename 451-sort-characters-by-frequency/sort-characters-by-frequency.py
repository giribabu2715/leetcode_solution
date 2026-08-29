class Solution:
    def frequencySort(self, s):
        freq = {}

        # Count frequency
        for ch in s:
            if ch not in freq:
                freq[ch] = 0
            freq[ch] += 1

        # Sort characters by frequency
        chars = sorted(freq, key=freq.get, reverse=True)

        # Build answer
        result = ""

        for ch in chars:
            result += ch * freq[ch]

        return result
        