from rest_framework import viewsets
from .models import Morador, Domicilio, Falecido
from .serializers import MoradorSerializer, DomicilioSerializer, FalecidoSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class MoradorViewSet(viewsets.ModelViewSet):
    queryset = Morador.objects.all()
    serializer_class = MoradorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
    
class DomicilioViewSet(viewsets.ModelViewSet):
    queryset = Domicilio.objects.all()
    serializer_class = DomicilioSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class FalecidoViewSet(viewsets.ModelViewSet):
    queryset = Falecido.objects.all()
    serializer_class = FalecidoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)