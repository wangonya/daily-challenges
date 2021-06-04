(ns kata.remove-url-anchor
  (:require
   [clojure.string :as str]))

(defn remove-url-anchor [url]
  (->> (str/split url #"#")
       (first)))
