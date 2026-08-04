from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words: return []
        word_len, word_cnt = len(words[0]), len(words)
        total_len = word_len * word_cnt
        word_map = Counter(words)
        res = []
        for i in range(word_len):
            left = i
            curr_map = Counter()
            count = 0
            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j:j + word_len]
                if word in word_map:
                    curr_map[word] += 1
                    count += 1
                    while curr_map[word] > word_map[word]:
                        curr_map[s[left:left + word_len]] -= 1
                        left += word_len
                        count -= 1
                    if count == word_cnt:
                        res.append(left)
                else:
                    curr_map.clear()
                    count = 0
                    left = j + word_len
        return res

        
