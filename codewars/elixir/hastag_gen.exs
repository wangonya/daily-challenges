# https://www.codewars.com/kata/52449b062fb80683ec000024/train/elixir

defmodule Hashtag do
  def too_long?(s) do
    String.length(s) > 140
  end

  def too_short?(s) do
    String.length(s) < 2
  end


  def result(input) do
    cond do
      too_long?(input) ->
        false
      too_short?(input) ->
        false
      true -> input
    end
  end

  def generate(input) do
    input
    |> String.split
    |> Enum.map(&String.capitalize/1)
    |> Enum.join(" ")
    |> String.replace(" ", "")
    |> (&"##{&1}").()
    |> result
  end
end

s = "       "
IO.inspect(Hashtag.generate(s))
