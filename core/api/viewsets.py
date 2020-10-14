from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import (
    SessionAuthentication, BasicAuthentication
)

from core.models import Pessoa, Endereco
from .permissions import GrupoApi1
from .serializers import PessoaSerializer


class PessoaViewSet(ModelViewSet):

    queryset = (
        Pessoa
        .objects
        .all()
    )
    permission_classes = (IsAuthenticated, GrupoApi1,)
    authentication_classes = (
        SessionAuthentication,
        BasicAuthentication,
    )
    serializer_class = PessoaSerializer
