defmodule MultiplesOf3Or5 do
  def multiple?(x) when x < 3, do: nil
  def multiple?(x), do: rem(x, 3) == 0 or rem(x, 5) == 0

  def solution(n) do
    Enum.filter(1..n-1, fn x -> multiple?(x) end)
    |> Enum.sum
  end
end

IO.inspect(MultiplesOf3Or5.solution(10))
