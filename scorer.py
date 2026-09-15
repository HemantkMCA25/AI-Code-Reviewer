def score(metrics):
    score = 100

    score -= metrics["loops"] * 12
    score += metrics["functions"] * 5

    return max(0, min(100, score))