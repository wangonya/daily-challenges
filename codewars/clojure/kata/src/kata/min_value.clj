(ns kata.min-value)
(defn min-value [digits]
  (->> digits
       (distinct)
       (sort)
       (apply str)
       (Integer.)))

