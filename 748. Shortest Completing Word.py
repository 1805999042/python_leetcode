from typing import List
from collections import Counter
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        lower_list = []  # lower_list: []
        for ch in licensePlate:  # ch: '1' -> 's' -> '3' -> ' ' -> 'P' -> 'S' -> 't'
            if ch.isalpha():  # ch: 's','P','S','t'
                lower_list.append(ch.lower())  # lower_list: ['s'] -> ['s','p'] -> ['s','p','s'] -> ['s','p','s','t']
        need = Counter(lower_list)  # need: {'s': 2, 'p': 1, 't': 1}
        ans = ""  # ans: ""
        for w in words:  # w: "step" -> "steps" -> "stripe" -> "stepple"
            freq = Counter(w)  # freq: Counter("step") / Counter("steps") / ...
            if all(freq[c] >= need[c] for c in need):  # freq vs need
                if ans == "" or len(w) < len(ans):  # ans, w
                    ans = w  # ans: "step" -> "steps"
        return ans  # ans: "steps"
Solution().shortestCompletingWord("1s3 PSt", ["step", "steps", "stripe", "stepple"])
Solution().shortestCompletingWord("1s3 456", ["looks", "pest", "stew", "show"])

'''
public class Solution {
public class Solution {                                                                 // Solution class

    public String shortestCompletingWord(String licensePlate, String[] words) {        // main method to find shortest completing word
        int[] need = new int[26];                                                      // frequency array for required letters (a-z)
        for (char ch : licensePlate.toCharArray()) {                                   // iterate over each character in licensePlate
            if (Character.isLetter(ch)) {                                              // process only letters, ignore digits/spaces
                ch = Character.toLowerCase(ch);                                        // make character lowercase
                need[ch - 'a']++;                                                      // increment count for this letter
            }
        }

        String ans = null;                                                             // variable to store current best answer

        for (String word : words) {                                                    // iterate over each candidate word
            if (isCompleting(word, need)) {                                            // check if this word satisfies all required letters
                if (ans == null || word.length() < ans.length()) {                     // update answer if shorter or first found
                    ans = word;                                                        // store current shortest completing word
                }
            }
        }

        return ans;                                                                    // return the shortest completing word
    }

    private boolean isCompleting(String word, int[] need) {                            // helper to check if word completes license plate
        int[] freq = new int[26];                                                      // frequency array for letters in this word
        for (char ch : word.toCharArray()) {                                           // iterate over characters in word
            if (Character.isLetter(ch)) {                                              // consider only letters
                ch = Character.toLowerCase(ch);                                        // convert to lowercase
                freq[ch - 'a']++;                                                      // increment count for this letter
            }
        }
        for (int i = 0; i < 26; i++) {                                                 // check all letters from 'a' to 'z'
            if (freq[i] < need[i]) {                                                   // if word lacks required count of a letter
                return false;                                                          // then it's not a completing word
            }
        }
        return true;                                                                   // all required letters are present
    }

    public static void main(String[] args) {                                           // test method
        Solution s = new Solution();                                                   // create Solution instance
        System.out.println(                                                            // print result for first test case
                s.shortestCompletingWord("1s3 PSt",
                        new String[]{"step", "steps", "stripe", "stepple"})
        );                                                                             // expected: "steps"

        System.out.println(                                                            // print result for second test case
                s.shortestCompletingWord("1s3 456",
                        new String[]{"looks", "pest", "stew", "show"})
        );                                                                             // expected: "pest"
    }
}
'''