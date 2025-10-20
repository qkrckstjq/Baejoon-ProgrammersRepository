class Solution {
    public int solution(int chicken) {
        return dfs(chicken);
    }
    
    public int dfs(int chicken) {
        if(chicken < 10) return 0;
        int num = chicken / 10;
        int last = chicken % 10;
        int sum = num + last;
        return num + dfs(sum);
    }
}