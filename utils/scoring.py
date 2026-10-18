def calculate_score(
    revenue,
    cost,
    cash,
    growth,
    business_type,
    industry_value=0
):

    score = 50

    profit = revenue - cost

    if revenue > 0:
        profit_margin = profit / revenue
    else:
        profit_margin = 0

    # กำไร

    if profit_margin > 0.30:
        score += 20

    elif profit_margin > 0.10:
        score += 10

    else:
        score -= 10

    # สภาพคล่อง

    if cash > revenue:
        score += 15

    elif cash > revenue * 0.5:
        score += 10

    elif cash < revenue * 0.3:
        score -= 15

    # การเติบโต

    if growth > 10:
        score += 15

    elif growth > 0:
        score += 10

    else:
        score -= 15

    score += industry_value

    return max(
        0,
        min(score,100)
    )
