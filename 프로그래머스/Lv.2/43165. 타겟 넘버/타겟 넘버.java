import java.util.Stack;
import java.util.HashMap;
import java.util.Map;


class Solution {
    public int solution(int[] numbers, int target) {
        return dfs(0, numbers[0]*-1, numbers, target) + dfs(0, numbers[0], numbers, target);        
    }
    
    public int dfs(int index, int value,int[] numbers,int target) {
        if(index == numbers.length-1) {
            return value == target ? 1 : 0;
        } else {
            return dfs(index+1, value+numbers[index+1], numbers, target) + 
                    dfs(index+1, value-numbers[index+1], numbers, target);
        }
    }
}

// public int solution(int[] numbers, int target) {
//         int answer = 0;
//         Stack<Integer[]> stack = new Stack<>();
//         Integer[] tempPlus = {0, numbers[0]};
//         Integer[] tempMinus = {0, numbers[0]*-1};
//         stack.push(tempPlus);
//         stack.push(tempMinus);
        
//         while(!stack.isEmpty()) {
//             Integer[] popped = stack.pop();
//             int index = popped[0];
//             int value = popped[1];
//             if(index == numbers.length-1) {
//                 answer += value == target ? 1 : 0;
//             } else {
//                 Integer[] temp1 = {index+1, value+numbers[index+1]};
//                 Integer[] temp2 = {index+1, value-numbers[index+1]};
//                 stack.push(temp1);
//                 stack.push(temp2);
//             }
//         }
//         return answer;                
//     }

