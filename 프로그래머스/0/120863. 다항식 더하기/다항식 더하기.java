class Solution {
    public String solution(String polynomial) {
        int coef = 0;     
        int constant = 0; 

        String[] terms = polynomial.split(" \\+ ");
        for (String term : terms) {
            if (term.contains("x")) {
                if (term.equals("x")) {
                    coef += 1;
                } else {
                    coef += Integer.parseInt(term.replace("x", "")); // 예: "3x" -> 3
                }
            } else {
                constant += Integer.parseInt(term);
            }
        }

        StringBuilder sb = new StringBuilder();

        if (coef != 0) {
            if (coef == 1) sb.append("x");
            else sb.append(coef).append("x");
        }

        if (constant != 0) {
            if (sb.length() > 0) sb.append(" + ");
            sb.append(constant);
        }

        return sb.toString();
    }
}
