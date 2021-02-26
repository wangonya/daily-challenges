# https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9

defmodule Word do
  def find_shortest(s) do
    Enum.group_by(String.split(s), &String.length/1)
    |> Map.keys()
    |> List.first()
  end
end

s = "bitcoin take over the world maybe who knows perhaps"
IO.inspect(Word.find_shortest(s) )