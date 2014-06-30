#!/usr/bin/env escript

main(_) ->
	io:format("result is ~w ~n", [is_multiple(999,0)]).	

is_multiple(Value, Sum) when Value == 0 ->
	Sum;
is_multiple(Value, Sum) when Value rem 5 == 0 ->	
	is_multiple(Value-1, Sum+Value);
is_multiple(Value, Sum) when Value rem 3 == 0 ->
	is_multiple(Value-1, Sum+Value);
is_multiple(Value, Sum) ->
	is_multiple(Value-1, Sum).

