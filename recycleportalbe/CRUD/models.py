from django.db import models


class ContractForm(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(verbose_name='Email', max_length=100, unique=True)
    tipoNegocio = models.CharField(verbose_name='TipoNegocio', max_length=100, unique=True)
    descricao = models.CharField(verbose_name='Descrição', max_length=100, unique=True)

    def __str__(self):        
        return self.email + ' - ' + self.tipoNegocio + ' - ' + self.descricao


    class Meta:
        verbose_name_plural = "Contract Form"


# Model são os campos da tabela, definir se é primary key, se é null e foraing key
