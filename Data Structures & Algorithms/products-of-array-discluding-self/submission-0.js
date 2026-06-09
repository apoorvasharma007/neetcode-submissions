class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {

        let ans = new Array(nums.length);
        let product = 1;
        let zeroCnt = 0;

        for (let i=0; i<nums.length; i++){
            if(nums[i]!==0){
                product *= nums[i];

            }else{
                zeroCnt++;
            }
        }

        if(zeroCnt>1){
            return Array(nums.length).fill(0);
        }

        for (let i=0; i<nums.length; i++){
            if(zeroCnt>0){
                ans[i] = nums[i] === 0? product : 0;
            }else{
                ans[i] = product/ nums[i]
            }
        }
        return ans;

    }
}
