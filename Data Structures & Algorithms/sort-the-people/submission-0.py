class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Pair names with heights
        people = list(zip(names, heights))
        
        # Sort by height descending
        people.sort(key=lambda x: x[1], reverse=True)
        
        # Extract names in sorted order
        return [name for name, _ in people]
