'''
Created on 9 de jun. de 2016

@author: Rottweilas
'''
from _datetime import timezone
from _overlapped import NULL
import urllib

from django.contrib.auth.decorators import login_required, permission_required
from django.core.context_processors import request, csrf
from django.http import HttpResponse
from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response, render, \
    redirect
from django.template import loader, Context

from SistemaWeb.forms import GradoForm, SeccionForm, AulaForm, AsistenciaForm, \
    CursoForm, PerfilForm, UsuarioForm, TutorForm
from SistemaWeb.models import Distrito, Persona, CeAlumno, CeGrado, CeSeccion, CeDetGradsecCurso, \
    CeAula, CeAsistencia, CeCurso, CeProfesor, CeDetProfcurso, CePerfil, \
    CeUsuario, CeCatalogo

from .forms import PostForm, DistritoForm, PersonaForm, ProfesorForm, AlumnoForm, CursoProfesorForm
from builtins import int
from SistemaWeb.util import Parametros
from SistemaWeb.views import permisos

persona = Persona


@login_required
def registrarPersonaAlumno(request):
    persona  = Persona.objects.order_by('per_nombres')
    mi_contexto = Context({'posts':persona,'Permisos':permisos(request)})
    if request.POST:
        form = PersonaForm(request.POST)
        if form.is_valid():
            Per = form.save(commit=False)
            #Guardamos en persona el From de Persona
            global persona
            persona = Per
            return HttpResponseRedirect('/REG/Alumno/')    
    else:
        form = PersonaForm()
    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('Registros/reg_DatosPersAlumno.html', args,mi_contexto)    

@login_required
def regAlumno(request):
 
    if request.POST:
        form = AlumnoForm(request.POST)
        if form.is_valid():
            Alum = form.save(commit=False)
            #Guardamos Persona y Alumno Juntos
            #Guardamos al alumno como no matriculado por defecto
            Alum.alu_estado = Parametros.ALUMNO_EST_NO_MATRICULADO
            global persona
            persona.save()
            global persona
            Alum.cepk_per = persona
            Alum.save()
            return redirect('matricula',alumno_id = Alum.cepk_alu)
    else:
        form = AlumnoForm()
        
    args = {}
    args.update(csrf(request))

    args['form'] = form
    contexto=Context({'Permisos':permisos(request)})
    return render_to_response('Registros/reg_Alumno.html', args,contexto)

@login_required
@permission_required('SistemaWeb.add_ceprofesor')
def registrarPersonaProfesor(request):
    persona  = Persona.objects.order_by('per_nombres')
    mi_contexto = Context({'posts':persona,'Permisos':permisos(request)})
    if request.POST:
        form = PersonaForm(request.POST)
        if form.is_valid():
            Per = form.save(commit=False)
            #Guardamos en persona el From de Persona
            global persona
            persona = Per
            return HttpResponseRedirect('/REG/Profesor/')    
    else:
        form = PersonaForm()
    args = {}
    args.update(csrf(request))

    args['form'] = form
    return render_to_response('Registros/reg_DatosPersProfesor.html', args,mi_contexto) 

@login_required
@permission_required('SistemaWeb.add_cetutor')
def registrarPersonaTutor(request):

    if request.POST:
        form = PersonaForm(request.POST)
        if form.is_valid():
            Per = form.save(commit=False)
            
            global persona
            persona = Per
            return HttpResponseRedirect('/REG/Tutor/')
    else:
        form = PersonaForm()
        
    args = {}
    args.update(csrf(request))
    args['form'] = form
    contexto=Context({'Permisos':permisos(request)})
    return render_to_response('Registros/reg_DatosPersTutor.html', args,contexto) 

@login_required
@permission_required('SistemaWeb.add_ceprofesor')
def regProfesor(request):
 
    if request.POST:
        form = ProfesorForm(request.POST)
        if form.is_valid():
            Prof = form.save(commit=False)
            global persona
            persona.save()
            #
            global persona
            Prof.cepk_per = persona
            Prof.save()
            return HttpResponseRedirect('/REG/DatosPersProfesor/')
    else:
        form = ProfesorForm()
        
    args = {}
    args.update(csrf(request))

    args['form'] = form
    contexto=Context({'Permisos':permisos(request)})
    return render_to_response('Registros/reg_Profesor.html', args,contexto)    

@login_required
@permission_required('SistemaWeb.add_cetutor')
def regTutor(request):
    
    if request.POST:
        form = TutorForm(request.POST)
        if form.is_valid():
            Tutor = form.save(commit=False)
            global persona
            persona.save()
            
            global persona
            Tutor.cepk_per = persona
            Tutor.save()
            return HttpResponseRedirect('/REG/DatosPersTutor')
    else:
        form = TutorForm()
        
    args = {}
    args.update(csrf(request))
    
    args['form'] = form
    contexto=Context({'Permisos':permisos(request)})
    return render_to_response('Registros/reg_Tutor.html',args,contexto)   

@login_required
@permission_required('SistemaWeb.add_cecurso')
def regCurso(request):

    if request.POST:
        form = CursoForm(request.POST)
        if form.is_valid():
            curso = form.save(commit = False)
            
            listaTCur = CeCatalogo.objects.filter(cat_general = Parametros.CURSO_TIPO_CURSO)
            listaECur = CeCatalogo.objects.filter(cat_general = Parametros.CURSO_ESTADO_CURSO)
            
            for valor in listaTCur :
                if(curso.cur_tipo == valor.cat_descripcion):
                    curso.cur_tipo = valor.cat_secundario
            for valor in listaECur :
                if(curso.cur_testado == valor.cat_descripcion):
                    curso.cur_testado = valor.cat_secundario
            curso.save()
            return HttpResponseRedirect('.')
    else:
        form = CursoForm()
    args = {}
    args.update(csrf(request))

    args['form'] = form
    contexto=Context({'Permisos':permisos(request)})
    return render_to_response('Registros/reg_Curso.html', args,contexto)

@login_required
@permission_required('SistemaWeb.add_ceseccion')
def regSeccion(request):

    if request.POST:
        form = SeccionForm(request.POST)
        if form.is_valid():
            secc= form.save(commit=False)
            
            listaTSecc = CeCatalogo.objects.filter(cat_general = Parametros.SECCION_TIPO_SECCION)
            
            for valor in listaTSecc :
                if(secc.secc_tipo == valor.cat_descripcion):
                    secc.secc_tipo = valor.cat_secundario
            
            secc.save()
            return HttpResponseRedirect('.')
    else:
        form = SeccionForm()
        
    args = {}
    args.update(csrf(request))
    
    args['form'] = form
    contexto=Context({'Permisos':permisos(request)})
    return render_to_response('Registros/reg_Seccion.html', args,contexto)