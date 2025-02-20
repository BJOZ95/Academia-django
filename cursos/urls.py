from django.urls import path
from .views import (Registro_user_view, CustomLoginView, ListaCursosView,
                    DetalleCursoView,CrearCursoView, InscribirCursoView,
                    CustomLogoutView, MisCursosView )
urlpatterns = [
    path('', ListaCursosView.as_view(), name='cursos'),
    path('registro/', Registro_user_view.as_view(), name='registro'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('curso/<int:pk>/', DetalleCursoView.as_view(), name='detalleCurso'),
    path('curso/crear', CrearCursoView.as_view(), name='crear_curso'),
    path('mis_cursos/', MisCursosView.as_view(), name='mis_cursos'),
    path('curso/pk/<int:pk>/inscribir', InscribirCursoView.as_view(), name='inscribir_curso')]