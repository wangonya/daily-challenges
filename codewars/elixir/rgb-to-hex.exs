defmodule Kata do
  # def rgb(r, g, b) when do
  # Integer.to_string(r, 16) <> Integer.to_string(g, 16) <> Integer.to_string(b, 16)
  # end

  def to_hex(x) do
    x = if x > 255, do: x = 255, else: x
    x = if x < 0, do: x = 0, else: x
    x = Integer.to_string(x, 16)
    cond do
      String.length(x) == 1 ->
        "0" <> x
      true ->
        x
    end
  end

  def rgb(r, g, b) do
    Kata.to_hex(r) <> Kata.to_hex(g) <>Kata.to_hex(b) 
  end
end

# returns 9400D3
IO.inspect(Kata.rgb(148, 0, 211))
# returns FFFFFF
IO.inspect(Kata.rgb(255, 255, 300))
# returns 000000 
IO.inspect(Kata.rgb(0, 0, -20))
