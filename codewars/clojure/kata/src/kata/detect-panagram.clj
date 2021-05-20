(ns Pangram
  (:require [clojure.string :refer [lower-case]]))

(defn pangram?
  [s]
  (->> (apply str (filter #(Character/isLetter %) s))
       (lower-case)
       (distinct)
       (count)
       (= 26)))

(println (pangram? "The quick b--rown fox jumps over the lazy dog."))
(println (pangram? "a AA abcd B CC"))

; other solutions

(defn pangram?
  [s]
  (subset?
   (set "abcdefghijklmnopqrstuvwxyz")
   (set (lower-case s))))

(defn pangram?
  [s]
  (superset?
   (set (lower-case s))
   (set "abcdefghijklmopqrstuvwxyz")))

(defn pangram? [s]
  (every? (-> s lower-case set) (set "abcdefghijklmnopqrstuvwxyz")))
