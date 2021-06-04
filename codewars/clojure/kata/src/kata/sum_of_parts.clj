(ns kata.sum-of-parts)

(defn parts-sums [&ls]
  ; (def sums (list))

  ; (println (map #(sum-list %) '(0 1 3 6 10)))
  ; (println (map #(reduce + %) '(0 1 3 6 10))))
  ; (println (map #(reduce + %) '(0 1 3 6 10))))

  (def s '(0 1 3 6 10))
  (def c (count s)))


;; solutions


;; (defn parts-sums [xs]
;;  (->> xs reverse (reductions + 0) reverse))
