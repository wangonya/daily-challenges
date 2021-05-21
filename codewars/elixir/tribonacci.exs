defmodule TribonacciSequence do
  def tribonacci(_signature, n) when n == 0, do: []

  def tribonacci(_signature, n) when n == 1, do: [1]

  def tribonacci(signature, n) when tuple_size(signature) >= n do
    Tuple.to_list(signature)
  end

  @spec tribonacci({number, number, number}, non_neg_integer) :: [number]
  def tribonacci(signature, n) do
    s =
      Enum.slice(Tuple.to_list(signature), (tuple_size(signature) - 3)..tuple_size(signature))
      |> Enum.sum()

    signature = Tuple.append(signature, s)
    tribonacci(signature, n)
  end
end

IO.inspect(TribonacciSequence.tribonacci({0, 1, 1}, 10))

# defmodule TribonacciSequence do
  # @spec tribonacci({number, number, number}, non_neg_integer) :: [number]
  # def tribonacci(signature, n) do
    # signature
    # |> Stream.unfold(fn {a, b, c} -> {a, {b, c, a+b+c}} end)
    # |> Enum.take(n)
  # end
# end
