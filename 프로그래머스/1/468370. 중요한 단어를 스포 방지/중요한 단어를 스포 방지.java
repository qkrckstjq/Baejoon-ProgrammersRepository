import java.util.*;

class Solution {

    public int solution(String message, int[][] spoiler_ranges) {
        int answer = 0;

        Set<String> normalWords = new HashSet<>();
        Set<String> revealed = new HashSet<>();

        boolean[] spoiler = new boolean[message.length()];

        for(int[] range : spoiler_ranges) {
            for(int i = range[0]; i <= range[1]; i++) {
                spoiler[i] = true;
            }
        }

        List<Word> words = parseWords(message);

        for(Word w : words) {
            boolean isSpoiler = false;

            for(int i = w.start; i <= w.end; i++) {
                if(spoiler[i]) {
                    isSpoiler = true;
                    break;
                }
            }

            if(!isSpoiler) {
                normalWords.add(w.word);
            }
        }

        for(int[] range : spoiler_ranges) {

            List<Word> current = getWordsInRange(range, words);

            for(Word w : current) {

                if(normalWords.contains(w.word)) {
                    continue;
                }

                if(revealed.contains(w.word)) {
                    continue;
                }

                answer++;
                revealed.add(w.word);
            }
        }

        return answer;
    }

    public static List<Word> getWordsInRange(int[] range, List<Word> words) {

        List<Word> result = new ArrayList<>();

        int start = range[0];
        int end = range[1];

        for(Word w : words) {

            if(w.end < start) {
                continue;
            }

            if(w.start > end) {
                break;
            }

            result.add(w);
        }

        return result;
    }

    public static List<Word> parseWords(String message) {

        List<Word> result = new ArrayList<>();

        int start = 0;

        for(int i = 0; i <= message.length(); i++) {

            if(i == message.length() || message.charAt(i) == ' ') {

                String word = message.substring(start, i);

                result.add(new Word(word, start, i - 1));

                start = i + 1;
            }
        }

        return result;
    }

    static class Word {
        String word;
        int start;
        int end;

        Word(String word, int start, int end) {
            this.word = word;
            this.start = start;
            this.end = end;
        }
    }
}