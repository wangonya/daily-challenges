defmodule WeightSort do
  def weight(str) do
    str
    |> String.split()
    |> Enum.map(fn x -> String.to_integer(x) end)
    |> Enum.map(fn x -> Integer.digits(x) end)
    |> Enum.map(fn x -> Enum.sum(x) end)
    |> Enum.with_index()
    |> Enum.map(fn {k, v} -> {Enum.at(String.split(str), v), k} end)
    |> Enum.sort
    |> List.keysort(1)
    |> Enum.map_join(" ", fn {k, _} -> k end)
  end
end

weights = "56 65 74 100 99 68 86 180 90"
IO.inspect(WeightSort.weight(weights))

weights = "103 123 4444 99 2000"
IO.inspect(WeightSort.weight(weights))

weights = "2000 10003 1234000 44444444 9999 11 11 22 123"
IO.inspect(WeightSort.weight(weights))
