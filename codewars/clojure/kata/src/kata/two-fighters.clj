(ns clojure.two-fighters)

(defrecord Fighter [name health damage-per-attack])

(defn declare-winner [f1 f2]
  (println f1)
  (println f2)
  (println (:health f1))

  (while (or (< 1 (:health f1)) (< 1 (:health f2)) )
    (println (:helth f1) - (:health f2))
  )
)

(declare-winner (->Fighter "Harald" 20 5) (->Fighter "Harry" 5 4))

; ==========
; solutions
; ==========


(defn declare-winner1 [f1 f2]
  (cond
    (<= (:hp f1) 0) (:name f2)
    (<= (:hp f2) 0) (:name f1)
    :else
      (recur
        (update f1 :hp - (:attack f2))
        (update f2 :hp - (:attack f1)))))

(defn declare-winner2 [f1 f2]
  (if (<= (:hp f1) 0)
    (:name f2)
    (recur f2 (update f1 :hp - (:attack f2)))))

(defn turn-ko [player opponent]
  (-> (/ (:hp player) (:attack opponent)) Math/ceil int))

(defn declare-winner3 [first second]
  (if (> (turn-ko first second) (turn-ko second first))
    (:name first)
    (:name second)))
