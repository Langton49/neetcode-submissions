class Solution:
    def simplifyPath(self, path: str) -> str:
        # paths are separated by '/' and the split function can be used to get all individual path labels
        # Using the split path we can build a stack where we only push the path labels
        # If we get any of the reference directories '.' or '..' we should do nothing and or pop the last directory to      simulate going up to the previous directory respectively
        # Time complexity: O(n) each directory is pushed and/or popped at most twice where n is the number of directories in that path
        # Space complexity: O(n) extra memory is needed to store both the stack and the split paths

        split_paths = path.split('/')
        joined_paths = []
        for path in split_paths:
            if not path or path == '.':
                continue
            
            if path == '..':
                if joined_paths:
                    joined_paths.pop()
                continue
            joined_paths.append(path)
        return f"/{"/".join(joined_paths)}"

