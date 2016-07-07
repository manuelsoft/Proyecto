# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-29 06:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'managed': False,
                'db_table': 'auth_group',
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'managed': False,
                'db_table': 'auth_group_permissions',
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'managed': False,
                'db_table': 'auth_permission',
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=30, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'managed': False,
                'db_table': 'auth_user',
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'managed': False,
                'db_table': 'auth_user_groups',
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'managed': False,
                'db_table': 'auth_user_user_permissions',
            },
        ),
        migrations.CreateModel(
            name='CeAlumno',
            fields=[
                ('cepk_alu', models.AutoField(primary_key=True, serialize=False)),
                ('alu_nhnos', models.DecimalField(blank=True, decimal_places=0, max_digits=2, null=True)),
                ('alu_altura', models.DecimalField(blank=True, decimal_places=2, max_digits=2, null=True)),
                ('alu_estado', models.DecimalField(max_digits=1, decimal_places=0)),
            ],
            options={
                'managed': False,
                'db_table': 'ce_alumno',
            },
        ),
        migrations.CreateModel(
            name='CeAsistencia',
            fields=[
                ('asis_tutor', models.CharField(blank=True, max_length=20, null=True)),
                ('cepk_asis', models.AutoField(primary_key=True, serialize=False)),
                ('asis_valor', models.DecimalField(blank=True, decimal_places=0, max_digits=1, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'ce_asistencia',
            },
        ),
        migrations.CreateModel(
            name='CeAula',
            fields=[
                ('cepk_aul', models.AutoField(primary_key=True, serialize=False)),
                ('aul_pabellon', models.CharField(blank=True, max_length=5, null=True)),
                ('aul_estado', models.CharField(blank=True, max_length=5, null=True)),
                ('aul_capacidad', models.CharField(blank=True, max_length=5, null=True)),
                ('aul_npiso', models.CharField(blank=True, max_length=5, null=True)),
                ('aul_nombre', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'ce_aula',
            },
        ),
        migrations.CreateModel(
            name='CeCalificacion',
            fields=[
                ('cepk_calf', models.DecimalField(decimal_places=0, max_digits=8, primary_key=True, serialize=False)),
                ('calf_notapract', models.DecimalField(blank=True, decimal_places=2, max_digits=2, null=True)),
                ('calf_notaexam', models.DecimalField(blank=True, decimal_places=2, max_digits=2, null=True)),
                ('calf_notaconducta', models.DecimalField(blank=True, decimal_places=2, max_digits=2, null=True)),
                ('calf_notaoral', models.DecimalField(blank=True, decimal_places=2, max_digits=2, null=True)),
                ('calf_promcurso', models.DecimalField(blank=True, decimal_places=0, max_digits=2, null=True)),
                ('calf_fechareg', models.DateField(blank=True, null=True)),
                ('calf_bimestre', models.DecimalField(blank=True, decimal_places=0, max_digits=1, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'ce_calificacion',
            },
        ),
        migrations.CreateModel(
            name='CeCurso',
            fields=[
                ('cepk_cur', models.AutoField(primary_key=True, serialize=False)),
                ('cur_nombre', models.CharField(blank=True, max_length=25, null=True)),
                ('cur_tipo', models.CharField(blank=True, max_length=5, null=True)),
                ('cur_testado', models.CharField(blank=True, max_length=5, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'ce_curso',
            },
        ),
        migrations.CreateModel(
            name='CeDetAlucurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cepk_alucurso', models.DecimalField(decimal_places=0, max_digits=8)),
            ],
            options={
                'managed': False,
                'db_table': 'ce_det_alucurso',
            },
        ),
        migrations.CreateModel(
            name='CeDetGradsecc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cepk_gradsec', models.DecimalField(decimal_places=0, max_digits=8, unique=True)),
            ],
            options={
                'managed': False,
                'db_table': 'ce_det_gradsecc',
            },
        ),
        #No necesita 'id' cuando tiene el primary key explicito
        migrations.CreateModel(
            name='CeDetGradsecCurso',
            fields=[
                ('det_gsc_horas', models.DecimalField(blank=True, decimal_places=0, max_digits=2, null=True)),
                ('cepk_detgrcur', models.DecimalField(decimal_places=0, max_digits=8, unique=True)),
            ],
            options={
                'managed': False,
                'db_table': 'ce_det_gradsec_curso',
            },
        ),
        migrations.CreateModel(
            name='CeDetProfcurso',
            fields=[
                ('cur_horas', models.DecimalField(blank=True, decimal_places=0, max_digits=2, null=True)),
                ('ecpk_detprocur', models.DecimalField(decimal_places=0, max_digits=8, unique=True)),
            ],
            options={
                'managed': False,
                'db_table': 'ce_det_profcurso',
            },
        ),
        migrations.CreateModel(
            name='CeGrado',
            fields=[
                ('cepk_grad', models.AutoField(primary_key=True, serialize=False)),
                ('grad_nivel', models.CharField(blank=True, max_length=10, null=True)),
                ('grad_nombre', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'ce_grado',
            },
        ),
        migrations.CreateModel(
            name='CeMatricula',
            fields=[
                ('cepk_secc', models.DecimalField(decimal_places=0, max_digits=8)),
                ('cepk_matr', models.DecimalField(decimal_places=0, max_digits=8, primary_key=True, serialize=False)),
                ('matr_fecha', models.DateField()),
                ('matr_estado', models.DecimalField(decimal_places=0, max_digits=1)),
                ('matr_observacion', models.CharField(blank=True, max_length=20, null=True)),
                ('cepk_gradsec', models.DecimalField(decimal_places=0, max_digits=8)),
                ('matr_edadalumno', models.DecimalField(blank=True, decimal_places=0, max_digits=2, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'ce_matricula',
            },
        ),
        migrations.CreateModel(
            name='CePerfil',
            fields=[
                ('cepk_perf', models.DecimalField(decimal_places=0, max_digits=8, primary_key=True, serialize=False)),
                ('perf_tperfil', models.DecimalField(decimal_places=0, max_digits=1)),
                ('perf_descripcion', models.CharField(blank=True, max_length=100, null=True)),
                ('perf_activo', models.DecimalField(decimal_places=0, max_digits=1)),
            ],
            options={
                'managed': False,
                'db_table': 'ce_perfil',
            },
        ),
        migrations.CreateModel(
            name='CeProfesor',
            fields=[
                ('cepk_prof', models.DecimalField(decimal_places=0, max_digits=8, primary_key=True, serialize=False)),
                ('prof_especialidad', models.CharField(blank=True, max_length=20, null=True)),
                ('prof_tipo', models.DecimalField(decimal_places=0, max_digits=1)),
                ('porf_gacademico', models.CharField(blank=True, max_length=20, null=True)),
                ('prof_estado', models.DecimalField(decimal_places=0, max_digits=1)),
            ],
            options={
                'managed': False,
                'db_table': 'ce_profesor',
            },
        ),
        migrations.CreateModel(
            name='CeSeccion',
            fields=[
                ('cepk_secc', models.AutoField(primary_key=True, serialize=False)),
                ('secc_nombre', models.CharField(blank=True, max_length=20, null=True)),
                ('secc_tipo', models.DecimalField(blank=True, decimal_places=0, max_digits=1, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'ce_seccion',
            },
        ),
        migrations.CreateModel(
            name='CeTutor',
            fields=[
                ('cepk_tut', models.DecimalField(decimal_places=0, max_digits=8, primary_key=True, serialize=False)),
                ('tut_especialidad', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'ce_tutor',
            },
        ),
        migrations.CreateModel(
            name='CeUsuario',
            fields=[
                ('usua_testado', models.DecimalField(decimal_places=0, max_digits=1)),
                ('cepk_usua', models.DecimalField(decimal_places=0, max_digits=8, primary_key=True, serialize=False)),
                ('usua_password', models.CharField(max_length=20)),
                ('usua_user', models.CharField(max_length=20)),
            ],
            options={
                'managed': False,
                'db_table': 'ce_usuario',
            },
        ),
        migrations.CreateModel(
            name='Distrito',
            fields=[
                ('cepk_distrito', models.AutoField(primary_key=True, serialize=False)),
                ('distr_departamento', models.CharField(max_length=20)),
                ('distr_provincia', models.CharField(max_length=20)),
                ('distr_nombre', models.CharField(max_length=20)),
            ],
            options={
                'managed': False,
                'db_table': 'ce_distrito',
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'managed': False,
                'db_table': 'django_admin_log',
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'managed': False,
                'db_table': 'django_content_type',
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'managed': False,
                'db_table': 'django_migrations',
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'managed': False,
                'db_table': 'django_session',
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('cepk_per', models.AutoField(primary_key=True, serialize=False)),
                ('per_nombres', models.CharField(max_length=40)),
                ('per_apellpat', models.CharField(max_length=20)),
                ('per_apellmat', models.CharField(max_length=20)),
                ('per_dni', models.DecimalField(decimal_places=0, max_digits=8)),
                ('per_telf', models.DecimalField(decimal_places=0, max_digits=9)),
                ('per_nomcalle', models.CharField(blank=True, max_length=40, null=True)),
                ('per_email', models.CharField(blank=True, max_length=50, null=True)),
                ('per_fechnac', models.DateField()),
            ],
            options={
                'managed': False,
                'db_table': 'ce_persona',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField(max_length=200)),
            ],
        ),
    ]
