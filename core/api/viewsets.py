from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated

from core.models import Pessoa
from .serializers import PessoaSerializer


class PessoaViewSet(ReadOnlyModelViewSet):

    queryset = (
        Pessoa
        .objects
        .all()
    )
    permission_classes = (IsAuthenticated,)
    lookup_field = "nome"
    serializer_class = PessoaSerializer
