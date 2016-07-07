'''
Created on 26 de jun. de 2016

@author: Rottweilas
'''
'''
Created on 9 de jun. de 2016

@author: Rottweilas
'''
#Paquete Operaciones

from _datetime import timezone

from django.contrib.auth.decorators import login_required, permission_required
from django.core.context_processors import request, csrf
from django.http import HttpResponse
from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response, render, \
    redirect
from django.template import loader, Context

from SistemaWeb.forms import GradoForm, SeccionForm, AulaForm, AsistenciaForm, \
    CursoForm, PerfilForm, UsuarioForm, EstadoTutorform
from SistemaWeb.models import Distrito, Persona, CeAlumno, CeGrado, CeSeccion, CeDetGradsecCurso, \
    CeAula, CeAsistencia, CeCurso, CeProfesor, CeDetProfcurso, CePerfil, \
    CeUsuario, CeCatalogo, CeTutor, CeDetGradsecTut
from SistemaWeb.util import Parametros
from SistemaWeb.views import permisos

from .forms import PostForm, DistritoForm, PersonaForm, ProfesorForm, AlumnoForm, CursoProfesorForm, EstadoProfesorForm


@login_required
@permission_required('SistemaWeb.estado_profesor')
def OpeProfesor(request):
    
    profesor  = CeProfesor.objects.order_by('porf_gacademico')
    mi_contexto = Context({'profesores':profesor})
    listaGrad = CeCatalogo.objects.filter(cat_general = Parametros.PROFESOR_GRADO_ACADEMICO)
    mi_lista = Context({'gradosAcad':listaGrad,'Permisos':permisos(request)})
    return render_to_response('Operaciones/ope_Profesor.html',mi_contexto,mi_lista)  

@login_required
@permission_required('SistemaWeb.estado_tutor')
def OpeTutor(request):
     
    tutores = CeTutor.objects.all()
    mi_contexto= Context({'tutores':tutores,'Permisos':permisos(request)})
    return render_to_response('Operaciones/ope_Tutor.html',mi_contexto)  

@login_required
@permission_required('SistemaWeb.estado_tutor')
def EstadoTutor(request,tutor_id):
    
    instance = get_object_or_404(CeTutor, cepk_tut = tutor_id)
    contexto = Context({'tutor':instance,'Permisos':permisos(request)})
    form = EstadoTutorform(request.POST or None, instance = instance)
    
    args = {}
    args.update(csrf(request))
    args['form'] = form 
    if form.is_valid():
        #Necesario
        Tut = form.save(commit=False)
#         listaEstad = CeCatalogo.objects.filter(cat_general = Parametros.TUTOR_ESTADO_TUTOR)
#        
#         for valor in listaEstad :
#             if(Tut.tut_estado == valor.cat_descripcion):
#                 Tut.tut_estado = valor.cat_secundario        
        Tut.save()
        
        return HttpResponseRedirect('/OPE/Tutor/') 
       
    return render_to_response('Operaciones/ope_EstadoTutor.html',args,contexto)
   
@login_required
@permission_required('SistemaWeb.estado_profesor')
def EstadoProfesor(request,profesor_id):
    
    instance = get_object_or_404(CeProfesor, cepk_prof = profesor_id)
    contexto = Context({'profesor':instance,'Permisos':permisos(request)})
    
    form = EstadoProfesorForm(request.POST or None, instance=instance)
    args = {}
    args.update(csrf(request))

    args['form'] = form 
    if form.is_valid():
        #Necesario    
        Prof = form.save(commit=False)
        listaEstad = CeCatalogo.objects.filter(cat_general = Parametros.PROFESOR_ESTADO_PROFESOR)
       
        for valor in listaEstad :
            if(Prof.prof_estado == valor.cat_descripcion):
                Prof.prof_estado = valor.cat_secundario        
        Prof.save()
        
        return HttpResponseRedirect('/OPE/Profesor/')
       
    return render_to_response('Operaciones/ope_EstadoProfesor.html',args,contexto)

@login_required
def ListaTutoresDes(request):
    tutores = CeTutor.objects.all()
    mi_contexto = Context({'tutores':tutores,'Permisos':permisos(request)})
    
    return render_to_response('Operaciones/ope_ListaTutoresDes.html',mi_contexto)
    
@login_required
def DesasignarGradSecTutor(request,tutor_id):

    GradSecTut = CeDetGradsecTut.objects.filter(cepk_tut=tutor_id)
    tutor = get_object_or_404(CeTutor,cepk_tut = tutor_id)
    detalle = GradSecTut
    
    if(len(GradSecTut)==0):
        flag = True
    else:
        detalle  = GradSecTut.get()
        flag = False
        
    mi_contexto = Context({'tutor':tutor,'GST':detalle,'flag':flag,'Permisos':permisos(request)})
    
    return render_to_response('Operaciones/ope_DesasignarGSTutor.html',mi_contexto)

@login_required
def DesasignarGST(request,gradSecTut_id):
    gradoSecTut = get_object_or_404(CeDetGradsecTut,cepk_detgrtut = gradSecTut_id)
    gradoSecTut.delete()
    return HttpResponseRedirect('/ListaTutorDesGS/')

@login_required
def ListaProfesoresDes(request):
    profesores = CeProfesor.objects.all()
    mi_contexto = Context({'profesores':profesores})
    listaGrad = CeCatalogo.objects.filter(cat_general = Parametros.PROFESOR_GRADO_ACADEMICO)
    mi_lista = Context({'gradosAcad':listaGrad,'Permisos':permisos(request)})
    return render_to_response('Operaciones/ope_ListaProfesoresDes.html',mi_contexto,mi_lista)
    
@login_required
def DesasignarCursoProfesor(request,profesor_id):
    
    profesor = get_object_or_404(CeProfesor,cepk_prof = profesor_id)
    GSCursoProf = CeDetProfcurso.objects.filter(cepk_prof=profesor_id)
    
    if(len(GSCursoProf)==0):
        flag = True
    else:
        flag = False
     
    mi_contexto = Context({'profesor':profesor,'GSCursoProf':GSCursoProf,'flag':flag,'Permisos':permisos(request)})
     
    return render_to_response('Operaciones/ope_DesasignarCursoProf.html',mi_contexto)

@login_required
def DesasignarCProf(request,gradCurProf_id):
    GSCursoProf = get_object_or_404(CeDetProfcurso,ecpk_detprocur=gradCurProf_id )
    GSCursoProf.delete()
    return HttpResponseRedirect('/ListaProfesorDesCur/')