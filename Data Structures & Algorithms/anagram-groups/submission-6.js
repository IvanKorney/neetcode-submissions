class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const res = {}
        for(const s of strs){
            const sorted_s = s.split('').sort().join();
            if(!res[sorted_s]){
                res[sorted_s] = []
            }
            res[sorted_s].push(s)
        }

        return Object.values(res)
    }
}
