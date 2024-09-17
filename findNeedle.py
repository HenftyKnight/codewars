
def findNeedle(haystack):
    key = "needle"
    for junk in range(len(haystack)-1):
        if haystack[junk] ==  key:
            return f'found the needle at position {junk}'
                     
# Best Solution
def findNeedle(haystack):
    return f'found the needle at position {haystack.index('needle')}'

haystack = ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]
print(findNeedle(haystack))

"""
Time and Space Complexity for both solutions
O(n) and O(1) respecrtively.

Index method under the hood uses iteration just like the normal above 
function to find the needle in the haystack.
"""

