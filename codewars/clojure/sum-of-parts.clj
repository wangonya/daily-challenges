(ns sum-of-parts.core)

(defn sum-list [ls]
  (println "in sum list")
  (reduce + ls))

(defn parts-sums [&ls]
  ; (def sums (list))

  ; (println (map #(sum-list %) '(0 1 3 6 10)))
  ; (println (map #(reduce + %) '(0 1 3 6 10))))
  ; (println (map #(reduce + %) '(0 1 3 6 10))))

  (def s '(0 1 3 6 10))
  (def c (count s))
  (println (take c (reductions + s)))
  (println (map #(reduce + %) s)))

(parts-sums '(0 1 3 6 10))


;; solutions
(defn parts-sums [xs]
  (->> xs reverse (reductions + 0) reverse))
