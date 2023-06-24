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
        (1,  'Aprovada'),
        (2,  'Parcialmente Aprovada'),
        (3, 'Negada'),
    )
    if (approved_value > 0 and score <= 300):
        status = STATUS_TYPE[0][1]
    elif (score > 300 and score <= 600):
        status = STATUS_TYPE[1][1]
    else:
        status = STATUS_TYPE[2][1]

    return status
