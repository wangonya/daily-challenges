# https://www.codewars.com/kata/550498447451fbbd7600041c

defmodule AreTheyTheSame do
  
  @spec comp([number], [number]) :: boolean
  def comp(a, b) do
    sorted_a = Enum.sort(a)
    IO.inspect(sorted_a)
    squared_sorted_a = Enum.map(sorted_a, fn n -> n * n end)
    IO.inspect(squared_sorted_a)
    sorted_b = Enum.sort(b)
    IO.inspect(sorted_b)
    squared_sorted_a == sorted_b
  end
end

a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
IO.puts AreTheyTheSame.comp(a, b)

# defmodule Aretheythesame do
#
#    @spec comp([number], [number]) :: boolean
#    def comp(a, b) do
#      a |> Enum.map(&(&1*&1)) |> Enum.sort == b |> Enum.sort
#    end
#end