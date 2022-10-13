# Time complexity : O(n^k)
# Space complexity : O(n^k)
# Leetcode : Solved and submitted

class Solution:
    def expand(self, s: str) -> List[str]:
        # find the len of the string and declare the default values
        self.res = []
        n = len(s)
        i = 0
        blocks = []
        
        # we need to build the blocks first for each char without {} and one group for chars within {}
        while i < n:
            ch = s[i]
            block = []
            
            # if we encounter an opening brace
            if ch == '{':
                i += 1
                # until we reach the closing brace
                while s[i] != '}':
                    # add all the chars in a block except the ,
                    if s[i] != ',':
                        block.append(s[i])
                    i += 1
            else:
                # if it's just a char, then simply append to the block list
                block.append(ch)
            i += 1
            
            # sort the block and append to the blocks group that we are creating
            block.sort()
            blocks.append(block)
            
        # we call the backtrack function to find all the possible cases
        self.backtrack(blocks, 0, '')
        
        # return the final resultant list
        return self.res
        
    def backtrack(self, blocks, idx, st):
        # base
        # if we have reached the max chars we need which is the length of blocks, then append the string to the res and return
        if idx == len(blocks):
            self.res.append(st[:])
            return
            
        # logic
        # find the block according to the idx
        block = blocks[idx]
        
        # do a for loop recursion on the current block at hand
        for i in range(len(block)):
            c = block[i]
            
            # action
            # add the current char to string
            st += c
                
            # recurse
            # call the recursive function with new index from next block
            self.backtrack(blocks, idx + 1, st)
                
            # backtrack
            # remove the lastly added char
            st = st[:-1]
