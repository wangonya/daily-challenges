(ns kata.core
  (:require
   [clojure.string :as str]))

(defn -main
  "I don't do a whole lot ... yet."
  []
  (println "Hello, World!"))


;; ======================================================================
;; "https://www.codewars.com/kata/55b3425df71c1201a800009c/train/clojure"


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
