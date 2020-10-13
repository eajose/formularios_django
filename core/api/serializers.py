from rest_framework import serializers

from core.models import Pessoa, Endereco


class EnderecoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Endereco
        fields = "__all__"


class PessoaSerializer(serializers.ModelSerializer):

    endereco = EnderecoSerializer(
        read_only=True,
        source="pessoa_set"
    )
    
    class Meta:
        model = Pessoa
        fields = "__all__"




