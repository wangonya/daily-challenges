(ns kata
  (:require
   [clojure.string :as str]))

(defn remove-url-anchor [url]
  (->> (str/split url #"#")
       (first)))

(println (remove-url-anchor "www.codewars.com#about"))
(println (remove-url-anchor "www.codewars.com?page=1"))
