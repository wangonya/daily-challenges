(ns kata.persistence)

(defn multiply-digits [n]
  (if (< n 10)
    0
    (let [number (if-not (string? n) (Long/toString n 10) n)]
      (reduce * (map #(Long/valueOf (str %) 10) number)))))

(defn persistence
  "takes in a positive parameter num and
   returns its multiplicative persistence,
   which is the number of times you must
   multiply the digits in num until you
   reach a single digit."

  [num]

  (def new-num (multiply-digits num))

  (if (< new-num 10)
    (do new-num)
    (do (persistence new-num))))

;; solution


(defn persistence-2 [n]
  (if (< n 10)
    0
    (let [digit-list (->> (str n)
                          seq
                          (map str)
                          (map read-string))]
      (if (= 1 (count digit-list))
        digit-list
        (inc (persistence (reduce * digit-list)))))))
