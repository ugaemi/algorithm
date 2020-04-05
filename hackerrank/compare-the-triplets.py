def compareTriplets(a, b):
    alice_win = 0
    bob_win = 0
    for alice, bob in zip(a, b):
        if int(alice) > int(bob):
            alice_win += 1
        elif int(alice) < int(bob):
            bob_win += 1

    return alice_win, bob_win
