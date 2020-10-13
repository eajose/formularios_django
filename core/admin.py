from django.contrib import admin

from .models import Pessoa, Endereco


class PessoaAdmin(admin.ModelAdmin):
    pass


admin.site.register(
    Pessoa,
    PessoaAdmin
)


class EnderecoAdmin(admin.ModelAdmin):
    pass


admin.site.register(
    Endereco,
    EnderecoAdmin
)
# Register your models here.
