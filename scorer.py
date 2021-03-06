unsA = 0  # Ultra Agressive
unsB = 0  # Agressive
unsC = 0  # Conservative
unsD = 0  # Ultra Conservative

total = {
    "Ваш инвест профиль - *Ультра-Агрессивный*. Приоритет такого инвестора — максимальная доходность. Он готов инвестировать в высокорисковые инструменты: акции новых технологичных компаний, ценные бумаги развивающихся рынков, IPO. Как правило, в инструменты фондового рынка они инвестирует около 80% капитала. Однако все позиции спекулятивные и короткие, не занимают более 10% от депозита. \n \n /start": unsA,
    "Ваш инвест профиль - *Агрессивный*. Инвестор готов принять значительный риск ради потенциальной доходности. Допускает колебания стоимости капитала в кратко- и среднесрочной перспективе ради потенциального дохода. Однако соблюдает баланс рисков к возможной доходности. Этот пункт крайне важен для такого инвестора, важно иметь длю консервативных ETF-фондов или облигаций, так же не стоит забывать о свободных средствах на счету. \n \n /start": unsB,
    "Ваш инвест профиль - *Консервативный*. Цель инвестора — сохранить капитал и защитить его от инфляции. Дополонительная прбыль вторична. Инвестор готов получать доход на уровне чуть выше ставки по вкладам. Он не склонен рисковать, поэтому большую часть денег, примерно 70-75%, инвестирует в облигации высоконадёжных эмитентов и держит на банковском счете. Остальное инвестирует в акции наиболее крупных и ликвидных компаний: «голубых фишек» и ETF. \n \n /start": unsC,
    "Ваш инвест профиль - *Ультра-Консервативный*. Цель инвестора — сохранить капитал и защитить его от инфляции. Уровень дохода близок к ставке по вкладам, однако в денежном эквиваленте такое отношение к риску как правильо обуславливается высокими капиталами и не молодым возрастом. Главный инструмент - облигации. ОФЗ - отличный вариант. Так же допускются муниципальные облигации и консервативные ETF. \n \n /start": unsD,
}


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
