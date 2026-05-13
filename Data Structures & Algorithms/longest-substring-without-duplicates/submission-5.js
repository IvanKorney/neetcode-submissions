class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        let res = 0;
        const sset = {}
        let l = 0;
        let r = 0;
        while(r < s.length){
            sset[s[r]] = (sset[s[r]]||0)+1
            while(sset[s[r]] > 1){
                sset[s[l]] -= 1
                l += 1
            }
            res = Math.max(res,r-l+1)
            r += 1
        }
        return res
    }
}
