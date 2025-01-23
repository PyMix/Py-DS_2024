import numpy as np


def guess_number(secret_number: int, from_n: int, to_n: int) -> int:
    """
    Args:
        secret_number (int): Number to guess.
        from_n (int): Lower bound.
        to_n (int): Upper bound.

    Returns:
        int: Number of attempts
    """

    count = 0 # number of attempts
    while True:
        count += 1
        predict = (from_n + to_n) // 2
        if secret_number > predict:
            from_n = predict
        elif secret_number < predict:
            to_n = predict
        else:
            break

    return count


def score_game(predict_func, from_n: int = 1, to_n: int = 101, games_n: int = 10000) -> int:
    """Calculate average number of attempts

    Args:
        predict_func (function): guessing function
        from_n (int, optional): lower bound. Defaults to 1.
        to_n (int, optional): upper bound. Defaults to 101.
        games_n (int, optional): number of games. Defaults to 10000.

    Returns:
        int: average number of attempts
    """

    count_ls = []
    # np.random.seed(1)
    random_array = np.random.randint(from_n, to_n, games_n)

    for secret_num in random_array:
        count_attempts = predict_func(secret_num, from_n, to_n)
        count_ls.append(count_attempts)

    score = int(np.mean(count_ls)) # average number of attempts
    print(f"Algorithm guesses the number in an average of {score} attempts")

    return score
