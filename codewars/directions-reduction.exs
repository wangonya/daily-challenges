# https://www.codewars.com/kata/550f22f4d758534c1100025a/train/elixir
defmodule Directions do
  def north_south?(dir) do
    (List.first(dir) == "NORTH" and List.last(dir) == "SOUTH") or
      (List.last(dir) == "NORTH" and List.first(dir) == "SOUTH")
  end

  def east_west?(dir) do
    (List.first(dir) == "EAST" and List.last(dir) == "WEST") or
      (List.last(dir) == "EAST" and List.first(dir) == "WEST")
  end

  def north_east?(dir) do
    (List.first(dir) == "NORTH" and List.last(dir) == "EAST") or
      (List.last(dir) == "NORTH" and List.first(dir) == "EAST")
  end

  def north_west?(dir) do
    (List.first(dir) == "NORTH" and List.last(dir) == "WEST") or
      (List.last(dir) == "NORTH" and List.first(dir) == "WEST")
  end

  def south_east?(dir) do
    (List.first(dir) == "SOUTH" and List.last(dir) == "EAST") or
      (List.last(dir) == "SOUTH" and List.first(dir) == "EAST")
  end

  def south_west?(dir) do
    (List.first(dir) == "SOUTH" and List.last(dir) == "WEST") or
      (List.last(dir) == "SOUTH" and List.first(dir) == "WEST")
  end

  def samed_direction?(dir) do
    length(Enum.uniq(dir)) == 1
  end

  def check(dir) do
    # require IEx; IEx.pry
    # IO.inspect(dir1)
    # IO.inspect(dir2)
    cond do
      north_south?(dir) ->
        []

      east_west?(dir) ->
        []

      north_east?(dir) ->
        List.last(dir) |> String.split()

      north_west?(dir) ->
        List.last(dir) |> String.split()

      south_east?(dir) ->
        List.last(dir) |> String.split()

      south_west?(dir) ->
        List.last(dir) |> String.split()

      samed_direction?(dir) ->
        List.last(dir) |> String.split()

      true ->
        [[dir]]
    end
  end

  def reduce(directions) do
    directions
    |> Enum.chunk_every(2, 1)
    |> Enum.flat_map(&Directions.check/1)

    # Enum.scan(directions, 1, &Directions.reduce(&1, &2))
  end
end

dir = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
IO.inspect(dir)
IO.inspect(Directions.reduce(dir))

# 1,2,3,4,5 = [1, 3, 6, 10, 15]
#
# defmodule Directions do

  # def reduce(directions), do: List.foldr(directions, [], &reduce/2)
  #
  # # Done.
  # defp reduce(head, []), do: [head]
  # # Fold.
  # defp reduce("NORTH", ["SOUTH" | tail]), do: tail
  # defp reduce("SOUTH", ["NORTH" | tail]), do: tail
  # defp reduce("WEST", ["EAST" | tail]), do: tail
  # defp reduce("EAST", ["WEST" | tail]), do: tail
  # # Continue.
  # defp reduce(head, [next | tail]), do: [head, next | tail]

end

