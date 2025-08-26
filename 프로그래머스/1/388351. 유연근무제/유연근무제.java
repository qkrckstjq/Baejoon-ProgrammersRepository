class Solution {
    public int toMin(int sch) {
        int hour = sch / 100;
        int minute = sch % 100;
        return (hour * 60 + minute);
    }
    
    public int solution(int[] schedules, int[][] timelogs, int startday) {
        int answer = 0;
        for(int i = 0; i < schedules.length; i++) {
            boolean safe = true;
            int[] curTimes = timelogs[i];
            int start = startday;
            int cutLine = (toMin(schedules[i]) + 10) % 1440;
            
            for(int d = 0; d < 7; d++) {
                if (start > 7) {
                    start -= 7;
                }
                // System.out.println(start);
                // System.out.println(curTimes[d]);
                
                if(start == 6 || start == 7) {
                    start += 1;
                    continue;
                }
                
                int curTime = toMin(curTimes[d]);
                if(cutLine < curTime) {
                    safe = false;
                    break;
                }
                start += 1;
            }
            if(safe == false) {
                continue;
            } else {
                answer += 1;
            }
        }
        
        return answer;
    }
}