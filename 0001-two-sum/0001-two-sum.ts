function twoSum(nums: number[], target: number): number[] {
     const hashMap: Map<number,number> = new Map();
    
    for(var i = 0; i < nums.length; i++){
        if (hashMap.get(target - nums[i]) != undefined){
            return [hashMap.get(target - nums[i]), i]
        }
        
        hashMap.set(nums[i], i)
    }
    
};