from config import total


def display_score(guesses):

    unsA = 0  # Ultra Agressive
    unsB = 0  # Agressive
    unsC = 0  # Conservative
    unsD = 0  # Ultra Conservative

    for i in guesses:
        if i == "A":  # ultra agressive
            unsA += 1

        elif i == "B":  # agressive
            unsB += 1

        elif i == "C":  # conservative
            unsC += 1

        elif i == "D":  # ultra conservative
            unsD += 1

        else:
            pass

    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print(guesses)

    print("A= " + str(unsA))
    print("B= " + str(unsB))
    print("C= " + str(unsC))
    print("D= " + str(unsD))

    # Counting most part answ.
    return(max(total, key=total.get))


# -------------------------
