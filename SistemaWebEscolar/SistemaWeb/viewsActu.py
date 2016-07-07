'''
Created on 9 de jun. de 2016

@author: Rottweilas
'''
from _datetime import timezone
from _overlapped import NULL

from django.contrib.auth.decorators import login_required
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
    CeUsuario, CeCatalogo,CeTutor

from .forms import PostForm, DistritoForm, PersonaForm, ProfesorForm, AlumnoForm, CursoProfesorForm
from django.contrib.auth.decorators import login_required
from SistemaWeb.util import Parametros
from SistemaWeb.views import permisos

@login_required
def ActualizarDistrito(request, distrito_id):
    instance = get_object_or_404(Distrito, cepk_distrito = distrito_id)
    form = DistritoForm(request.POST or None, instance=instance)
    args = {}
    args.update(csrf(request))

    args['form'] = form 
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/MAN/Distrito/')
    contexto = Context({'Permisos':permisos(request)})
    return render_to_response('Mantenimientos/Actualizaciones/ActualizarDistrito.html',args,contexto)

@login_required
def ActulizarDatosTutor(request, tutor_id):

    instance = get_object_or_404(CeTutor, cepk_tut = tutor_id)    
    global tutor
    tutor = instance
    
    i_persona = get_object_or_404(Persona, cepk_per = instance.cepk_per.cepk_per)
    
    persForm = PersonaForm(request.POST or None, instance = i_persona)
    args = {}
    args.update(csrf(request))

    args['form'] = persForm 
    if persForm.is_valid():
        persForm.save()
        return HttpResponseRedirect('/ActualizarTutor/')
    contexto = Context({'Permisos':permisos(request)})    
    return render_to_response('Mantenimientos/Actualizaciones/ActualizarDatosTutor.html',args,contexto)

@login_required
def ActualizarTutor(request):
     
    global tutor
    form = TutorForm(request.POST or None, instance=tutor)
    args = {}   
    args.update(csrf(request))

    args['form'] = form 
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/MAN/Tutor/')
    contexto = Context({'Permisos':permisos(request)})   
    return render_to_response('Mantenimientos/Actualizaciones/ActualizarTutor.html',args,contexto)

@login_required
def ActulizarDatosProfesor(request, profesor_id):
    
    instance = get_object_or_404(CeProfesor, cepk_prof = profesor_id)
    global profesor
    profesor = instance
    i_persona = get_object_or_404(Persona, cepk_per = instance.cepk_per.cepk_per)
    
    persForm = PersonaForm(request.POST or None, instance = i_persona)
    args = {}
    args.update(csrf(request))

    args['form'] = persForm 
    if persForm.is_valid():
        persForm.save()
        return HttpResponseRedirect('/ActualizarProfesor/')
    contexto = Context({'Permisos':permisos(request)})       
    return render_to_response('Mantenimientos/Actualizaciones/ActualizarDatosProfesor.html',args,contexto)

@login_required
def ActualizarProfesor(request):
    
    global profesor
    form = ProfesorForm(request.POST or None, instance=profesor)
    args = {}
    args.update(csrf(request))
    
    args['form'] = form 
    if form.is_valid():
        Prof = form.save(commit=False)
        listaTProf = CeCatalogo.objects.filter(cat_general = Parametros.PROFESOR_TIPO_PROFESOR)
        listaGAcad = CeCatalogo.objects.filter(cat_general = Parametros.PROFESOR_GRADO_ACADEMICO)
        listaEstad = CeCatalogo.objects.filter(cat_general = Parametros.PROFESOR_ESTADO_PROFESOR)
            
        for valor in listaTProf :
            if(Prof.prof_tipo == valor.cat_descripcion):
                Prof.prof_tipo = valor.cat_secundario
        for valor in listaGAcad :
            if(Prof.porf_gacademico == valor.cat_descripcion):
                Prof.porf_gacademico = valor.cat_secundario
        for valor in listaEstad :
            if(Prof.prof_estado == valor.cat_descripcion):
                Prof.prof_estado = valor.cat_secundario
                    
        form.save()
        return HttpResponseRedirect('/MAN/Profesor/')
    contexto = Context({'Permisos':permisos(request)})     
    return render_to_response('Mantenimientos/Actualizaciones/ActualizarProfesor.html',args,contexto)

@login_required
def ActualizarCurso(request, curso_id):
    
    instance = get_object_or_404(CeCurso, cepk_cur = curso_id)
    
    curForm = CursoForm(request.POST or None, instance = instance)
    args = {}
    args.update(csrf(request))

    args['form'] = curForm 
    if curForm.is_valid():
        curForm.save()
        return HttpResponseRedirect('/MAN/Curso/')
    contexto = Context({'Permisos':permisos(request)})       
    return render_to_response('Mantenimientos/Actualizaciones/ActualizarCurso.html',args,contexto)

@login_required
def ActualizarSeccion(request, seccion_id):
    
    instance = get_object_or_404(CeSeccion, cepk_secc = seccion_id)
    
    seccForm = SeccionForm(request.POST or None, instance = instance)
    args = {}
    args.update(csrf(request))

    args['form'] = seccForm 
    if seccForm.is_valid():
        seccForm.save()
        return HttpResponseRedirect('/MAN/Seccion/')
    contexto = Context({'Permisos':permisos(request)})  
    return render_to_response('Mantenimientos/Actualizaciones/ActualizarSeccion.html',args,contexto)
