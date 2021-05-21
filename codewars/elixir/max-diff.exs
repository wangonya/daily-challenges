# https://www.codewars.com/kata/5663f5305102699bad000056/train/elixir

defmodule MaxDiff do

  def max_diff(a1, a2) when a1 == [] or a2 == [], do: -1

  @spec max_diff([String], [String]) :: number
  def max_diff(a1, a2) do
    a3 = Enum.sort_by(a1, &String.length/1)
    a4 = Enum.sort_by(a2, &String.length/1)
    cond do
      String.length(List.last(a3)) > String.length(List.last(a4)) ->
        String.length(List.last(a3)) - String.length(List.first(a4))

      String.length(List.last(a3)) < String.length(List.last(a4)) ->
        String.length(List.last(a4)) - String.length(List.first(a3))
    end
  end
end

# defmodule MaxDiff do
#
#    def mxdiflg(a1, _) when (a1 == []), do: -1
#    def mxdiflg(_, a2) when (a2 == []), do: -1
#    def mxdiflg(a1, a2) do
#        l1 = a1 |> Enum.map(&String.length/1)
#        l2 = a2 |> Enum.map(&String.length/1)
#        max(abs((l1 |> Enum.max) - (l2 |> Enum.min)), abs((l2 |> Enum.max) - (l1 |> Enum.min)))
#    end
#
#end
