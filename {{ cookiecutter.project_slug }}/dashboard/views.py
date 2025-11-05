from django.views.generic import TemplateView
from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

User = get_user_model()

class DashboardHomeView(TemplateView):
    template_name = "dashboard/home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_users'] = User.objects.count()
        return context

@method_decorator(cache_page(60 * 15), name='dispatch')  # Cache por 15 minutos
@method_decorator(vary_on_cookie, name='dispatch')
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint para visualização e edição de usuários
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(username__icontains=username)
        return queryset
