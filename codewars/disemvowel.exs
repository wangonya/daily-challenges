defmodule Kata do
  def disemvowel(s) do 
    String.replace(s, ~r/[aeiouAEIOU]/, "")
  end
end

s = "This website is for losers LOL!"
IO.inspect(Kata.disemvowel(s))
