"""The binary search algorithm"""

class BinarySearch:
    """Binary search"""

    @staticmethod
    def search(item: int, elements: list[int]) -> int | None:
        low: int = 0
        high: int = len(elements) - 1
        iteration: int = 0
        
        while low <= high:
            iteration += 1
            mid: int = (low + high) // 2
            guess: int = elements[mid]
            if guess == item:
                print(f"Number of iterations: {iteration}")
                return mid
            elif guess > item:
                high = mid - 1
            else:
                low = mid + 1
        return None
           
from math import log2
print(int(log2(1_000_000_000))) 
# result: int | None = BinarySearch.search(item=127 * 2, elements=[name for name in range(128 * 2)])
# print(result)