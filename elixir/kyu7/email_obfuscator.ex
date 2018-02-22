defmodule EmailObfuscator do

  def execute(email) do
    email |> String.replace("@", " [at] ") |> String.replace(".", " [dot] ")
  end

end