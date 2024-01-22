class Solution {
    public String solution(int a, int b) {
        int year = 2016;
        int month = a;
        int day = b;

        int date = calculateDayOfWeek(year, month, day);
        return getDayOfWeekName(date);
    }
    
    public static int calculateDayOfWeek(int year, int month, int day) {
        if (month < 3) {
            month += 12;
            year--;
        }

        int k = year % 100;
        int j = year / 100;

        int dayOfWeek = (day + ((13 * (month + 1)) / 5) + k + (k / 4) + (j / 4) - (2 * j)) % 7;

        if (dayOfWeek < 0) {
            dayOfWeek += 7;
        }

        return dayOfWeek;
    }
    
    public static String getDayOfWeekName(int dayOfWeek) {
        String[] dayOfWeekNames = {"SAT", "SUN", "MON", "TUE", "WED", "THU", "FRI"};
        return dayOfWeekNames[dayOfWeek];
    }
}