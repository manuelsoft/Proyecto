from _datetime import timezone
from _overlapped import NULL

from django.contrib.auth.decorators import login_required , permission_required
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.context_processors import request, csrf
from django.http import HttpResponse
from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response, render, \
    redirect
from django.template import loader, Context
from django.template.context import RequestContext

from SistemaWeb.models import CeAlumno,CeProfesor, CeCatalogo, CeMatricula
from django.contrib.auth.decorators import login_required
from SistemaWeb.forms import MatriculaForm, MantMatriculaForm
from django.contrib.auth.models import User, Permission
from SistemaWeb.util import Parametros
from SistemaWeb.views import permisos

@login_required
@permission_required('SistemaWeb.add_cematricula')
def IniciarMatricula(request):
    #alumno  = CeAlumno.objects.order_by('cepk_alu')
    #Alumnos no matriculados
    alumno = CeAlumno.objects.filter(alu_estado = Parametros.ALUMNO_EST_NO_MATRICULADO)
    mi_contexto = Context({'alumnos':alumno,'Permisos':permisos(request)})
    listaEstado = CeCatalogo.objects.filter(cat_general = Parametros.ALUMNO_ESTADO_ALUMNO)
    mi_lista = Context({'estadosAlu':listaEstado})
    return render_to_response('Matricula/matr_Alumno.html',mi_contexto,mi_lista)

@login_required
@permission_required('SistemaWeb.add_cematricula')
def GenerarMatricula(request, alumno_id):
    instance = get_object_or_404(CeAlumno,cepk_alu = alumno_id)

    mi_contexto = Context({'alumno':instance,'Permisos':permisos(request)})
    if request.POST:
        form = MatriculaForm(request.POST)
        if form.is_valid():
            
            Matr = form.save(commit=False)
            
            listaEstad = CeCatalogo.objects.filter(cat_general = Parametros.MATRICULA_ESTADO_MATRICULA)
            for valor in listaEstad :
                if(Matr.matr_estado == valor.cat_descripcion):
                    Matr.matr_estado = valor.cat_secundario
                #Aqui a Alumno cambiamos su estado a MATRICULADO 
                #Solo Si la la Matricula se registra como Actualizada
                if(Matr.matr_estado == Parametros.MATRICULA_EST_ACTUALIZADA):
                    CeAlumno.objects.filter(cepk_alu = alumno_id ).update(alu_estado=Parametros.ALUMNO_EST_MATRICULADO)
                    
            Matr.cepk_alu = instance
            Matr.save()
            return HttpResponseRedirect('/IniciarMatricula/')
    else:
        form = MatriculaForm()
        
    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('Matricula/matr_MostrarAlumno.html',args,mi_contexto)

@login_required
@permission_required('SistemaWeb.delete_cematricula')
def IniciarAnularMatricula(request):
    
    listaMatriculas = CeMatricula.objects.filter(matr_estado = Parametros.MATRICULA_EST_ACTUALIZADA)
    matriculas = Context({'matriculas':listaMatriculas,'Permisos':permisos(request)})
    print("Aqui entro"+ str(permisos(request)))
          
    for matricula in listaMatriculas:
        catalogoTipo = CeCatalogo.objects.filter(cat_general = Parametros.MATRICULA_ESTADO_MATRICULA ,cat_secundario = matricula.matr_estado)
        tipo = catalogoTipo.get()
        matricula.matr_estado = tipo.cat_descripcion
    return render_to_response('Matricula/matr_AnularMatricula.html',matriculas)

@login_required
@permission_required('SistemaWeb.delete_cematricula')
def AnularMatricula(request,alumno_id,matricula_id):
    
    matricula_anular = get_object_or_404(CeMatricula,cepk_matr = matricula_id)
    alumno_anular = get_object_or_404(CeAlumno,cepk_alu = alumno_id)
  
    catalogoEstadoMatr = CeCatalogo.objects.filter(cat_general = Parametros.MATRICULA_ESTADO_MATRICULA ,cat_secundario = matricula_anular.matr_estado)
    estMatr = catalogoEstadoMatr.get()
    matricula_anular.matr_estado = estMatr.cat_descripcion
    
    catalogoEstadoAlu = CeCatalogo.objects.filter(cat_general = Parametros.ALUMNO_ESTADO_ALUMNO ,cat_secundario = alumno_anular.alu_estado)
    estAlu = catalogoEstadoAlu.get()
    alumno_anular.alu_estado = estAlu.cat_descripcion
    
    matr_context = Context({'matricula':matricula_anular})
   
   
    alum_context = Context({'alumno':alumno_anular,'Permisos':permisos(request)})
    
    return render_to_response('Matricula/matr_Anulando.html',matr_context,alum_context)

@login_required
@permission_required('SistemaWeb.delete_cematricula')    
def Anulalo_Matricula(request,alumno_id,matricula_id):
   
    CeAlumno.objects.filter(cepk_alu = alumno_id ).update(alu_estado=Parametros.ALUMNO_EST_NO_MATRICULADO)
    CeMatricula.objects.filter(cepk_matr = matricula_id).update(matr_estado = Parametros.MATRICULA_EST_NO_ACTUALIZADA)
        
    return HttpResponseRedirect('/IniciarMatricula/')

@login_required
@permission_required('SistemaWeb.change_cematricula')    
def IniciarMantenerMatricula(request):
    listaMatriculas = CeMatricula.objects.filter(matr_estado = Parametros.MATRICULA_EST_ACTUALIZADA)
    for matricula in listaMatriculas:
        estado  = CeCatalogo.objects.filter(cat_general = Parametros.MATRICULA_ESTADO_MATRICULA ,cat_secundario = matricula.matr_estado)
        matricula.matr_estado = estado.get().cat_descripcion
        
    matriculas = Context({'matriculas':listaMatriculas,'Permisos':permisos(request)})
    
    return render_to_response('Matricula/matr_MantenerMatricula.html',matriculas)

@login_required
@permission_required('SistemaWeb.change_cematricula')    
def MantenerMatricula(request,matricula_id):
    instance = get_object_or_404(CeMatricula, cepk_matr = matricula_id)    
    
    mantForm = MantMatriculaForm(request.POST or None, instance = instance)
    args = {}
    args.update(csrf(request))

    args['form'] = mantForm 
    if mantForm.is_valid():
        mantForm.save()
        return HttpResponseRedirect('/MantenerMatricula/')
        
    contexto = Context({'Permisos':permisos(request)})
    
    return render_to_response('Matricula/matr_MantenerMatricula_Form.html',args,contexto)