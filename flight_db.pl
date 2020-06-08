
flight(toronto, london, aircanada, 625, 500).
flight(toronto, london, united, 775, 560).
flight(toronto, madrid, united, 1075, 645).
flight(toronto, madrid, iberia, 925, 585).
flight(toronto, madrid, aircanada, 1025, 585).

flight(london, barcelona, iberia, 335,350).

flight(barcelona, valencia, iberia, 190,125).
flight(barcelona, madrid, iberia, 235, 140).
flight(barcelona, madrid, aircanada, 215, 135).

flight(madrid, valencia, iberia, 155, 115).
flight(madrid, malaga, iberia, 175, 135).

flight(valencia, malaga, iberia, 170, 170).

flight(paris, toulouse, united, 125, 210).

airport(toronto, 50, 60).
airport(barcelona, 40, 30).
airport(madrid, 75, 45).
airport(valencia, 40, 20).
airport(malaga, 50, 30).
airport(paris, 50, 60).
airport(toulouse, 40, 30).
airport(london, 75, 80).

is_flight(A, B) :-
    ( flight(A, B, _, _, _) ; flight(B, A, _, _, _) ).

is_flight_new(A, B, C) :-
    ( flight(A, B, C, _, _) ; flight(B, A, C, _, _) ).

is_cheap(A, B, C) :-
    ( flight(A, B, C, Price, _) ; flight(B, A, C, Price, _) ) , ( Price < 400 ).

in_two_flights(A, B) :-
    ( is_flight(A, X) , is_flight(X, B) ).

preferred_cheap_or_aircanada(A, B, C):-
    (is_cheap(A, B, C) ; C == aircanada),
    format("~nPreferred : ~w ", [C]).

if_united_then_aircanada(A, B) :-
    is_flight_new(A, B, united)  ->  is_flight_new(A, B, aircanada).
        


