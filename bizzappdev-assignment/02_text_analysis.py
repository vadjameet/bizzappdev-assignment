"""
Problem: Text Analysis with Constraints
Approach: Use dictionary for frequency counting, trie for prefix queries.
Optimize with pre-processing and sorted lists.
"""
import re
from collections import defaultdict

class TextAnalyzer:
    def __init__(self, text):
        self.stop_words = {'the', 'is', 'at', 'on', 'in', 'and', 'a', 'an'}
        self.word_freq = defaultdict(int)
        self.prefix_map = defaultdict(list)
        
        words = re.findall(r'\b\w+\b', text.lower())
        for word in words:
            if word not in self.stop_words:
                self.word_freq[word] += 1
                
        # Build prefix map
        for word in self.word_freq:
            for i in range(1, len(word)+1):
                self.prefix_map[word[:i]].append(word)
        
    def top_prefix_words(self, prefix, k):
        candidates = self.prefix_map.get(prefix, [])
        sorted_words = sorted(candidates, key=lambda x: (-self.word_freq[x], x))
        return sorted_words[:k]

# Example usage:
if __name__ == "__main__":
    text = "The cat is on the mat. The cat and the mat are on the floor."
    analyzer = TextAnalyzer(text)
    print("Top 3 words starting with 'th':", analyzer.top_prefix_words('th', 3))