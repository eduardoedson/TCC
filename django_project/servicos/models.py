from django.db import models
from django.utils.translation import ugettext_lazy as _


class Setor(models.Model):
    descricao = models.CharField(
        max_length=30, verbose_name=_('Nome do Setor'), unique=True)
    nome = models.CharField(
        max_length=50, verbose_name=_('Nome'), blank=True)

    class Meta:
        verbose_name = _('Setor')
        verbose_name_plural = _('Setores')
        ordering = ['descricao']

    def __str__(self):
        return self.descricao + ' - ' + self.nome


class Disciplina(models.Model):
    setor = models.ForeignKey(Setor, verbose_name=_('Curso'))
    descricao = models.CharField(
        max_length=50, verbose_name=('Nome da Disciplina'))

    class Meta:
        verbose_name = _('Disciplina')
        verbose_name_plural = _('Disciplinas')
        ordering = ['descricao', 'setor']

    def __str__(self):
        return self.descricao


class AreaAtendimento(models.Model):
    setor = models.ForeignKey(Setor, verbose_name=_('Setor'))
    descricao = models.CharField(
        max_length=30, verbose_name=('Área de Atendimento'), unique=True)

    class Meta:
        verbose_name = _('Área de Atendimento')
        verbose_name_plural = _('Áreas de Atendimento')
        ordering = ['setor', 'descricao']

    def __str__(self):
        return self.descricao
