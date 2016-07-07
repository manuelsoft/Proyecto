'''
Created on 9 de jun. de 2016

@author: Rottweilas
'''
from _datetime import timezone
from _overlapped import NULL

from django.core.context_processors import request, csrf
from django.http import HttpResponse
from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response, render, \
    redirect
from django.template import loader, Context

from SistemaWeb.forms import GradoForm, SeccionForm, AulaForm, AsistenciaForm, \
    CursoForm, PerfilForm, UsuarioForm
from SistemaWeb.models import Distrito, Persona, CeAlumno, CeGrado, CeSeccion, CeDetGradsecCurso, \
    CeAula, CeAsistencia, CeCurso, CeProfesor, CeDetProfcurso, CePerfil, \
    CeUsuario, CeCatalogo , CeTutor

from .forms import PostForm, DistritoForm, PersonaForm, ProfesorForm, AlumnoForm, CursoProfesorForm
from django.contrib.auth.decorators import login_required, permission_required
from SistemaWeb.util import Parametros
from SistemaWeb.views import permisos

#Paquete Mantenimiento
@login_required
@permission_required('SistemaWeb.change_ceaula')
def mantAula(request):
    aula  = CeAula.objects.order_by('aul_pabellon')
    mi_contexto = Context({'posts':aula,'Permisos':permisos(request)})

    return render_to_response('Mantenimientos/mant_Aula.html',mi_contexto)

@login_required
def mantPersona(request):
    persona  = Persona.objects.order_by('per_nombres')
    mi_contexto = Context({'posts':persona,'Permisos':permisos(request)})

    return render_to_response('Mantenimientos/mant_Persona.html',mi_contexto)    

@login_required
@permission_required('SistemaWeb.change_ceprofesor')
def mantProfesor(request):
    
    profesor  = CeProfesor.objects.order_by('porf_gacademico')
    mi_contexto = Context({'profesores':profesor,'Permisos':permisos(request)})
    
    listaGrad = CeCatalogo.objects.filter(cat_general = Parametros.PROFESOR_GRADO_ACADEMICO)
    mi_lista = Context({'gradosAcad':listaGrad})
    return render_to_response('Mantenimientos/mant_Profesor.html',mi_contexto,mi_lista)    

@login_required
@permission_required('SistemaWeb.change_cetutor')
def mantTutor(request):
    
    tutor = CeTutor.objects.order_by(('tut_especialidad'))
    mi_contexto = Context({'tutores':tutor,'Permisos':permisos(request)}) 
    
    return render_to_response('Mantenimientos/mant_Tutor.html',mi_contexto)     

@login_required
def mantGrado(request):
    grado  = CeGrado.objects.order_by('grad_nombre')
    mi_contexto = Context({'posts':grado,'Permisos':permisos(request)})

    return render_to_response('Mantenimientos/mant_Grado.html',mi_contexto)

@login_required
@permission_required('SistemaWeb.change_ceseccion')
def mantSeccion(request):
    listaSeccion  = CeSeccion.objects.order_by('secc_nombre')
    for seccion in listaSeccion:
        catalogoTipo = CeCatalogo.objects.filter(cat_general = Parametros.SECCION_TIPO_SECCION ,cat_secundario = seccion.secc_tipo)
        tipo = catalogoTipo.get()
        seccion.secc_tipo = tipo.cat_descripcion
   
    mi_contexto = Context({'secciones':listaSeccion,'Permisos':permisos(request)})
    return render_to_response('Mantenimientos/mant_Seccion.html',mi_contexto)

@login_required
def mantAlumno(request):
    alumno  = CeAlumno.objects.order_by('cepk_per')
    mi_contexto = Context({'posts':alumno,'Permisos':permisos(request)})
  
    return render_to_response('Mantenimientos/mant_Alumno.html',mi_contexto)

@login_required
def mantDistrito(request):
    distrito  = Distrito.objects.order_by('distr_nombre')
    mi_contexto = Context({'posts':distrito,'Permisos':permisos(request)})
    
    return render_to_response('Mantenimientos/mant_Distrito.html',mi_contexto)

@login_required
@permission_required('SistemaWeb.change_cecurso')
def mantCurso(request):
    listaCursos  = CeCurso.objects.order_by('cur_nombre')
    mi_contexto = Context({'posts':listaCursos,'Permisos':permisos(request)})
    
    #Aqui traemos la decripcion del catalogo      
    for curso in listaCursos:
        catalogoTipo = CeCatalogo.objects.filter(cat_general = Parametros.CURSO_TIPO_CURSO ,cat_secundario = curso.cur_tipo)
        tipo = catalogoTipo.get()
        curso.cur_tipo = tipo.cat_descripcion
        
        catalogoEsta = CeCatalogo.objects.filter(cat_general = Parametros.CURSO_ESTADO_CURSO ,cat_secundario = curso.cur_testado)
        estado = catalogoEsta.get()
        curso.cur_testado = estado.cat_descripcion
        
    return render_to_response('Mantenimientos/mant_Curso.html',mi_contexto)