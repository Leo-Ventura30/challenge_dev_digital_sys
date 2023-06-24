def validate_proposal(value, score):
    if (score <= 300):
        value = 0
    elif (score > 300 and score <= 600):
        value = value / 2
    else:
        return value
    return value


def compare_score(approved_value, score):
    STATUS_TYPE = (
        ('aprovada',  'Aprovada'),
        ('parcial_aprovada',  'Parcialmente Aprovada'),
        ('negada', 'Negada'),
        ('em_analise', 'Em analise'),
    )

    if (approved_value == 0 or score <= 300):
        status = STATUS_TYPE[2][0]
    elif (score > 300 and score <= 600):
        status = STATUS_TYPE[1][0]
    else:
        status = STATUS_TYPE[0][0]

    return status
