# https://www.codewars.com/kata/541c8630095125aba6000c00

defmodule FindDigitalRoot do
  def digital_root(n) when n < 10 do
    n
  end

  def digital_root(n) do
    digits = Integer.digits(n)
    sum = Enum.sum(digits)
    digital_root(sum)
  end
end

IO.inspect(FindDigitalRoot.digital_root(456))

# defmodule Kata do
#    def digital_root(n) when n < 10, do: n
#    def digital_root(n), do: Integer.digits(n) |> Enum.sum |> digital_root
#end