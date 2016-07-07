from _datetime import timezone


from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required , permission_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.context_processors import request, csrf
from django.http import HttpResponse
from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response, render, \
    redirect
from django.template import loader, Context
from django.template.context import RequestContext

from SistemaWeb.forms import GradoForm, AulaForm, AsistenciaForm, \
    CursoForm, PerfilForm, UsuarioForm, CursoSeccGradForm
from SistemaWeb.models import Distrito, Persona, CeAlumno, CeGrado, CeSeccion, CeDetGradsecCurso, \
    CeAula, CeAsistencia, CeCurso, CeProfesor, CeDetProfcurso, CePerfil, \
    CeUsuario, CeDetGradsecc, CeCatalogo, CeTutor, CeDetGradsecTut
from SistemaWeb.util import Parametros
from SistemaWeb.util.Parametros import TUTOR_ESTADO_TUTOR
import SistemaWebEscolar

from .forms import PostForm, DistritoForm, PersonaForm, ProfesorForm, AlumnoForm, CursoProfesorForm


#PARA EL LOGIN
# Create your views here.
#request --> El primer parametro y devuelve un objeto hhtpResponse valido
id_distrito  = 0
id_profesor = 0
id_curso = 0

id_seccion = 0

def permisos(request):
    PermisosUsuario = request.user.get_all_permissions()
    return PermisosUsuario

def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            username = request.POST.get('username')
            password = request.POST.get('password')
            print (username,password)
            user = authenticate(username=username , password=password)
        
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/inicio/')
                else:
                    return HttpResponseRedirect("Tu cuenta esta inactiva.")
        
            else:
                return HttpResponse("Tu usuario o contrasenia es incorrecta.")   

    return render_to_response('login.html',{'Permisos':permisos(request)},context)

def user_logout(request):
    logout(request)
    
    if request.user.is_authenticated():
        print("ingreso")
    else:
        print("no ingreso")  
        
    return HttpResponseRedirect('/login/')

@login_required
def indexprueba(request):
    distrito  = Distrito.objects.all()
    persona = Persona.objects.all()
    mi_template = loader.get_template("index.html")
    mi_contexto = Context({'posts':distrito,'posts2':persona})
    return HttpResponse(mi_template.render(mi_contexto))

@login_required
def articles(request):
    distrito  = Distrito.objects.all()
    mi_contexto = Context({'posts':distrito})
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('Pruebas/post_detail', cepk_distrito=post.cepk_distrito)
    else:
        form = PostForm()
    return render(request, 'Pruebas/post_detail.html', {'form': form})

#Pasando String
@login_required
def prueba(request):
    caso = Distrito.objects.order_by('distr_nombre')
    caso_string = "Distritos <br/>"
    caso_string += '<br/>'.join(["Departamento:%s -- Nombre:%s"%
    (d.distr_departamento,d.distr_nombre) for d in caso])
    return HttpResponse(caso_string)
@login_required
def prueba2(request,distrito_id):
    try:
        caso = Distrito.objects.get(cepk_distrito=distrito_id)
    except Distrito.DoesNotExist:
        raise Http404
        #return HttpResponse("No existe distrito identificado con  = "+distrito_id)
    return HttpResponse("%s" % caso.distr_nombre)

#Reduce codigo anterior de prueba2
@login_required
def prueba3(request,distrito_id):
    caso = get_object_or_404(Distrito,cepk_distrito=distrito_id)
    return HttpResponse("%s" % caso.distr_nombre)

###########################################
@login_required
def prueba4(request):
    caso = Distrito.objects.all()
    return render_to_response('Pruebas/ejemplosprueba.html',{'distritos':caso})

@login_required
def prueba5(request,distrito_id):
    caso = get_object_or_404(Distrito,cepk_distrito=distrito_id)
    global id_distrito 
    id_distrito = distrito_id
    cursos = CeCurso.objects.all()
    mi_contexto = Context({'cursos':cursos})
    
    return render_to_response('Pruebas/ejemplo.html',{'distrito':caso},mi_contexto)

@login_required
def prueba6(request,curso_id):
    caso = get_object_or_404(CeCurso,cepk_cur=curso_id)
    distrito = get_object_or_404(Distrito,cepk_distrito = id_distrito)
    mi_contexto = Context({'distrito':distrito})
    return render_to_response('Pruebas/ejemploCurso.html',{'curso':caso},mi_contexto)
###########################################

###########################################

@login_required
def NuevoDistrito(request):
    form = PostForm()
    distrito  = Distrito.objects.all()
    mi_contexto = Context({'posts':distrito})
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('inicio')
    else:
        form = PostForm()
    return  render_to_response('Pruebas/post_edit.html', {'form': form},mi_contexto)

@login_required
def post_detail(request):
    return  render(request, 'Pruebas/post_detail.html')



#Paquete Mantenimiento

@login_required
def newAula(request):
    aula  = CeAula.objects.order_by('aul_pabellon')
    mi_contexto = Context({'posts':aula,'Permisos':permisos(request)})
    if request.POST:
        form = AulaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/newAula/')
    else:
        form = AulaForm()
    args = {}
    args.update(csrf(request))

    args['form'] = form
 
    return render_to_response('Mantenimientos/mant_Aula.html', args,mi_contexto)

@login_required
def newDistrito(request):
    distrito  = Distrito.objects.order_by('distr_nombre')
    mi_contexto = Context({'posts':distrito,'Permisos':permisos(request)})
    if request.POST:
        form = DistritoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/newDistrito/')
    else:
        form = DistritoForm()
    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('Mantenimientos/mant_Distrito.html', args,mi_contexto)    

@login_required
def newPersona(request):
    persona  = Persona.objects.order_by('per_nombres')
    mi_contexto = Context({'posts':persona,'Permisos':permisos(request)})
    if request.POST:
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/newPersona/')
    else:
        form = PersonaForm()
    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('Mantenimientos/mant_Persona.html', args,mi_contexto)    

@login_required
def newProfesor(request):
    
    profesor  = CeProfesor.objects.order_by('porf_gacademico')
    mi_contexto = Context({'profesores':profesor,'Permisos':permisos(request)})
    if request.POST:
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/newProfesor/')
    else:
        form = ProfesorForm()
    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('Operaciones/ope_Profesor.html', args,mi_contexto)    

@login_required
def newPerfil(request):
    perfil = CePerfil.objects.order_by('perf_tperfil');
    mi_contexto = Context({'posts':perfil,'Permisos':permisos(request)})
    if request.POST:
        form = PerfilForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/newPerfil')
    else:
        form = PerfilForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    
    return render_to_response('Operaciones/ope_Perfil.html',args,mi_contexto)

@login_required
@permission_required('auth.add_user')
def newUsuario(request):    
    contexto = RequestContext(request)
   
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/newUsuario/')
    else:
        form = UserCreationForm()
        cont = Context({'Permisos':permisos(request),'formulario' :form})
    return render_to_response('Operaciones/ope_Usuario.html',cont,contexto)


@login_required
def newGrado(request):
    grado  = CeGrado.objects.order_by('grad_nombre')
    mi_contexto = Context({'posts':grado,'Permisos':permisos(request)})
    if request.POST:
        form = GradoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/newGrado/')
    else:
        form = GradoForm()
    args = {}
    args.update(csrf(request))

    args['form'] = form
 
    return render_to_response('Mantenimientos/mant_Grado.html', args,mi_contexto)
@login_required
#def newSeccion(request):
#   seccion  = CeSeccion.objects.order_by('secc_nombre')
#  mi_contexto = Context({'posts':seccion})
# if request.POST:
#    #form = SeccionForm(request.POST)
#   if form.is_valid():
#      form.save()
#     return HttpResponseRedirect('/newSeccion/')
#   else:
#   form = SeccionForm()
#   args = {}
#   args.update(csrf(request))

#   args['form'] = form
 
#return render_to_response('Mantenimientos/mant_Seccion.html', args,mi_contexto)

#Paquete Operaciones
@login_required
def newAlumno(request):
    alumno  = CeAlumno.objects.order_by('cepk_per')
    mi_contexto = Context({'posts':alumno,'Permisos':permisos(request)})
    if request.POST:
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/newAlumno/')
    else:
        form = AlumnoForm()
    args = {}
    args.update(csrf(request))

    args['form'] = form
 
    return render_to_response('Operaciones/ope_Alumno.html', args,mi_contexto)

@login_required
def inicio(request):    
    return render_to_response('login.html')

@login_required(login_url='/login/')
def index(request):   
    
    print("permisos:"+".."+str(permisos(request)))
    mi_contexto2 = Context({'Permisos':permisos(request)})
    return render_to_response('index.html',mi_contexto2)

@login_required
def newCurso(request):

    curso  = CeCurso.objects.order_by('cur_nombre')
    mi_contexto = Context({'posts':curso,'Permisos':permisos(request)})
    if request.POST:
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/newCurso/')
    else:
        form = CursoForm()
    args = {}
    args.update(csrf(request))

    args['form'] = form
 
    return render_to_response('Operaciones/ope_Curso.html', args,mi_contexto)



#Actualizar models
@login_required
def ActualizarDistrito(request, distrito_id): 
    distrito  = Distrito.objects.order_by('distr_nombre')
    mi_contexto = Context({'posts':distrito})
    instance = get_object_or_404(Distrito, cepk_distrito = distrito_id)
    form = DistritoForm(request.POST or None, instance=instance)
    args = {}
    args.update(csrf(request))

###########################################
@login_required
@permission_required('SistemaWeb.asignar_profesorCurso')
def ElegirProfesor(request):
    profesor = CeProfesor.objects.order_by('porf_gacademico')
    mi_contexto = Context({'profesores':profesor,'Permisos':permisos(request)})
    listaGrad = CeCatalogo.objects.filter(cat_general = Parametros.PROFESOR_GRADO_ACADEMICO)
    mi_lista = Context({'gradosAcad':listaGrad})
    return render_to_response('Operaciones/ope_SeleccionarProfesor.html',mi_contexto,mi_lista)

@login_required
@permission_required('SistemaWeb.asignar_profesorCurso')
def ElegirCurso(request,profesor_id):
    caso = get_object_or_404(CeProfesor,cepk_prof=profesor_id)
    global id_profesor 
    id_profesor = profesor_id
    cursos = CeDetGradsecCurso.objects.filter(det_asig = Parametros.CURGRADSEC_NO_ASIGNADO)
    for curso in cursos:
        asig =  CeCatalogo.objects.filter(cat_general = Parametros.CURGRADSEC_TIPO_ASIGNADO ,cat_secundario = curso.det_asig)
        curso.det_asig = asig.get().cat_descripcion
        
    mi_contexto = Context({'cursos':cursos,'Permisos':permisos(request)})
    
    return render_to_response('Operaciones/ope_SeleccionarCurso.html',{'profesor':caso},mi_contexto)

@login_required
@permission_required('SistemaWeb.asignar_profesorCurso')
def AsignarCursoProfesor(request,curso_id):
    caso = get_object_or_404(CeDetGradsecCurso,cepk_detgrcur=curso_id)
    global curso
    curso = caso
    global id_profesor 
    profesor = get_object_or_404(CeProfesor,cepk_prof = id_profesor)
    global prof
    prof = profesor
    mi_contexto = Context({'profesor':profesor,'Permisos':permisos(request)})
    return render_to_response('Operaciones/ope_AsignarCursoProfesor.html',{'curso':caso},mi_contexto)

@login_required
@permission_required('SistemaWeb.asignar_profesorCurso')
def Asignar(request):
    global prof
    global curso
    CeDetGradsecCurso.objects.filter(cepk_detgrcur = curso.cepk_detgrcur).update(det_asig=Parametros.CURGRADSEC_ASIGNADO)
    cursoProf = CeDetProfcurso(cepk_prof=prof,cepk_detgrcur=curso,cur_horas='3')  
    cursoProf.save()
    #return render_to_response('Operaciones/Correcto.html',{'Permisos':permisos(request)});
    return HttpResponseRedirect('/elegirProfesor/') 

#################
@login_required
@permission_required('SistemaWeb.asignar_seccGrad')
def ElegirSeccion_DetGradSecc(request):
    caso = CeSeccion.objects.order_by('secc_nombre')
    #Aqui traemos la decripcion del catalogo      
    for seccion in caso:
        catalogoTipo = CeCatalogo.objects.filter(cat_general = Parametros.SECCION_TIPO_SECCION ,cat_secundario = seccion.secc_tipo)
        tipo = catalogoTipo.get()
        seccion.secc_tipo = tipo.cat_descripcion
    contexto = Context({'secciones':caso,'Permisos':permisos(request)})
    return render_to_response('Operaciones/ope_Select_SeccionDetSeccGrado.html',contexto)

@login_required
@permission_required('SistemaWeb.asignar_seccGrad')
def ElegirGrado_DetGradSecc(request,seccion_id):
    caso = get_object_or_404(CeSeccion,cepk_secc=seccion_id)
  
    catalogoTipo = CeCatalogo.objects.filter(cat_general = Parametros.SECCION_TIPO_SECCION ,cat_secundario = caso.secc_tipo)
    tipo = catalogoTipo.get()
    caso.secc_tipo = tipo.cat_descripcion
    
    global id_seccion 
    id_seccion = seccion_id
    grados = CeGrado.objects.all()
    mi_contexto = Context({'grados':grados,'Permisos':permisos(request)})
    
    return render_to_response('Operaciones/ope_Select_GradoDetSeccGrado.html',{'seccion':caso},mi_contexto)

@login_required
@permission_required('SistemaWeb.asignar_seccGrad')
def AsignarSeccion_DetGradSecc(request,grado_id):
    caso = get_object_or_404(CeGrado,cepk_grad=grado_id)
    
    global grado_DSG
    grado_DSG = caso
    
    global id_seccion
    seccion = get_object_or_404(CeSeccion,cepk_secc = id_seccion)
    global seccion_DSG
    seccion_DSG = seccion
    catalogoTipo = CeCatalogo.objects.filter(cat_general = Parametros.SECCION_TIPO_SECCION ,cat_secundario = seccion.secc_tipo)
    tipo = catalogoTipo.get()
    seccion.secc_tipo = tipo.cat_descripcion
    
   
    mi_contexto = Context({'seccion':seccion,'Permisos':permisos(request)})
    
    return render_to_response('Operaciones/ope_AsignarSeccionGrado.html',{'grado':caso},mi_contexto)

@login_required
@permission_required('SistemaWeb.asignar_seccGrad')
def Asignar_DetGradSecc(request):
    
    seccionGrado = CeDetGradsecc(cepk_secc=seccion_DSG,cepk_grad=grado_DSG)  
    seccionGrado.save()
    return render_to_response('Operaciones/Correcto_DSG.html',{'Permisos':permisos(request)});

#######################################
@login_required
@permission_required('SistemaWeb.asignar_cursoSeccGrad')
def Elegir_Curso_DCSG(request):
    listaCursos = CeCurso.objects.filter(cur_testado = Parametros.CURSO_EST_ACTIVO)
    
    for curso in listaCursos:
        catalogoTipo = CeCatalogo.objects.filter(cat_general = Parametros.CURSO_TIPO_CURSO ,cat_secundario = curso.cur_tipo)
        tipo = catalogoTipo.get()
        curso.cur_tipo = tipo.cat_descripcion
        
        catalogoEsta = CeCatalogo.objects.filter(cat_general = Parametros.CURSO_ESTADO_CURSO ,cat_secundario = curso.cur_testado)
        esta = catalogoEsta.get()
        curso.cur_testado = esta.cat_descripcion
        
    mis_cursos = Context({'listaCursos':listaCursos,'Permisos':permisos(request)})
    return render_to_response('Operaciones/Curso_DSG/ope_Select_Curso_DCSG.html',mis_cursos);

@login_required
@permission_required('SistemaWeb.asignar_cursoSeccGrad')
def Elegir_GradSecc_DCSG(request,curso_id):
    
    cursoSelect = get_object_or_404(CeCurso,cepk_cur = curso_id)
    listaSeccGrad = CeDetGradsecc.objects.all()
    
    catalogoTipo = CeCatalogo.objects.filter(cat_general = Parametros.CURSO_TIPO_CURSO ,cat_secundario = cursoSelect.cur_tipo)
    tipo = catalogoTipo.get()
    cursoSelect.cur_tipo = tipo.cat_descripcion
        
    catalogoEsta = CeCatalogo.objects.filter(cat_general = Parametros.CURSO_ESTADO_CURSO ,cat_secundario = cursoSelect.cur_testado)
    esta = catalogoEsta.get()
    cursoSelect.cur_testado = esta.cat_descripcion    
    
    curso_select = Context({'curso':cursoSelect})
    mis_seccGrad = Context({'listaSeccGrad':listaSeccGrad,'Permisos':permisos(request)})
    
    return render_to_response('Operaciones/Curso_DSG/ope_Select_SeccGrad_DCSG.html',mis_seccGrad,curso_select);

@login_required
@permission_required('SistemaWeb.asignar_cursoSeccGrad')
def Asignar_CursoSeccGrad_DCSG(request,curso_id,seccGrad_id):
    
    curso = get_object_or_404(CeCurso,cepk_cur = curso_id)
    seccGrad = get_object_or_404(CeDetGradsecc,cepk_gradsec = seccGrad_id)
    
    catalogoEst = CeCatalogo.objects.filter(cat_general = Parametros.CURSO_ESTADO_CURSO ,cat_secundario = curso.cur_testado)
    estado = catalogoEst.get()
    curso.cur_testado = estado.cat_descripcion
    
    catalogoTipo = CeCatalogo.objects.filter(cat_general = Parametros.SECCION_TIPO_SECCION ,cat_secundario = seccGrad.cepk_secc.secc_tipo)
    estado = catalogoTipo.get()
    seccGrad.cepk_secc.secc_tipo = estado.cat_descripcion
    
    contexto= Context({'seccGrad':seccGrad,'curso':curso,'Permisos':permisos(request)})
    if request.POST:
        form = CursoSeccGradForm(request.POST)
        if form.is_valid():
            CSG = form.save(commit = False)
            CSG.cepk_gradsec =seccGrad
            CSG.cepk_cur=curso
            CSG.save()
            return HttpResponseRedirect('/OPE/Asignar_DCSG/')
    else:
        form = CursoSeccGradForm()
    args = {}
    args.update(csrf(request))

    args['form'] = form
    
    return render_to_response('Operaciones/Curso_DSG/ope_Asignar_CurSeccGrad_DCSG.html',args,contexto)

@login_required
def ElegirTutor(request):
    tutor = CeTutor.objects.all()
    mi_contexto = Context({'tutores':tutor,'Permisos':permisos(request)})
    
    return render_to_response('Operaciones/ope_SeleccionarTutor.html',mi_contexto)

@login_required
@permission_required('SistemaWeb.asignar_cursoSeccGrad')
def Asignar_DCSG(request):
    
    return render_to_response('Operaciones/Curso_DSG/Correcto.html',{'Permisos':permisos(request)});
@login_required
def ElegirGradSecc(request,tutor_id):
    
    caso = get_object_or_404(CeTutor,cepk_tut=tutor_id)
    global id_tutor
    id_tutor = tutor_id
    gradsecc = CeDetGradsecc.objects.all()
    mi_contexto = Context({'gradsecc':gradsecc,'Permisos':permisos(request)})
    
    return render_to_response('Operaciones/ope_SeleccionarGradSeccTut.html',{'tutor':caso},mi_contexto)

@login_required
def AsignarGradSecTutor(request,gradsecc_id):
    caso = get_object_or_404(CeDetGradsecc,cepk_gradsec=gradsecc_id)
    global grad_seccion_t
    grad_seccion_t = caso
    global id_tutor
    tut = get_object_or_404(CeTutor,cepk_tut = id_tutor)
    global tutor  
    tutor = tut
    mi_contexto = Context({'tutor':tutor,'Permisos':permisos(request)})
    
    return render_to_response('Operaciones/ope_AsignarSeccionGradoTutor.html',{'gradsec':caso},mi_contexto)   

@login_required
def Asignar_GradSecTut(request):
    global tutor
    global grad_seccion_t
    gradSecTutor = CeDetGradsecTut(cepk_gradsec = grad_seccion_t, cepk_tut = tutor)
    gradSecTutor.save()
    
    return HttpResponseRedirect('/elegirTutor/') 
