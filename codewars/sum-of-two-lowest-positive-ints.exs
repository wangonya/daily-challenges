# https://www.codewars.com/kata/558fc85d8fd1938afb000014/elixir

defmodule SmallSummer do
  def sum_two_smallest_numbers(numbers) do
    Enum.sort(numbers)
    |> Enum.slice(0..1)
    |> Enum.sum
  end
end

n = [19, 5, 42, 2, 77]
IO.inspect(SmallSummer.sum_two_smallest_numbers(n))

# def sum_two_smallest_numbers(numbers) do
#    [x,y | _] = Enum.sort(numbers)
#    x + y
#  end