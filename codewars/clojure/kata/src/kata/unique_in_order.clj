(ns kata.unique-in-order)

(defn unique-in-order
  "- takes a sequence
   - returns a list of items without any elements with the same value next to each other
   - preserving the original order of elements"
  [input]
  (->> input
       (partition-by identity)))

; solutions
(defn unique-in-order [input]
  (dedupe input)) ; dedupe: Returns a lazy sequence removing consecutive duplicates in coll.

(defn unique-in-order [input]
  (mapcat set (partition-by identity input))) ; mapcat: Returns the result of applying concat to the result of applying map to f and colls

(defn unique-in-order
  [input]
  (reduce
   #(if (= (peek %1) %2)
      %1
      (conj %1 %2))
   []
   input))
