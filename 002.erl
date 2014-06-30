#!/usr/bin/env escript

main(_) ->
	io:format("result is ~w ~n", [sum_fib(1,2,0)]).	

sum_fib(_, C, Sum) when C >= 4000000 -> 
	Sum;
sum_fib(P, C, Sum) when C rem 2 == 0 ->
	sum_fib(C, P+C, Sum+C);
sum_fib(P, C, Sum) ->
	sum_fib(C, P+C, Sum).

