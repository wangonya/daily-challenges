(ns kata.looking-for-benefactor)

(defn new-avg [arr navg]
  (->> arr
       (reduce +)
       (- (* (+ 1 (count arr)) navg))
       (pos-int?)
       (cond  "ok"
             :else "not ok")))

(new-avg [14 30 5 7 9 11 15] 30)
(new-avg [14 30 5 7 9 11 16] 90)
(new-avg [14, 30, 5, 7, 9, 11, 15] 2)


;; solutions
(defn- output [n]
  (int (Math/ceil n)))

(defn new-avg [arr navg]
  (let [sum   (apply + arr)
        len   (count arr)
        n     (- (* navg (inc len)) sum)]
    (cond
      (<= n 0) (throw (IllegalArgumentException. ""))
      :else    (output n))))

(defn new-avg [arr navg]
  (let [x (int (Math/ceil (- (* navg (+ (count arr) 1)) (reduce + arr))))]
    (if (>= x 0) x (throw (IllegalArgumentException. "invalid_argument")))))

(defn new-avg [arr navg]
  (-> arr
       (count)
       (inc)
       (* navg)
       (- (apply + arr))
       (Math/ceil)
       (int)
       (#(if (neg? %) (throw (IllegalArgumentException. "")) %))))
