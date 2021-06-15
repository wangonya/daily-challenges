(ns kata.core
  (:require
   [clojure.string :as str]))

(defn -main
  "I don't do a whole lot ... yet."
  []
  (println "Hello, World!"))


;; ====================================================================
;; https://www.codewars.com/kata/55b3425df71c1201a800009c/train/clojure


(defn to-seconds
  [text]
  (let [[h, m, s] (str/split text #"\|")]
    (+ (* 3600 (Integer/parseInt h))
       (* 60 (Integer/parseInt m))
       (Integer/parseInt s))))

(defn to-str
  [seconds]
  (let [s (mod seconds 60)
        minutes (int (/ seconds 60))
        m (mod minutes 60)
        h  (int (/ minutes 60))]
    (str/join "|" (map #(format "%02d" %) [h m s]))))

(defn stat [strg]
  (if (empty? strg)
    ""
    (let [datetimes (map to-seconds (str/split strg #", "))
          sorted (sort datetimes)
          n (count sorted)
          center (take (if (odd? n) 1 2) (drop (int (/ (dec n) 2)) sorted))
          mean (int (/ (apply + center) (count center)))
          delta (- (last sorted) (first sorted))
          avg (int (/ (apply + sorted) n))]
      (str "Range: " (to-str delta)
           " Average: " (to-str avg)
           " Median: " (to-str mean)))))

;; ====================================================================
;; https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/train/clojure

(defn max-sequence
  "Finding the maximum sum of a contiguous subsequence in an array or list of integers.
  Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array.
  If the list is made up of only negative numbers, return 0 instead.
  Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray."
  [input]
  (let [pos+ (fn [sum x] (if (neg? sum) x (+ sum x)))
        ending-heres (reductions pos+ 0 input)]
    (reduce max ending-heres)))

(defn max-sequence2
  [xs]
  (apply max (reductions #(max (+ %1 %2) 0) 0 xs)))


;; ====================================================================
;; https://www.codewars.com/kata/559a28007caad2ac4e000083/train/clojure


(defn fib
  ([]
   (fib 1 1))
  ([a b]
   (lazy-seq (cons a (fib b (+ a b))))))

(defn perimeter [n]
  (->> (take (inc n) (fib))
       (reduce +)
       (* 4)))

;; ====================================================================
;; https://www.codewars.com/kata/573992c724fc289553000e95/train/clojure

(defn num-to-seq [n]
  (->> n
       (iterate #(quot % 10))
       (take-while pos?)
       (mapv #(mod % 10))
       rseq))

(defn smallest [n]
  (let [num-seq (vec (num-to-seq n))
        indexed-num-seq (map-indexed vector num-seq)
        smallest (apply min-key second indexed-num-seq)
        smallest-index (first smallest)
        smallest-number (second smallest)
        larger-index (first (some #(if (> (second %) (second smallest)) %) indexed-num-seq))
        new-num (list* smallest-number (concat (subvec num-seq 0 smallest-index) (subvec num-seq (inc smallest-index))))]
    [new-num smallest-index larger-index]))

;; solution
(defn smallest2 [n]
  (let [s (str n)]
    (-> (for [i (range (count s))
              j (range (count s))
              :when (not= i j)
              :let [c (get s i)
                    s (str (subs s 0 i) (subs s (inc i)))
                    s (str (subs s 0 j) c (subs s j))]]
          [(bigint s) i j])
        sort
        first)))
