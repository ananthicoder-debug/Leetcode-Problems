import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);
        for (int i = 0; i < nums.length - 2; i++) {
            // Skip the same element to avoid duplicate triplets
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            // If the smallest number is greater than 0, 
            // no three numbers can sum up to 0
            if (nums[i] > 0) {
                break;
            }
            int left = i + 1;
            int right = nums.length - 1;
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                
                if (sum == 0) {
                    result.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    
                    // Skip duplicate values for the left pointer
                    while (left < right && nums[left] == nums[left + 1]) {
                        left++;
                    }
                    // Skip duplicate values for the right pointer
                    while (left < right && nums[right] == nums[right - 1]) {
                        right--;
                    }                    
                    left++;
                    right--;
                } else if (sum < 0) {
                    left++; // Sum is too small, move left pointer rightward
                } else {
                    right--; // Sum is too large, move right pointer leftward
                }
            }
        }
        
        return result;
    }
}
