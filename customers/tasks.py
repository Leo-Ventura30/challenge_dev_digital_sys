from celery import shared_task
from .utils import validate_proposal, compare_score
from .models import Customers
from challenge_dev_digital_sys.celery import app


@app.task
def approve_proposal(id):
    try:
        customer = Customers.objects.get(id=id)

        customer.approved_value = validate_proposal(
            customer.value, customer.score)
        customer.status = compare_score(
            customer.approved_value, customer.score)

        customer.save()
        return f"Empréstimo no valor de R${customer.value} {customer.status} para o cliente {customer.full_name}"
    except Exception as err:
        print('Ocorreu erro ao acionar task', err)
        raise err
    finally:
        print('Task encerrada.')
