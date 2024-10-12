class ContainsDuplicate:
    def hasDuplicate(self, nums: list[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

if __name__ == "__main__":
    solution = ContainsDuplicate()

    # Test cases
    t1 = [1, 2, 3, 5]  # Expected output: False
    t2 = [1, 2, 3, 1]  # Expected output: True

    print(f"Test Case 1: {solution.hasDuplicate(t1)}")  # Output: False
    print(f"Test Case 2: {solution.hasDuplicate(t2)}")  # Output: True
