(ns kata)
(defn min-value [digits]
  (->> digits
  (distinct)
  (sort)
  (apply str)
  (Integer. )
  )
)

(println (min-value [1 3 1])) ; 13
(min-value [4 7 5 7]) ; 457
(min-value [4 8 1 4]) ; 148
(min-value [1 9 1 3 7 4 6 6 7]) ; 134679
(min-value [3 6 5 5 9 8 7 6 3 5 9]) ; 356789
