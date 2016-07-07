'''
Created on 9 de jun. de 2016

@author: Rottweilas
'''
from _datetime import timezone
from _overlapped import NULL

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
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
    CeUsuario, CeCatalogo , CeTutor, CeDetGradsecTut, CeMatricula

from .forms import PostForm, DistritoForm, PersonaForm, ProfesorForm, AlumnoForm, CursoProfesorForm
from SistemaWeb.util import Parametros
from SistemaWeb.views import permisos


@login_required
@permission_required('SistemaWeb.consultar_ceprofesor')
def cnsProfesor(request):
    
    profesor  = CeProfesor.objects.order_by('porf_gacademico')
    mi_contexto = Context({'profesores':profesor})
    listaGrad = CeCatalogo.objects.filter(cat_general = Parametros.PROFESOR_GRADO_ACADEMICO)
    mi_lista = Context({'gradosAcad':listaGrad,'Permisos':permisos(request)})
    return render_to_response('Consultas/cns_Profesor.html',mi_contexto,mi_lista)  

@login_required
@permission_required('SistemaWeb.consultar_ceprofesor')
def cns_Profesor(request,profesor_id):
    profesor  = get_object_or_404(CeProfesor,cepk_prof = profesor_id)
    
    listaTProf = CeCatalogo.objects.filter(cat_general = Parametros.PROFESOR_TIPO_PROFESOR)
    listaGAcad = CeCatalogo.objects.filter(cat_general = Parametros.PROFESOR_GRADO_ACADEMICO)
    listaEstad = CeCatalogo.objects.filter(cat_general = Parametros.PROFESOR_ESTADO_PROFESOR)
            
    for valor in listaTProf :
        if(profesor.prof_tipo == valor.cat_secundario):
            profesor.prof_tipo = valor.cat_descripcion
    #Pasamos a String par apoder Comparar
    for valor in listaGAcad :
        if(profesor.porf_gacademico == str(valor.cat_secundario)):
            profesor.porf_gacademico = valor.cat_descripcion
    for valor in listaEstad :
        if(profesor.prof_estado == valor.cat_secundario):
            profesor.prof_estado = valor.cat_descripcion
            
    mi_contexto = Context({'profesor':profesor,'Permisos':permisos(request)})
   
    return render_to_response('Consultas/cns_DatosProfesor.html',mi_contexto)  

@login_required
@permission_required('SistemaWeb.consultar_cetutor')
def cnsTutor(request):
    
    tutores  = CeTutor.objects.order_by('tut_especialidad')
    mi_contexto = Context({'Permisos':permisos(request),'tutores':tutores})
    return render_to_response('Consultas/cns_Tutor.html',mi_contexto)  

@login_required
@permission_required('SistemaWeb.consultar_cetutor')
def cns_Tutor(request,tutor_id):
    tutor  = get_object_or_404(CeTutor,cepk_tut= tutor_id)
    
    estado = CeCatalogo.objects.filter(cat_general = Parametros.TUTOR_ESTADO_TUTOR ,cat_secundario = tutor.tut_estado)
    tutor.tut_estado = estado.get().cat_descripcion
    mi_contexto = Context({'tutor':tutor,'Permisos':permisos(request)})
    
    return render_to_response('Consultas/cns_DatosTutor.html',mi_contexto)  

@login_required
@permission_required('SistemaWeb.consultar_cealumno')
def cnsAlumno(request):
    
    listaAlumno  = CeAlumno.objects.order_by('cepk_alu')
    
    for alumno in listaAlumno:
        estado = CeCatalogo.objects.filter(cat_general = Parametros.ALUMNO_ESTADO_ALUMNO ,cat_secundario = alumno.alu_estado)
        alumno.alu_estado = estado.get().cat_descripcion
        
    mi_contexto = Context({'alumnos':listaAlumno,'Permisos':permisos(request)})

    return render_to_response('Consultas/cns_Alumno.html',mi_contexto)

@login_required
@permission_required('SistemaWeb.consultar_cealumno')
def cns_Alumno(request,alumno_id):
    
    alumno  = get_object_or_404(CeAlumno,cepk_alu = alumno_id)
    
    listaMatriculaNoActu = CeMatricula.objects.filter(cepk_alu = alumno_id,matr_estado = Parametros.MATRICULA_EST_NO_ACTUALIZADA)
    listaMatriculaActu = CeMatricula.objects.filter(cepk_alu = alumno_id,matr_estado = Parametros.MATRICULA_EST_ACTUALIZADA)
    
    matricula = 0
    
    flagMatricula = False
    flagListaMatricula = False
    
    if(len(listaMatriculaActu) > 0):  
        matricula = listaMatriculaActu.get()  
        estado = CeCatalogo.objects.filter(cat_general = Parametros.MATRICULA_ESTADO_MATRICULA ,cat_secundario = matricula.matr_estado)
        matricula.matr_estado = estado.get().cat_descripcion
        flagMatricula = True
    #print(str(matricula) +".."+ str(len(listaMatriculaActu)))
    
    for matr in listaMatriculaNoActu:
        estado = CeCatalogo.objects.filter(cat_general = Parametros.MATRICULA_ESTADO_MATRICULA ,cat_secundario = matr.matr_estado)
        matr.matr_estado = estado.get().cat_descripcion
        flagListaMatricula = True
    mi_contexto = Context({'alumno':alumno,'matricula':matricula,'listaMatricula':listaMatriculaNoActu,'flagLista':flagListaMatricula,'flag':flagMatricula,'Permisos':permisos(request)})
    
    return render_to_response('Consultas/cns_DetAlumno.html',mi_contexto)       

@login_required
@permission_required('auth.consultar_ceusuario')
def cnsUsuario(request):
    
    usuarios  = User.objects.all()
    mi_contexto = Context({'profesores':usuarios,'Permisos':permisos(request)})

    return render_to_response('Consultas/cns_Usuario.html',mi_contexto) 

@login_required
@permission_required('SistemaWeb.consultar_ceProfCur')
def cnsProfesorCurso(request):
    listaProfesores = CeProfesor.objects.order_by('porf_gacademico')
   
    for prof in listaProfesores:
        tipo= CeCatalogo.objects.filter(cat_general = Parametros.PROFESOR_TIPO_PROFESOR ,cat_secundario = prof.prof_tipo)
        prof.prof_tipo= tipo.get().cat_descripcion
        
        gradoAcad = CeCatalogo.objects.filter(cat_general = Parametros.PROFESOR_GRADO_ACADEMICO ,cat_secundario = prof.porf_gacademico)
        prof.porf_gacademico = gradoAcad.get().cat_descripcion
        
        estad = CeCatalogo.objects.filter(cat_general = Parametros.PROFESOR_ESTADO_PROFESOR ,cat_secundario = prof.prof_estado)
        prof.prof_estado = estad.get().cat_descripcion
        
    mi_contexto = Context({'dets':listaProfesores,'Permisos':permisos(request)})   
    
    return render_to_response('Consultas/cns_ProfesorCurso.html',mi_contexto)

@login_required
def cnsTutorGradSec(request):
    listaTutores = CeTutor.objects.all()
    mi_contexto = Context({'tut':listaTutores,'Permisos':permisos(request)})
    return render_to_response('Consultas/cns_GradSecTutor.html',mi_contexto)

@login_required
@permission_required('SistemaWeb.consultar_ceProfCur')
def cns_Det_ProfesorCurso(request,profesor_id):   
    profesor = CeProfesor.objects.get(cepk_prof = profesor_id)
    estado = CeCatalogo.objects.filter(cat_general = Parametros.PROFESOR_ESTADO_PROFESOR ,cat_secundario = profesor.prof_estado) 
    profesor.prof_estado = estado.get().cat_descripcion
    
    listaCursoProf = CeDetProfcurso.objects.filter(cepk_prof = profesor_id)
    
    for d in listaCursoProf:
        tipo = CeCatalogo.objects.filter(cat_general = Parametros.CURSO_TIPO_CURSO ,cat_secundario = d.cepk_detgrcur.cepk_cur.cur_tipo) 
        d.cepk_detgrcur.cepk_cur.cur_tipo = tipo.get().cat_descripcion
        
    if(len(listaCursoProf)==0):
        vacio = True
    else:
        vacio = False
    #cursoGradoSecc = CeDetGradsecCurso.objects.filter(cepk_detgrcur = listaCursoProf.get().cepk_detgrcur).values().distinct()
    
    contexto = Context({"listCursos":listaCursoProf,"flag":vacio,"profesor":profesor,'Permisos':permisos(request)})  
    
    return render_to_response('Consultas/cns_CursosDeProfesor.html',contexto)

def cns_Det_TutorCurso(request,tutor_id):
    tutor = CeTutor.objects.get(cepk_tut = tutor_id)
    listaGradSecTut = CeDetGradsecTut.objects.filter(cepk_tut = tutor_id)
    
    for x in listaGradSecTut:
        estado = CeCatalogo.objects.filter(cat_general = Parametros.TUTOR_ESTADO_TUTOR,cat_secundario = x.cepk_tut.tut_estado)
        tipo = estado.get()
        tutor.tut_estado = tipo.cat_descripcion
        
    if(len(listaGradSecTut)==0):
        vacio = True
    else:
        vacio = False
        
    contexto = Context({"listaGradSecTut":listaGradSecTut,"flag":vacio,"tutor":tutor,'Permisos':permisos(request)})
        
    return render_to_response('Consultas/cns_GradSecDeTutor.html',contexto)   

def cnsCursoGradoSecc(request):
    lista = CeDetGradsecCurso.objects.all()
    contexto =({'listaDet':lista,'Permisos':permisos(request)})
    
    return render_to_response('Consultas/cns_CursosGradosSeccion.html',contexto)   

def cnsDetCursoGradoSecc(request,det_id):
    detalle = get_object_or_404(CeDetGradsecCurso,cepk_detgrcur = det_id)
    
    estadoCur = detalle.cepk_cur.cur_testado
    tipoCur = detalle.cepk_cur.cur_tipo
    tipoSecc = detalle.cepk_gradsec.cepk_secc.secc_tipo
    
    estadoCurResult = CeCatalogo.objects.filter(cat_general = Parametros.CURSO_ESTADO_CURSO,cat_secundario = estadoCur)
    detalle.cepk_cur.cur_testado = estadoCurResult.get().cat_descripcion
    
    tipoCurResult = CeCatalogo.objects.filter(cat_general = Parametros.CURSO_TIPO_CURSO,cat_secundario = tipoCur)
    detalle.cepk_cur.cur_tipo =  tipoCurResult.get().cat_descripcion
    
    tipoSeccResult = CeCatalogo.objects.filter(cat_general = Parametros.SECCION_TIPO_SECCION,cat_secundario = tipoSecc)
    detalle.cepk_gradsec.cepk_secc.secc_tipo =  tipoSeccResult.get().cat_descripcion
    
    contexto = Context({'detalle':detalle,'Permisos':permisos(request)})
    
    return render_to_response('Consultas/cns_DetalleCursosGradosSeccion.html',contexto)   
