from django.db import models
from django.conf import settings
import os
from django.core.validators import FileExtensionValidator

class EjemploormPersona(models.Model):
    rut = models.CharField(primary_key=True, max_length=13)
    nombre = models.CharField(max_length=20)
    correo_electronico = models.CharField(unique=True, max_length=40)
    direccion = models.CharField(max_length=50)
    contrasenna = models.CharField(max_length=15)
    telefono = models.CharField(max_length=15)
    perfil = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'ejemploorm_persona'

class EjemploormProductos(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    thumbnail = models.CharField(max_length=100, blank=True, null=True)
    slug = models.CharField(unique=True, max_length=50)
    content_file = models.CharField(max_length=100, blank=True, null=True)
    active = models.IntegerField()
    price = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ejemploorm_productos'


class EjemploormProductoscomprados(models.Model):
    email = models.CharField(max_length=254)
    date_purchased = models.DateTimeField()
    productos = models.ForeignKey(EjemploormProductos, models.DO_NOTHING, db_column='Productos_id')  # Field name made lowercase.
    rut = models.ForeignKey(EjemploormPersona, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ejemploorm_productoscomprados'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

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
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
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


class EjemploormCategoria(models.Model):
    id_categoria = models.CharField(primary_key=True, max_length=10)
    nombre_cat = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'ejemploorm_categoria'


class EjemploormCiudad(models.Model):
    id_ciudad = models.CharField(primary_key=True, max_length=10)
    nombre_ciudad = models.CharField(max_length=50)
    id_region = models.ForeignKey('EjemploormRegion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ejemploorm_ciudad'


class EjemploormCliente(models.Model):
    rut_cliente = models.CharField(primary_key=True, max_length=20)
    nombre_cliente = models.CharField(max_length=50)
    apellido_cliente = models.CharField(max_length=50)
    telefono = models.CharField(max_length=30)
    sexo = models.CharField(max_length=20)
    correo = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    fecha_nac = models.DateField()
    fecha_registro = models.DateTimeField()
    id_ciudad = models.ForeignKey(EjemploormCiudad, models.DO_NOTHING)
    id_comuna = models.ForeignKey('EjemploormComuna', models.DO_NOTHING)
    id_credencial = models.ForeignKey('EjemploormCredencial', models.DO_NOTHING)
    id_pais = models.ForeignKey('EjemploormPais', models.DO_NOTHING)
    id_region = models.ForeignKey('EjemploormRegion', models.DO_NOTHING)
    id_rol = models.ForeignKey('EjemploormRol', models.DO_NOTHING)
    password = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'ejemploorm_cliente'


class EjemploormComuna(models.Model):
    id_comuna = models.CharField(primary_key=True, max_length=10)
    nombre_comuna = models.CharField(max_length=50)
    id_ciudad = models.ForeignKey(EjemploormCiudad, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ejemploorm_comuna'


class EjemploormCredencial(models.Model):
    id_credencial = models.CharField(primary_key=True, max_length=10)
    correo = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    estado = models.CharField(max_length=20)
    fecha_update = models.DateField()

    class Meta:
        managed = False
        db_table = 'ejemploorm_credencial'


class EjemploormHistorial(models.Model):
    id_historial = models.CharField(primary_key=True, max_length=10)
    id_producto = models.ForeignKey('EjemploormProducto', models.DO_NOTHING)
    id_venta = models.ForeignKey('EjemploormVenta', models.DO_NOTHING)
    rut_cliente = models.ForeignKey(EjemploormCliente, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ejemploorm_historial'


class EjemploormImgproducto(models.Model):
    id_img = models.CharField(primary_key=True, max_length=50)
    descripcion = models.CharField(max_length=100)
    id_producto = models.ForeignKey('EjemploormProducto', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ejemploorm_imgproducto'


class EjemploormLogProductos(models.Model):
    id_prod = models.IntegerField()
    name_prod = models.CharField(max_length=100)
    price_prod = models.IntegerField()
    inserted = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    deleted = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ejemploorm_log_productos'


class EjemploormOrdencompra(models.Model):
    nro_orden = models.CharField(primary_key=True, max_length=10)
    precio = models.PositiveIntegerField()
    cantidad = models.PositiveIntegerField()
    estado = models.CharField(max_length=20)
    medio_pago = models.CharField(max_length=30)
    id_producto = models.ForeignKey('EjemploormProducto', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ejemploorm_ordencompra'


class EjemploormPais(models.Model):
    id_pais = models.CharField(primary_key=True, max_length=10)
    nombre_pais = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'ejemploorm_pais'




def marketplace_directory_path(instance, filename):
    banner_pic_name='products/{0}/{1}'.format(instance.name, filename)
    full_path = os.path.join(settings.MEDIA_ROOT, banner_pic_name)

class EjemploormProducto(models.Model):
    id_producto = models.CharField(primary_key=True, max_length=10)
    nombre_prod = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    precio_cl = models.PositiveIntegerField()
    precio_usd = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    imagen = models.CharField(max_length=100)
    titulo = models.CharField(max_length=30)
    subtitulo = models.CharField(max_length=30)
    introduccion = models.CharField(max_length=50)
    talla = models.CharField(max_length=30)
    materiales = models.CharField(max_length=100)
    medidas = models.CharField(max_length=100)
    color = models.CharField(max_length=30)
    archivo_pdf = models.CharField(max_length=100)
    id_categoria = models.ForeignKey(EjemploormCategoria, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ejemploorm_producto'





class EjemploormRegion(models.Model):
    id_region = models.CharField(primary_key=True, max_length=10)
    nombre_region = models.CharField(max_length=50)
    id_pais = models.ForeignKey(EjemploormPais, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ejemploorm_region'

class EjemploormRol(models.Model):
    id_rol = models.CharField(primary_key=True, max_length=10)
    rol_admin = models.IntegerField()
    rol_cliente = models.IntegerField()
    rol_emprendedor = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ejemploorm_rol'

class productosComprados(models.Model):
    rut = models.ForeignKey(EjemploormPersona,on_delete=models.CASCADE, related_name="products")
    email = models.EmailField()
    Productos = models.ForeignKey(EjemploormProductos, on_delete=models.CASCADE)
    date_purchased = models.DateTimeField(auto_now_add=True)

class EjemploormVenta(models.Model):
    id_venta = models.CharField(primary_key=True, max_length=10)
    fecha_venta = models.DateField()
    id_producto = models.ForeignKey(EjemploormProducto, models.DO_NOTHING)
    nro_orden = models.ForeignKey(EjemploormOrdencompra, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ejemploorm_venta'