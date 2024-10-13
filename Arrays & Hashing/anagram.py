class anagram:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted (t)

if __name__ == "__main__":
    solution = anagram()
    print(solution.isAnagram("monkey", "keymon"))