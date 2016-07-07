'''
Created on 18 de may. de 2016

@author: Rottweilas
'''
from django import forms
from django.forms.widgets import Widget

from SistemaWeb.models import CeGrado, CeSeccion, CeAula, CeAsistencia, CeCurso, CeDetProfcurso, \
    CeProfesor, CePerfil, CeUsuario, CeMatricula, CeTutor, CeCatalogo,\
    CeDetGradsecCurso

from .models import Distrito, Persona, CeAlumno
from django.shortcuts import get_object_or_404
from SistemaWeb.util import Parametros
from logging import PlaceHolder


class PostForm(forms.ModelForm):
    class Meta:
        model = Distrito
        fields = ('distr_departamento','distr_provincia','distr_nombre')
        
class DistritoForm(forms.ModelForm):
    class Meta:
        model = Distrito
        fields = ('distr_departamento','distr_provincia', 'distr_nombre')
        widgets = {
            'distr_departamento': forms.TextInput(attrs={'class': 'form-control'}),
            'distr_provincia': forms.TextInput(attrs={'class': 'form-control'}),
            'distr_nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }
class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ('cepk_per','per_nombres','per_apellpat','per_apellmat','per_dni','per_telf','per_nomcalle','cepk_distrito','per_email','per_fechnac')
        widgets = {
            'cepk_per': forms.TextInput(attrs={'class': 'form-control'}),      
            'per_nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'per_apellpat': forms.TextInput(attrs={'class': 'form-control'}),
            'per_apellmat': forms.TextInput(attrs={'class': 'form-control'}),
            'per_dni': forms.NumberInput(attrs={'class': 'form-control'}),
            'per_telf': forms.TextInput(attrs={'class': 'form-control'}),
            'cepk_distrito': forms.Select(attrs={'class': 'form-control'}),
            'per_nomcalle': forms.TextInput(attrs={'class': 'form-control'}),
            'per_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'distr_provincia': forms.TextInput(attrs={'class': 'form-control'}),
            'per_fechnac': forms.DateInput(attrs={'type':'date'}),
        }
        
class ProfesorForm(forms.ModelForm):
    class Meta:
        model = CeProfesor
        
        listaTProf = CeCatalogo.objects.filter(cat_general = Parametros.PROFESOR_TIPO_PROFESOR)
        listaGAcad = CeCatalogo.objects.filter(cat_general = Parametros.PROFESOR_GRADO_ACADEMICO)
        listaEstad = CeCatalogo.objects.filter(cat_general = Parametros.PROFESOR_ESTADO_PROFESOR)
        
        opcTProf = [(x.cat_secundario,x.cat_descripcion) for x in listaTProf]
        opcGAcad = [(x.cat_secundario,x.cat_descripcion) for x in listaGAcad]
        opcEstad = [(x.cat_secundario,x.cat_descripcion) for x in listaEstad]
        
        widgets = {
            'prof_especialidad': forms.TextInput(attrs={'class': 'form-control'}),
            'prof_tipo': forms.Select(choices = opcTProf,attrs={'class': 'form-control'}),
            'porf_gacademico': forms.Select(choices = opcGAcad,attrs={'class': 'form-control'}),
            'prof_estado': forms.Select(choices = opcEstad,attrs={'class': 'form-control'}),
        }
        fields = ('prof_especialidad','prof_tipo','porf_gacademico','prof_estado')
       


        
class TutorForm(forms.ModelForm):
    class Meta:
        model = CeTutor
        
        fields = ('tut_especialidad',)
        widgets = {
               'tut_especialidad':  forms.TextInput(attrs={'class': 'form-control'}), 
        }

class EstadoProfesorForm(forms.ModelForm):
    class Meta:
        model = CeProfesor
        
        listaEstad = CeCatalogo.objects.filter(cat_general = Parametros.PROFESOR_ESTADO_PROFESOR)
        opcEstad = [(x.cat_secundario,x.cat_descripcion) for x in listaEstad]
        
        fields = ('prof_estado',)
        widgets = {
            'prof_estado': forms.Select(choices = opcEstad,attrs={'class': 'form-control'}),
        }

class EstadoTutorform(forms.ModelForm):
    class Meta:
        model = CeTutor
        
        listaEstad = CeCatalogo.objects.filter(cat_general = Parametros.TUTOR_ESTADO_TUTOR)
        opcEstad = [(x.cat_secundario,x.cat_descripcion) for x in listaEstad]
        
        fields = ('tut_estado',) 
        
        widgets = {
            'tut_estado': forms.Select(choices = opcEstad,attrs={'class': 'form-control'}),
        }
               
class AlumnoForm(forms.ModelForm):
    class Meta:
        model = CeAlumno
        fields = ('alu_nhnos',)
        widgets = {
            'alu_nhnos': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class AulaForm(forms.ModelForm):
    class Meta:
        model = CeAula
        fields = ('cepk_secc','cepk_grad','aul_pabellon', 'aul_estado','aul_capacidad','aul_npiso','aul_nombre')
        widgets = {
            'cepk_secc': forms.Select(attrs={'class': 'form-control'}),
            'cepk_grad': forms.Select(attrs={'class': 'form-control'}),
            'aul_capacidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'aul_pabellon': forms.TextInput(attrs={'class': 'form-control'}),
            'aul_estado': forms.TextInput(attrs={'class': 'form-control'}),
            'aul_npiso': forms.NumberInput(attrs={'class': 'form-control'}),
            'aul_nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
 
class GradoForm(forms.ModelForm):
    class Meta:
        model = CeGrado
        fields = ('cepk_grad','grad_nivel','grad_nombre')
        widgets = {
            'grad_nivel': forms.TextInput(attrs={'class': 'form-control'}),
            'grad_nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PerfilForm(forms.ModelForm):
    class Meta:
        model = CePerfil
        fields = ('cepk_perf','perf_tperfil','perf_descripcion','perf_activo')
        widgets = {
           'perf_tperfil' : forms.TextInput(attrs={'class': 'form-control'}),     
           'perf_descripcion': forms.TextInput(attrs={'class': 'form-control'}),
           'perf_activo': forms.TextInput(attrs={'class': 'form-control'}),
        }
        

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = CeUsuario
        fields = ('cepk_usua','cepk_per','cepk_perf','usua_testado','usua_user','usua_password') 
        
        widgets = {
              'cepk_per': forms.Select(attrs={'class': 'form-control'}),
              'cepk_perf': forms.Select(attrs={'class': 'form-control'}),
              'usua_testado': forms.TextInput(attrs={'class': 'form-control'}),
              'usua_user': forms.TextInput(attrs={'class': 'form-control'}),
              'usua_password': forms.TextInput(attrs={'class': 'form-control'}),

              }
               
class SeccionForm(forms.ModelForm):
    
    class Meta:
        model = CeSeccion
        #Traigo los tipo de Seccion
        listaTSecc = CeCatalogo.objects.filter(cat_general = Parametros.SECCION_TIPO_SECCION)
        opcTSecc = [(x.cat_secundario,x.cat_descripcion) for x in listaTSecc]
        
        fields = ('cepk_secc','secc_nombre','secc_tipo')
        widgets = {
            'secc_nombre': forms.TextInput(attrs={'class': 'form-control'}),
            #El x.cat_secundario es el que se manda al form
            'secc_tipo' : forms.Select(choices= opcTSecc ,attrs={'class': 'form-control'}),
        }
        
class CursoForm(forms.ModelForm):
    class Meta:
        model = CeCurso
        
        listaTCur = CeCatalogo.objects.filter(cat_general = Parametros.CURSO_TIPO_CURSO)
        listaECur = CeCatalogo.objects.filter(cat_general = Parametros.CURSO_ESTADO_CURSO)    
        
        opcTCur = [(x.cat_secundario,x.cat_descripcion) for x in listaTCur]
        opcECur = [(x.cat_secundario,x.cat_descripcion) for x in listaECur]
        
        fields = ('cur_nombre','cur_tipo','cur_testado')
        widgets = {
            'cur_nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'cur_tipo': forms.Select(choices=opcTCur,attrs={'class': 'form-control'}),
            'cur_testado': forms.Select(choices=opcECur,attrs={'class': 'form-control'}),
        }
                
class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = CeAsistencia
        fields = ('cepk_grad','cepk_secc','asis_tutor','asis_valor','cepk_alu')
        widgets = {
            'cepk_grad': forms.Select(attrs={'class': 'form-control'}),
            'cepk_secc': forms.Select(attrs={'class': 'form-control'}),
            'asis_tutor': forms.TextInput(attrs={'class': 'form-control'}),
            'asis_valor': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'cepk_alu': forms.Select(attrs={'class': 'form-control'}),
        }
class CursoProfesorForm(forms.ModelForm): 
    class Meta:
        model = CeDetProfcurso
        fields = ('cepk_prof','cepk_detgrcur','cur_horas','ecpk_detprocur')
        

class MatriculaForm(forms.ModelForm):
    class Meta:
        model = CeMatricula
        
        listaEstad = CeCatalogo.objects.filter(cat_general = Parametros.MATRICULA_ESTADO_MATRICULA)
        opcEstad = [(x.cat_secundario,x.cat_descripcion) for x in listaEstad]
        opcEstad.sort()
        fields =('matr_fecha','matr_estado','matr_observacion','cepk_gradsec','matr_observacion','matr_edadalumno')
        widgets = {
            'matr_fecha': forms.DateInput(attrs={'type':'date'}),
            'matr_estado': forms.Select(choices = opcEstad, attrs={'class': 'form-control'}),
            'matr_observacion': forms.TextInput(attrs={'class': 'form-control'}),
            'cepk_gradsec': forms.Select(attrs={'class': 'form-control'}),
            'matr_observacion': forms.TextInput(attrs={'class': 'form-control'}),
            'matr_edadalumno': forms.TextInput(attrs={'class': 'form-control'}),
        }
class MantMatriculaForm(forms.ModelForm):
    class Meta:
        model = CeMatricula
        
        listaEstad = CeCatalogo.objects.filter(cat_general = Parametros.MATRICULA_ESTADO_MATRICULA)
        opcEstad = [(x.cat_secundario,x.cat_descripcion) for x in listaEstad]
        opcEstad.sort()
        fields =('matr_fecha','matr_observacion','cepk_gradsec','matr_observacion','matr_edadalumno',)
        widgets = {
            'matr_fecha': forms.DateInput(attrs={'type':'date'}),
            'matr_observacion': forms.TextInput(attrs={'class': 'form-control'}),
            'cepk_gradsec': forms.Select(attrs={'class': 'form-control'}),
            'matr_observacion': forms.TextInput(attrs={'class': 'form-control'}),
            'matr_edadalumno': forms.TextInput(attrs={'class': 'form-control'}),
        }
class CursoSeccGradForm(forms.ModelForm):
    class Meta:
        model = CeDetGradsecCurso
        
        fields =('det_gsc_horas',)
        widgets = {
            'det_gsc_horas': forms.NumberInput(attrs={'class': 'form-control'}),
        }                         