-module(primes).
-export([next/1,next/0]).

next() ->
	next([]).
next([]) ->
	Primes = [2],
	Primes ++ [next_prime(Primes, Primes, 3)];
next(Primes) when is_list(Primes) ->	
	Primes ++ [next_prime(Primes, Primes, lists:last(Primes)+1)].

%% V was not divisible by any of the previos primes, we found our next prime
next_prime([], Primes, V) ->
	V;
%% Is divisible by one the primes -> V is not a prime
next_prime([H|T], Primes, V) when V rem H == 0 ->
	next_prime(Primes, Primes, V+1);
%% V is not divisible by the head prime in list, continue recursion
next_prime([H|T], Primes, V) ->
	next_prime(T, Primes, V).

