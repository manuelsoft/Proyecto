# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from pickle import FALSE


class Distrito(models.Model):
    # cepk_distrito = models.DecimalField(primary_key=True, max_digits=8, decimal_places=0)
    cepk_distrito = models.AutoField(primary_key=True)
    distr_departamento = models.CharField(_('Departamento'),
        max_length=20 
    )
    distr_provincia = models.CharField(_('Provincia'),max_length=20)
    distr_nombre = models.CharField(_('Distrito'),max_length=20)

    def __str__(self):
        return self.distr_nombre
    class Meta:
        managed = False
        db_table = 'ce_distrito'


class Persona(models.Model):
    # cepk_per = models.DecimalField(primary_key=True, max_digits=8, decimal_places=0)
        
    cepk_per = models.AutoField(primary_key=True)
    per_nombres = models.CharField(_('Nombres'),max_length=40)
    per_apellpat = models.CharField(_('Apellido Paterno'),max_length=20)
    per_apellmat = models.CharField(_('Apellido Materno'),max_length=20)
    per_dni = models.DecimalField(_('DNI'),max_digits=8, decimal_places=0)
    per_telf = models.DecimalField(_('Telefono'),max_digits=9, decimal_places=0)
    per_nomcalle = models.CharField(_('Direccion'),max_length=40, blank=True, null=True)
    cepk_distrito = models.ForeignKey(Distrito, models.DO_NOTHING, db_column='cepk_distrito')
    per_email = models.CharField(_('E-mail'),max_length=50, blank=True, null=True)
    per_fechnac = models.DateField(_('Fecha Nacimiento'))
    
    def __str__(self):
        return self.per_nombres+" "+self.per_apellpat+ " "+ self.per_apellmat
        
    class Meta:
        managed = False
        db_table = 'ce_persona'
        


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    
    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)




class CeCalificacion(models.Model):
    cepk_calf = models.DecimalField(primary_key=True, max_digits=8, decimal_places=0)
    calf_notapract = models.DecimalField(max_digits=2, decimal_places=2, blank=True, null=True)
    calf_notaexam = models.DecimalField(max_digits=2, decimal_places=2, blank=True, null=True)
    calf_notaconducta = models.DecimalField(max_digits=2, decimal_places=2, blank=True, null=True)
    calf_notaoral = models.DecimalField(max_digits=2, decimal_places=2, blank=True, null=True)
    calf_promcurso = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    calf_fechareg = models.DateField(blank=True, null=True)
    calf_bimestre = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ce_calificacion'


class CeCurso(models.Model):
    # cepk_cur = models.DecimalField(primary_key=True, max_digits=8, decimal_places=0)
    cepk_cur = models.AutoField(primary_key=True)
    cur_nombre = models.CharField(_('Curso'),max_length=25, blank=True, null=True)
    cur_tipo = models.CharField(_('Tipo'),max_length=5, blank=True, null=True)
    cur_testado = models.CharField(_('Estado'),max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ce_curso'
        

class CeAlumno(models.Model):
    cepk_per = models.ForeignKey(Persona, models.DO_NOTHING, db_column='cepk_per')
    cepk_alu = models.AutoField(primary_key=True)
    alu_nhnos = models.DecimalField(_('Numero hermanos'),max_digits=2, decimal_places=0, blank=True, null=True)
    alu_altura = models.DecimalField(_('Alturo'),max_digits=2, decimal_places=2, blank=True, null=True)
    alu_estado = models.DecimalField(_('Estado'),max_digits=1, decimal_places=0)
    
    class Meta:
        managed = False
        db_table = 'ce_alumno'


class CeDetAlucurso(models.Model):
    cepk_cur = models.ForeignKey(CeCurso, models.DO_NOTHING, db_column='cepk_cur')
    cepk_alu = models.ForeignKey(CeAlumno, models.DO_NOTHING, db_column='cepk_alu')
    cepk_calf = models.ForeignKey(CeCalificacion, models.DO_NOTHING, db_column='cepk_calf', blank=True, null=True)
    cepk_alucurso = models.DecimalField(max_digits=8, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'ce_det_alucurso'
        unique_together = (('cepk_cur', 'cepk_alu', 'cepk_alucurso'),)


class CeDetGradsecCurso(models.Model):
    det_gsc_horas = models.DecimalField(_('Horas Totales:'),max_digits=2, decimal_places=0)
    cepk_detgrcur = models.AutoField(primary_key=True)
    cepk_gradsec = models.ForeignKey('CeDetGradsecc', models.DO_NOTHING, db_column='cepk_gradsec')
    cepk_cur = models.ForeignKey(CeCurso, models.DO_NOTHING, db_column='cepk_cur')
    det_asig = models.DecimalField(max_digits=1, decimal_places=0,default='2', editable=False)
    
    
    class Meta:
        managed = False
        db_table = 'ce_det_gradsec_curso'
        unique_together = (('cepk_gradsec', 'cepk_cur', 'cepk_detgrcur'),)
        
class CeDetGradsecTut(models.Model):
    cepk_gradsec = models.ForeignKey('CeDetGradsecc', models.DO_NOTHING, db_column='cepk_gradsec')
    cepk_tut = models.ForeignKey('CeTutor', models.DO_NOTHING, db_column='cepk_tut')
    cepk_detgrtut = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'ce_det_gradsec_tut'
        unique_together = (('cepk_gradsec', 'cepk_tut', 'cepk_detgrtut'),)

class CeDetGradsecc(models.Model):
    cepk_grad = models.ForeignKey('CeGrado', models.DO_NOTHING, db_column='cepk_grad')
    cepk_secc = models.ForeignKey('CeSeccion', models.DO_NOTHING, db_column='cepk_secc')
    cepk_gradsec = models.AutoField(primary_key=True)
    ce_det_asignaciontut = models.DecimalField(db_column='ce_det_asignaciontut', max_digits=2, decimal_places=0,default='2',editable=False, blank=True, null=True)
    
    def __str__(self):
        return self.cepk_grad.grad_nombre+" "+self.cepk_grad.grad_nivel+", Seccion "+self.cepk_secc.secc_nombre
    
    
    class Meta:
        managed = False
        db_table = 'ce_det_gradsecc'
        unique_together = (('cepk_grad', 'cepk_secc', 'cepk_gradsec'),)


class CeDetProfcurso(models.Model):
    cepk_prof = models.ForeignKey('CeProfesor', models.DO_NOTHING, db_column='cepk_prof')
    cepk_detgrcur = models.ForeignKey(CeDetGradsecCurso, models.DO_NOTHING, db_column='cepk_detgrcur')
    cur_horas = models.DecimalField(_('Horas'),max_digits=2, decimal_places=0, blank=True, null=True)
    ecpk_detprocur = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'ce_det_profcurso'
        unique_together = (('cepk_prof', 'cepk_detgrcur', 'ecpk_detprocur'),)


class DistritoAdmin(admin.ModelAdmin):
    list_display = ('cepk_distrito', 'distr_nombre', 'distr_provincia', 'distr_departamento')
    
class CeGrado(models.Model):
    # cepk_grad = models.DecimalField(primary_key=True, max_digits=8, decimal_places=0)
    cepk_grad = models.AutoField(primary_key=True)
    grad_nivel = models.CharField(_('Nivel'),max_length=10, blank=True, null=True)
    grad_nombre = models.CharField(_('Nombre'),max_length=10, blank=True, null=True)

    def __str__(self):
        return self.grad_nombre
    class Meta:
        managed = False
        db_table = 'ce_grado'



class CeMatricula(models.Model):
    cepk_matr = models.AutoField(primary_key=True)
    cepk_alu = models.ForeignKey(CeAlumno, models.DO_NOTHING, db_column='cepk_alu')
    matr_fecha = models.DateField(_('Fecha de Matricula'))
    matr_estado = models.DecimalField(_('Estado'),max_digits=1, decimal_places=0)
    matr_observacion = models.CharField(_('Observacion'),max_length=20, blank=True, null=True)
    cepk_gradsec = models.ForeignKey(CeDetGradsecc, models.DO_NOTHING, db_column='cepk_gradsec')
    matr_edadalumno = models.DecimalField(_('Edad Alumno'),max_digits=2, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ce_matricula'



class CePerfil(models.Model):
#     cepk_perf = models.DecimalField(primary_key=True, max_digits=8, decimal_places=0)
    cepk_perf = models.AutoField(primary_key=True)
    perf_tperfil = models.DecimalField(max_digits=1, decimal_places=0)
    perf_descripcion = models.CharField(max_length=100, blank=True, null=True)
    perf_activo = models.DecimalField(max_digits=1, decimal_places=0)
    
    def _str_(self):
        return 'perfil' + self.perf_tperfil

    class Meta:
        managed = False
        db_table = 'ce_perfil'
        
 



class CeProfesor(models.Model):
    cepk_prof = models.AutoField(primary_key=True)
    cepk_per = models.ForeignKey(Persona, models.DO_NOTHING, db_column='cepk_per')
    prof_especialidad = models.CharField(_('Especialidad'),max_length=20, blank=True, null=True)
    prof_tipo = models.DecimalField(_('Tipo'),max_digits=1, decimal_places=0)
    porf_gacademico = models.CharField(_('Grado Academico'),max_length=20, blank=True, null=True)
    prof_estado = models.DecimalField(_('Estado'),max_digits=1, decimal_places=0)
    class Meta:
        managed = False
        db_table = 'ce_profesor'


class CeSeccion(models.Model):
    # cepk_secc = models.DecimalField(primary_key=True, max_digits=8, decimal_places=0)
    cepk_secc = models.AutoField(primary_key=True)
    secc_nombre = models.CharField(_('Nombre'),max_length=20, blank=True, null=True)
    #No es necesario cambiar aca, sino al momento de insertar
    secc_tipo = models.DecimalField(_('Tipo'),max_digits=1, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ce_seccion'


class CeTutor(models.Model):
    cepk_per = models.ForeignKey(Persona, models.DO_NOTHING, db_column='cepk_per')
    cepk_tut = models.AutoField(primary_key=True)
    tut_especialidad = models.CharField(_('Especialidad'),max_length=20, blank=True, null=True)
    tut_estado = models.DecimalField(_('Estado'),max_digits=1, decimal_places=0,default='2')
    
    class Meta:
        managed = False
        db_table = 'ce_tutor'


class CeUsuario(models.Model):
    cepk_usua = models.AutoField(primary_key=True)
    cepk_per = models.ForeignKey(Persona, models.DO_NOTHING, db_column='cepk_per')
    cepk_perf = models.ForeignKey(CePerfil, models.DO_NOTHING, db_column='cepk_perf')
    usua_testado = models.DecimalField(max_digits=1, decimal_places=0)
#   cepk_usua = models.DecimalField(primary_key=True, max_digits=8, decimal_places=0)
    usua_user = models.CharField(max_length=20)
    usua_password = models.CharField(max_length=20)


    class Meta:
        managed = False
        db_table = 'ce_usuario'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
        

class PersonaAdmin(admin.ModelAdmin):
    list_display = ('per_nombres', 'per_apellpat', 'per_apellmat', 'per_dni', 'per_telf')

class CeAsistencia(models.Model):
    cepk_grad = models.ForeignKey(CeGrado, models.DO_NOTHING, db_column='cepk_grad')
    cepk_secc = models.ForeignKey(CeSeccion, models.DO_NOTHING, db_column='cepk_secc')
    cepk_alu = models.ForeignKey(CeAlumno, models.DO_NOTHING, db_column='cepk_alu')
    asis_tutor = models.CharField(max_length=20, blank=True, null=True)
    cepk_asis = models.AutoField(primary_key=True)
    asis_valor = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'ce_asistencia'

class CeAula(models.Model):
    cepk_aul = models.AutoField(primary_key=True)
    cepk_grad = models.ForeignKey(CeGrado, models.DO_NOTHING, db_column='cepk_grad')
    cepk_secc = models.ForeignKey(CeSeccion, models.DO_NOTHING, db_column='cepk_secc')
    aul_pabellon = models.CharField(max_length=5, blank=True, null=True)
    aul_estado = models.CharField(max_length=5, blank=True, null=True)
    aul_capacidad = models.CharField(max_length=5, blank=True, null=True)
    aul_npiso = models.CharField(max_length=5, blank=True, null=True)
    aul_nombre = models.CharField(max_length=20, blank=True, null=True)
    

    class Meta:
        managed = False
        db_table = 'ce_aula'

class CeCatalogo(models.Model):
    cepk_cat = models.DecimalField(primary_key=True, max_digits=8, decimal_places=0)
    cat_general = models.DecimalField(max_digits=2, decimal_places=0)
    cat_secundario = models.DecimalField(max_digits=2, decimal_places=0)
    cat_descripcion = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'ce_catalogo'


    
    
admin.site.register(Distrito, DistritoAdmin)
admin.site.register(Persona, PersonaAdmin)
admin.site.register(CeCurso)

