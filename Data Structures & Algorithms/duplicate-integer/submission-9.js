class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const numset = new Set()
        for(const num of nums){
            if(numset.has(num)){
                return true;
            }
            numset.add(num)
        }
        return false
    }
}
