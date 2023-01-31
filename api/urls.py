from rest_framework.routers import DefaultRouter
from api.views import PersonaViewSet, CatalogoViewSet, InstitucionViewSet

router = DefaultRouter()

router.register('api/persona', PersonaViewSet)
router.register('api/catalogo', CatalogoViewSet)
router.register('api/institucion', InstitucionViewSet)
#Otras rutas

urlpatterns = []

urlpatterns += router.urls
