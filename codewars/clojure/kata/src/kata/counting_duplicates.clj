(ns kata.counting-duplicates)

(defn duplicate-count
  "return the count of distinct case-insensitive alphabetic
  characters and numeric digits that occur more than
  once in the input string"

  ;;
  ; "abcde" -> 0 # no characters repeats more than once
  ; "aabbcde" -> 2 # 'a' and 'b'
  ; "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
  ; "indivisibility" -> 1 # 'i' occurs six times
  ; "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
  ; "aA11" -> 2 # 'a' and '1'
  ; "ABBA" -> 2 # 'A' and 'B' each occur twice
  ;;

  [text]

  (->> text
       (clojure.string/lower-case)
       (frequencies)
       (filter #(> (second %) 1))
       (count)))
