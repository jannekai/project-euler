-module(primes).
-export([next/1,next/0,is_prime/1]).

next() 		-> [2].
next([]) 	-> [2];
next(Primes) when is_list(Primes) ->	
	Primes ++ [next_prime(Primes, Primes, lists:last(Primes)+1)].

%% V was not divisible by any of the previos primes, we found our next prime
next_prime([], _Primes, V) ->
	V;
%% Is divisible by one the primes -> V is not a prime
next_prime([H|_T], Primes, V) when V rem H == 0 ->
	next_prime(Primes, Primes, V+1);
%% V is not divisible by the head prime in list, continue recursion
next_prime([_H|T], Primes, V) ->
	next_prime(T, Primes, V).

%% Returns true if the given number is a prime
is_prime(V) when V < 2 ->
	false;
is_prime(V) when V == 2 ->
	true;
is_prime(V) ->
	H = erlang:trunc(math:sqrt(V))+1,
	is_not_divisible_by_smaller_natural_number(V, H).

%% Returns true if the number is not divisible by
is_not_divisible_by_smaller_natural_number(_V, H) when H < 2 ->
	true;
is_not_divisible_by_smaller_natural_number(V, H) when V rem H == 0 ->
	false;
is_not_divisible_by_smaller_natural_number(V, H) ->
	is_not_divisible_by_smaller_natural_number(V, H-1).

