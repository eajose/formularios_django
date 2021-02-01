from rest_framework import serializers

from core.models import Endereco, Pessoa


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        exclude = [
            'pessoa'
        ]


class PessoaSerializer(serializers.ModelSerializer):
    enderecos = EnderecoSerializer(
        read_only=True,
        many=True
    )

    class Meta:
        model = Pessoa
        fields = [
            'id',
            'nome',
            'cpf',
            'salario',
            'enderecos',
        ]

