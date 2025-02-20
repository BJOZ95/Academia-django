from http.client import responses
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, DetailView
from django.contrib import messages
from django.shortcuts import redirect
from cursos.forms import Registro_user_form, Curso_form
from cursos.models import Curso


class ListaCursosView(LoginRequiredMixin, ListView):
    model = Curso
    template_name = 'cursos/cursos.html'

    context_object_name = 'cursos'

    def get_queryset(self):
        if self.request.user.rol=='admin':
            return Curso.objects.all()
        else:
            return Curso.objects.filter(estado='true')



class CustomLoginView(LoginView):
    template_name = 'registro/login.html'

    def form_valid(self, form):
        messages.error(self.request, 'Usuario o Contraseña incorrectos')
        return super().form_valid(form)

class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'Sesión cerrada correctamente')
        response = redirect('login')
        response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response['Pragma'] = 'no-cache'
        response['Expires'] = '0'
        return response



class Registro_user_view(CreateView):
    form_class = Registro_user_form
    template_name = 'registro/registro.html'
    success_url = reverse_lazy('cursos/cursos.html')

    def form_valid(self, form):
        response=super().form_valid(form)
        login(self.request, self.object)
        messages.success(self.request, 'Usuario registrado Correctamente')
        return response

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error, f"{field}: {error}")
        return super().form_invalid(form)

class DetalleCursoView(LoginRequiredMixin, DetailView):
    model = Curso
    template_name = 'cursos/detalle_curso.html'
    context_object_name = 'curso'

class InscribirCursoView(LoginRequiredMixin, DetailView):
    model = Curso

    def get(self, request, *args, **kwargs):
        curso = self.get_object()
        if request.user not in curso.inscritos.all() and curso.inscritos.count()< curso.cupos:
            curso.inscritos.add(request.user)
            messages.success(request, 'Inscrito correctamente')
        else:
            messages.error(request, 'No se puedo completar el proceso')
        response = redirect('detalle_curso', pk=curso.pk)

class CrearCursoView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Curso
    form_class = Curso_form
    template_name = 'cursos/form_curso.html'
    success_url = reverse_lazy('cursos/cursos.html')

    def test_func(self):
        return self.request.user.rol=='admin'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Curso creado correctamente')
        return response


class MisCursosView(LoginRequiredMixin, ListView):
    model = Curso
    template_name = 'cursos/cursos.html'
    context_object_name = 'cursos'

    def get_queryset(self):
        return self.request.user.cursos.inscritos.all()







