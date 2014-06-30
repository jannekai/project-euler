#!/usr/bin/env escript

main(_) ->
	% factors = factors(13195)
	% factors = factors(600851475143)	
	io:format("result is ~w ~n", [find_primes_up_to(6857)]).	

find_primes_up_to(Max) ->
	find_primes_up_to([2], 1, Max).

find_primes_up_to(Primes, V, Max) when V == Max ->
	Primes;
find_primes_up_to(Primes, V, Max) ->
	find_primes_up_to(apppend_if_prime(Primes, V+1), V+1, Max).

apppend_if_prime(Primes, Value) ->
	apppend_if_prime(Primes, Value, Primes).

% None of the previous primes divided the value -> the value is prime
apppend_if_prime([], V, Primes) ->
	%% io:format("~w is a prime~n", [V]),
	Primes ++ [V];
%% Is divisible by one the earlier primes -> V is not the next prime
apppend_if_prime([P | _], V, Primes) when V rem P == 0 ->
	% io:format("~w is not a prime~n", [V]),
	Primes;
apppend_if_prime([_ | Rest], V, Primes) ->
	apppend_if_prime(Rest, V, Primes).

