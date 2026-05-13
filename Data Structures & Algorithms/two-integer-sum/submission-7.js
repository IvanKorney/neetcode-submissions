class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const smap = {}
        for(let i = 0; i < nums.length; i++){
            if(target-nums[i] in smap){
                return [smap[target-nums[i]],i]
            }else{
                smap[nums[i]] = i
            }
        }
    }
}
