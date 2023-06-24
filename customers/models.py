from django.db import models
import uuid


class Customers(models.Model):
    STATUS_TYPE = (
        ('aprovada',  'Aprovada'),
        ('parcial_aprovada',  'Parcialmente Aprovada'),
        ('negada', 'Negada'),
        ('em_analise', 'Em analise'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(verbose_name='Nome do cliente',
                                 max_length=200, blank=False, help_text='Nome completo do cliente.')
    cpf_cnpj = models.CharField(
        verbose_name='CPF/CNPJ', max_length=20, blank=False, help_text='Numero de cpf ou cnpj.')
    address = models.CharField(
        verbose_name='Endereço', max_length=100, blank=False, help_text='Endereço completo.')
    value = models.DecimalField(verbose_name='Valor solicitado', max_digits=12,
                                decimal_places=2, blank=False, help_text='Valor solicitado pelo cliente.')
    approved_value = models.DecimalField(verbose_name='Valor aprovado', default=0, max_digits=12,
                                         decimal_places=2, editable=False, help_text='Valor aprovado pelo banco.')
    status = models.CharField(
        verbose_name='Status', default=STATUS_TYPE[3][0], choices=STATUS_TYPE, editable=False, help_text='Status da solicitação de empréstimo.')
    score = models.IntegerField(verbose_name='Pontuação', default=0, editable=False,
                                help_text='Pontuação do cliente gerada automaticamente.')
    created_at = models.DateTimeField(
        verbose_name='Data de criação', auto_now_add=True, help_text='Data de criação do cliente.')
    updated_at = models.DateTimeField(
        verbose_name='Ultima atualização', auto_now=True, help_text='Data da ultima atualização.')

    class Meta:
        ordering = ['-updated_at', 'status']
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return f'{self.full_name} - {self.status}'
