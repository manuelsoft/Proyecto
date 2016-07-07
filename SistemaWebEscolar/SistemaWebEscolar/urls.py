"""SistemaWebEscolar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView

from SistemaWeb.views import index, articles, prueba, prueba2, prueba3, prueba4, prueba5, NuevoDistrito, post_detail, newDistrito, newPersona, inicio, newAlumno, \
    newGrado, newAula, newCurso, prueba6, ElegirProfesor, ElegirCurso, AsignarCursoProfesor, Asignar, \
    newProfesor, newPerfil, newUsuario, user_login, \
    user_logout, ElegirSeccion_DetGradSecc, ElegirSeccion_DetGradSecc, \
    ElegirGrado_DetGradSecc, ElegirGrado_DetGradSecc, Asignar_DetGradSecc, \
    ElegirTutor, ElegirGradSecc, \
    AsignarGradSecTutor, Asignar_GradSecTut, Elegir_Curso_DCSG, \
    Elegir_GradSecc_DCSG, AsignarSeccion_DetGradSecc, Asignar_CursoSeccGrad_DCSG, \
    Asignar_DCSG
from SistemaWeb.viewsActu import ActualizarDistrito, ActualizarProfesor, ActulizarDatosProfesor, ActualizarSeccion, \
    ActualizarCurso, ActualizarTutor, ActulizarDatosTutor
from SistemaWeb.viewsCns import cnsProfesor, cnsUsuario, cnsAlumno, cns_Profesor, \
    cnsTutor, cns_Tutor, cnsProfesorCurso, cns_Det_ProfesorCurso, \
    cnsTutorGradSec, cns_Det_TutorCurso, cnsCursoGradoSecc, cnsDetCursoGradoSecc,\
    cns_Alumno
from SistemaWeb.viewsMant import mantAula, mantPersona, mantAlumno, mantCurso, mantDistrito, mantGrado, mantSeccion, mantProfesor, \
    mantTutor
from SistemaWeb.viewsMatricula import GenerarMatricula, IniciarMatricula, IniciarAnularMatricula, AnularMatricula, Anulalo_Matricula, \
    IniciarMantenerMatricula, MantenerMatricula
from SistemaWeb.viewsOpe import OpeProfesor, EstadoProfesor, OpeTutor, \
    EstadoTutor, DesasignarGradSecTutor, ListaProfesoresDes, DesasignarGST, \
    ListaTutoresDes, DesasignarCursoProfesor, DesasignarCProf
from SistemaWeb.viewsReg import regProfesor, registrarPersonaProfesor, regAlumno, \
    registrarPersonaAlumno, regCurso, regSeccion, registrarPersonaTutor, regTutor


urlpatterns = [
               
    url(r'^admin/',include(admin.site.urls)),
   # url(r'^inicio/$',index,name='inicio'),
    url(r'^articulos/$',articles),
    url(r'^prueba/$',prueba),
    url(r'^prueba/(?P<distrito_id>\d+)/$',prueba2),
    url(r'^validar/(?P<distrito_id>\d+)/$',prueba3),
    url(r'^vertemplate/$',prueba4),
    url(r'^vertemplate/(?P<distrito_id>\d+)/$',prueba5,name='ver_distrito'),
    
    url(r'^escogerCurso/(?P<curso_id>\d+)/$',prueba6,name='ver_curso'),
    
    url(r'^distrito/$', NuevoDistrito, name='distrito'),
    url(r'^distrito/(?P<pk>[0-9]+)/$', post_detail),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', NuevoDistrito, name='post_edit'),
    url(r'^newDistrito/', newDistrito, name='crearDistrito'),
    url(r'^newPersona/', newPersona, name='crearPersona'),
    url(r'^newAlumno/', newAlumno, name='crearAlumno'),
    
    #Mantenimientos
    url(r'^newGrado/', newGrado, name='crearGrado'),
    #url(r'^newSeccion/', newSeccion, name='crearSeccion'),
    url(r'^newAula/', newAula, name='crearAula'),
    
    url(r'^newCurso/', newCurso, name='crearCurso'),
    
    url(r'^inicio/$',index,name='inicio'),
    
     #Profesor
    url(r'^newProfesor/', newProfesor, name='crearProfesor'),
   
    
    #Operaciones
    url(r'^elegirProfesor/$',ElegirProfesor),
    url(r'^elegirTutor/$',ElegirTutor), 
    url(r'^elegirCurso/(?P<profesor_id>\d+)/$',ElegirCurso,name='ver_profesor'),
    url(r'^elegirGradSecc/(?P<tutor_id>\d+)/$',ElegirGradSecc,name='ver_tutor'),
    url(r'^selecCursoProfesor/(?P<curso_id>\d+)/$',AsignarCursoProfesor,name='ver_curso2'),
    url(r'^selecGradSecTutor/(?P<gradsecc_id>\d+)/$',AsignarGradSecTutor,name='ver_gradsecc'),
    url(r'^Asignar/$', Asignar, name='Asignar'),
    url(r'^AsignarTutor/$', Asignar_GradSecTut),
    
    url(r'^ListaTutorDesGS/$', ListaTutoresDes),    
    url(r'^SelecDesGST/(?P<tutor_id>\d+)/$',DesasignarGradSecTutor,name='DesGradSecTutor'),
    url(r'^DesasignarGST/(?P<gradSecTut_id>\d+)/$',DesasignarGST),
    url(r'^ListaProfesorDesCur/$', ListaProfesoresDes),    
    url(r'^SelecDesCurso/(?P<profesor_id>\d+)/$',DesasignarCursoProfesor,name='DesCrusoProf'),
    url(r'^DesasignarCProf/(?P<gradCurProf_id>\d+)/$',DesasignarCProf, name='DesigPC'),    
    
    
    url(r'^elegirSeccion_DSG/$',ElegirSeccion_DetGradSecc),
    url(r'^elegirGrado_DSG/(?P<seccion_id>\d+)/$',ElegirGrado_DetGradSecc,name='ver_seccion'),
    url(r'^selecSeccionGrado/(?P<grado_id>\d+)/$',AsignarSeccion_DetGradSecc,name='ver_grado'),
    url(r'^Asignar_DSG/$', Asignar_DetGradSecc),
    
    url(r'^OPE/Curso_DCSG/$', Elegir_Curso_DCSG),
    url(r'^OPE/SeccGrado_DCSG/(?P<curso_id>\d+)/$',Elegir_GradSecc_DCSG,name='curso_DCSG'),
    url(r'^OPE/CursoSeccGrado_DCSG/(?P<curso_id>\d+)/(?P<seccGrad_id>\d+)/$',Asignar_CursoSeccGrad_DCSG,name='seccGrad_DCSG'),
    url(r'^OPE/Asignar_DCSG/$',Asignar_DCSG),
    
    #Usuario y PErfiles
    url(r'^newPerfil/$',newPerfil),
    url(r'^newUsuario/$',newUsuario),

    
    #Actualizaciones
    url(r'^ActualizarDistrito/(?P<distrito_id>\d+)/$',ActualizarDistrito,name='distrito'),
    
    url(r'^ActualizarProfesor/$',ActualizarProfesor), 
    
    url(r'^ActualizarProfesor/(?P<profesor_id>\d+)/$',ActulizarDatosProfesor,name='profesor'),    

    url(r'^ActualizarCurso/(?P<curso_id>\d+)/$',ActualizarCurso,name='curso'),
    url(r'^ActualizarSeccion/(?P<seccion_id>\d+)/$',ActualizarSeccion,name='seccion'),
  
    url(r'^ActualizarTutor/(?P<tutor_id>\d+)/$',ActulizarDatosTutor, name='tutor'),    
    url(r'^ActualizarTutor/$',ActualizarTutor), 
    
       
    #Consultas
    url(r'^CNS/cns_ProfesorCurso/$', cnsProfesorCurso),
    url(r'^CNS/cns_TutorGradSec/$', cnsTutorGradSec),
    url(r'^CNS/cns_DatosProfesorCurso/(?P<profesor_id>\d+)/$', cns_Det_ProfesorCurso, name='profesorCurso'),
    url(r'^CNS/cns_DatosTutorGradSec/(?P<tutor_id>\d+)/$', cns_Det_TutorCurso, name='tutorGradSec'),    
    url(r'^CNS/Profesor/$', cnsProfesor, name='cnsProfesorCurso'),
    url(r'^CNS/Tutor/$',cnsTutor),
    url(r'^CNS/ConsultarProf/(?P<profesor_id>\d+)/$', cns_Profesor, name='cns_profesor'),
    url(r'^CNS/ConsultarTutor/(?P<tutor_id>\d+)/$', cns_Tutor, name='cns_tutor'),
    
    url(r'^CNS/Usuario/$', cnsUsuario, name='cnsUsuario'),
    url(r'^CNS/Alumno/$', cnsAlumno),  
    url(r'^CNS/Alumno/(?P<alumno_id>\d+)/$', cns_Alumno, name='cnsAlumno'),  
  
    url(r'^CNS/Cuso_GradoSeccion/$',cnsCursoGradoSecc),
    url(r'^CNS/Cuso_GradoSeccion/(?P<det_id>\d+)/$', cnsDetCursoGradoSecc, name='cns_CursoGradSecc'),
    
    #LOGIN
    url(r'^login/', user_login), 
    url(r'^logout/', user_logout), 
    
    #Mantenimientos
    url(r'MAN/Alumno/$', mantAlumno),
    url(r'^MAN/Profesor/$', mantProfesor),
    url(r'^MAN/Tutor/$', mantTutor),
    url(r'^MAN/Curso/$', mantCurso),
    url(r'^MAN/Grado/$', mantGrado),
    url(r'^MAN/Seccion/$', mantSeccion),
    url(r'^MAN/Aula/$', mantAula),
    url(r'^MAN/Distrito/$', mantDistrito),
    
    #Registros

    url(r'^REG/DatosPersProfesor/$', registrarPersonaProfesor),
    url(r'^REG/DatosPersAlumno/$', registrarPersonaAlumno),
    url(r'^REG/DatosPersTutor/$',registrarPersonaTutor),
    
    url(r'^REG/Alumno/$', regAlumno),
    url(r'^REG/Profesor/$', regProfesor),
    url(r'^REG/Tutor/$', regTutor),
    url(r'^REG/Curso/$', regCurso),
    url(r'^REG/Grado/$', regProfesor),
    url(r'^REG/Seccion/$', regSeccion),
    url(r'^REG/Aula/$', regProfesor),
    url(r'^REG/Distrito/$', regProfesor),
    
    url(r'^REG/Usuario/$',newUsuario),

    #Matricula
    url(r'^IniciarMatricula/$',IniciarMatricula),
    url(r'^GenerarMatricula/(?P<alumno_id>\d+)/$',GenerarMatricula,name='matricula'),
    
    url(r'^AnularMatricula/$',IniciarAnularMatricula),
    url(r'^GenerarMatricula/(?P<alumno_id>\d+)/(?P<matricula_id>\d+)/$',AnularMatricula,name='anular_matricula'),
    url(r'^Anulalo/(?P<alumno_id>\d+)/(?P<matricula_id>\d+)/$',Anulalo_Matricula),
    
    url(r'^MantenerMatricula/$',IniciarMantenerMatricula),    
    url(r'^MantenerMatricula/(?P<matricula_id>\d+)/$',MantenerMatricula,name='mant_matricula'),
     
    url(r'^OPE/Profesor/$',OpeProfesor),
    url(r'^OPE/EstadoProfesor(?P<profesor_id>\d+)/$',EstadoProfesor,name='opeProfesor'),
    
    url(r'^OPE/Tutor/$',OpeTutor),
    url(r'^OPE/EstadoTutor(?P<tutor_id>\d+)/$',EstadoTutor,name="opeTutor"),
    
]
