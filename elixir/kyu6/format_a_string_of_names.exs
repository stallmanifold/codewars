defmodule People do
  def list(people) do
    case people do
      [] -> "" 
      [person] -> person[:name]
      [person1, person2] -> person1[:name] <> " & " <> person2[:name]
      [person | tail] -> person[:name] <> ", " <> list(tail)
    end
  end
end


IO.puts(People.list([ %{name: "Bart"}, %{name: "Lisa"}, %{name: "Maggie"}]))
IO.puts(People.list([ %{name: "Bart"}, %{name: "Lisa"} ]))
IO.puts(People.list([ %{name: "Bart"}]))
