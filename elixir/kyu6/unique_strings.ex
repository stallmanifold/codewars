defmodule Util do
  def factorial(n) do
    case n do
      n when n <= 1 -> 1
      _ -> n * factorial(n - 1)
    end
  end

  def product(ns) do
    Enum.reduce(ns, 1, fn acc, n -> acc * n end)
  end
end

defmodule UniqueStrings do
  def uniq_count(string) do
    IO.puts(string)
    char_counts = String.upcase(string)
                |> String.graphemes()
                |> Enum.sort() 
                |> Enum.chunk_by(fn x -> x end) 
                |> Enum.map(fn s -> length(s) end)
    numerator = Util.factorial(String.length(string))
    denominator = char_counts 
                |> Enum.map(fn n -> Util.factorial(n) end)
                |> Util.product()
    div(numerator, denominator)
  end
end
