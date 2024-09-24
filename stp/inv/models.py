from django.db import models

from bases.models import ClaseModelo


class Categoria(ClaseModelo):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(
        max_length = 100,
        help_text = 'Descripción de la Categoría',
        unique = True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Categoria, self).save()

    class Meta:
        verbose_name_plural = "Categorias"


class SubCategoria(ClaseModelo):
    id = models.AutoField(primary_key=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la Categoría'
    )

    def __str__(self):
        return '{}:{}'.format(self.categoria.descripcion, self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(SubCategoria, self).save()

    class Meta:
        verbose_name_plural = "Sub Categorias"
        unique_together = ('categoria', 'descripcion')


class Marca(ClaseModelo):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la Marca',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Marca, self).save()

    class Meta:
        verbose_name_plural = "Marca"


class UnidadMedida(ClaseModelo):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la Unidad Medida',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(UnidadMedida, self).save()

    class Meta:
        verbose_name_plural = "Unidades de Medida"


class Producto(ClaseModelo):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(
        max_length=20,
        unique=True
    )
    codigo_barra = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    precio = models.FloatField(default=0)
    existencia = models.IntegerField(default=0)
    ultima_compra = models.DateField(null=True, blank=True)

    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    unidad_medida = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to="images/", null=True,blank=True)

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Producto, self).save()

    class Meta:
        verbose_name_plural = "Productos"
        unique_together = ('codigo', 'codigo_barra')

    # This is an auto-generated Django model module.
    # You'll have to do the following manually to clean this up:
    #   * Rearrange models' order
    #   * Make sure each model has one field with primary_key=True
    #   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
    #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
    # Feel free to rename the models, but don't rename db_table values or field names.


"""
class Areq(ClaseModelo):
    nro = models.FloatField(db_column='NRO', blank=True, null=True)  # Field name made lowercase.
    f2 = models.CharField(db_column='F2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    f6 = models.CharField(db_column='F6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    f7 = models.FloatField(db_column='F7', blank=True, null=True)  # Field name made lowercase.
    f8 = models.DecimalField(db_column='F8', max_digits=19, decimal_places=4, blank=True,
                             null=True)  # Field name made lowercase.
    f72 = models.DecimalField(db_column='F72', max_digits=19, decimal_places=4, blank=True,
                              null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AREQ'
"""


class AsMotivos(ClaseModelo):
    idmot = models.AutoField(db_column='IDMOT', primary_key=True)  # Field name made lowercase.
    codarea = models.IntegerField(db_column='CODAREA', blank=True, null=True)  # Field name made lowercase.
    codmot = models.IntegerField(db_column='CODMOT', blank=True, null=True)  # Field name made lowercase.
    desmotivo = models.CharField(db_column='DESMOTIVO', max_length=70, blank=True,
                                 null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AS_Motivos'


class Archivoinformebaja(ClaseModelo):
    item = models.AutoField(db_column='Item', primary_key=True)  # Field name made lowercase.
    nrosolling = models.BigIntegerField(db_column='Nrosolling')  # Field name made lowercase.
    archivo = models.BinaryField(db_column='Archivo', blank=True, null=True)  # Field name made lowercase.
    fecpro = models.DateTimeField(db_column='FecPro', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ArchivoInformeBaja'

class Califica(ClaseModelo):
    item = models.AutoField(primary_key=True)
    descripcion = models.CharField(db_column='Descripcion', max_length=100, blank=True,
                                   null=True)  # Field name made lowercase.
    estado = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Califica'

class Cecofinal(ClaseModelo):
    id = models.FloatField(db_column='ID', blank=True, null=False, primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=255, blank=True,
                                   null=True)  # Field name made lowercase.
    cecos = models.CharField(db_column='CECOS', max_length=255, blank=True,
                             null=True)  # Field name made lowercase.
    depend = models.FloatField(db_column='DEPEND', blank=True, null=True)  # Field name made lowercase.
    cebes = models.CharField(db_column='CEBES', max_length=255, blank=True,
                             null=True)  # Field name made lowercase.
    ceges = models.CharField(db_column='CEGES', max_length=255, blank=True,
                             null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CecoFINAL'

# class Cecosap(ClaseModelo):
#     cecod = models.FloatField(db_column='CECOD', blank=True, null=True)  # Field name made lowercase.
#     cecnom = models.CharField(db_column='CECNOM', max_length=255, blank=True,
#                               null=True)  # Field name made lowercase.
#     cecnum = models.CharField(db_column='CECNUM', max_length=255, blank=True,
#                               null=True)  # Field name made lowercase.
#     cecdep = models.FloatField(db_column='CECDEP', blank=True, null=True)  # Field name made lowercase.
#     cebes = models.CharField(db_column='CEBES', max_length=10, blank=True,
#                              null=True)  # Field name made lowercase.
#     ceges = models.CharField(db_column='CEGES', max_length=10, blank=True,
#                              null=True)  # Field name made lowercase.
#     estado = models.CharField(db_column='ESTADO', max_length=1, blank=True,
#                               null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CecoSap'
#
# class Cecosapult(ClaseModelo):
#     cecod = models.FloatField(db_column='CECOD', blank=True, null=True)  # Field name made lowercase.
#     cecnom = models.CharField(db_column='CECNOM', max_length=255, blank=True,
#                               null=True)  # Field name made lowercase.
#     cecnum = models.CharField(db_column='CECNUM', max_length=255, blank=True,
#                               null=True)  # Field name made lowercase.
#     cecdep = models.FloatField(db_column='CECDEP', blank=True, null=True)  # Field name made lowercase.
#     cebes = models.CharField(db_column='CEBES', max_length=10, blank=True,
#                              null=True)  # Field name made lowercase.
#     ceges = models.CharField(db_column='CEGES', max_length=10, blank=True,
#                              null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CecoSapUlt'

class Contratoorden(ClaseModelo):
    item = models.AutoField(primary_key=True)
    idcontrato = models.IntegerField(blank=True, null=True)
    orden = models.CharField(max_length=50, blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True, null=True)
    cuenta = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ContratoOrden'

class Destino(ClaseModelo):
    coddes = models.IntegerField(db_column='CodDes', blank=True, null=False, primary_key=True)  # Field name made lowercase.
    desdestino = models.CharField(db_column='DesDestino', max_length=50, blank=True,
                                  null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=1, blank=True,
                              null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Destino'

# class Hojaxx2(ClaseModelo):
#     codigo = models.FloatField(db_column='CODIGO', blank=True, null=True)  # Field name made lowercase.
#     tipopenalidad = models.FloatField(db_column='TIPOPENALIDAD', blank=True,
#                                       null=True)  # Field name made lowercase.
#     f3 = models.CharField(db_column='F3', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     unidad = models.CharField(db_column='UNIDAD', max_length=255, blank=True,
#                               null=True)  # Field name made lowercase.
#     pu = models.FloatField(db_column='PU', blank=True, null=True)  # Field name made lowercase.
#     adicional = models.CharField(db_column='ADICIONAL', max_length=255, blank=True,
#                                  null=True)  # Field name made lowercase.
#     contrato = models.FloatField(db_column='CONTRATO', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'Hojaxx2'

# class Hojaxx3(ClaseModelo):
#     a = models.FloatField(db_column='A', blank=True, null=True)  # Field name made lowercase.
#     b = models.FloatField(db_column='B', blank=True, null=True)  # Field name made lowercase.
#     c = models.CharField(db_column='C', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     e = models.CharField(db_column='E', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     f = models.FloatField(db_column='F', blank=True, null=True)  # Field name made lowercase.
#     g = models.CharField(db_column='G', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     h = models.FloatField(db_column='H', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'Hojaxx3'
#
# class Hojaxxx(ClaseModelo):
#     codigo = models.FloatField(db_column='Codigo', blank=True, null=True)  # Field name made lowercase.
#     idtipopenalidad = models.FloatField(db_column='IDTipoPenalidad', blank=True,
#                                         null=True)  # Field name made lowercase.
#     nombre = models.CharField(db_column='Nombre', max_length=255, blank=True,
#                               null=True)  # Field name made lowercase.
#     unidad = models.CharField(db_column='Unidad', max_length=255, blank=True,
#                               null=True)  # Field name made lowercase.
#     pu = models.FloatField(db_column='PU', blank=True, null=True)  # Field name made lowercase.
#     adicional = models.CharField(db_column='Adicional', max_length=255, blank=True,
#                                  null=True)  # Field name made lowercase.
#     f7 = models.FloatField(db_column='F7', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'Hojaxxx'

class Imaterial(ClaseModelo):
    idcod = models.BigIntegerField(db_column='IdCod', blank=True, null=False, primary_key=True)  # Field name made lowercase.
    bukrs = models.CharField(db_column='BUKRS', max_length=4, blank=True,
                             null=True)  # Field name made lowercase.
    mjahr = models.IntegerField(db_column='MJAHR', blank=True, null=True)  # Field name made lowercase.
    werks = models.CharField(db_column='WERKS', max_length=4, blank=True,
                             null=True)  # Field name made lowercase.
    lgort = models.CharField(db_column='LGORT', max_length=4, blank=True,
                             null=True)  # Field name made lowercase.
    bwart = models.CharField(db_column='BWART', max_length=3, blank=True,
                             null=True)  # Field name made lowercase.
    mblnr = models.CharField(db_column='MBLNR', max_length=10, blank=True,
                             null=True)  # Field name made lowercase.
    zeile = models.IntegerField(db_column='ZEILE', blank=True, null=True)  # Field name made lowercase.
    budat = models.CharField(db_column='BUDAT', max_length=8, blank=True,
                             null=True)  # Field name made lowercase.
    usnam = models.CharField(db_column='USNAM', max_length=12, blank=True,
                             null=True)  # Field name made lowercase.
    matnr = models.CharField(db_column='MATNR', max_length=18, blank=True,
                             null=True)  # Field name made lowercase.
    maktx = models.CharField(db_column='MAKTX', max_length=40, blank=True,
                             null=True)  # Field name made lowercase.
    erfmg = models.DecimalField(db_column='ERFMG', max_digits=13, decimal_places=3, blank=True,
                                null=True)  # Field name made lowercase.
    erfme = models.CharField(db_column='ERFME', max_length=3, blank=True,
                             null=True)  # Field name made lowercase.
    dmbtr = models.DecimalField(db_column='DMBTR', max_digits=13, decimal_places=2, blank=True,
                                null=True)  # Field name made lowercase.
    waers = models.CharField(db_column='WAERS', max_length=5, blank=True,
                             null=True)  # Field name made lowercase.
    aufnr = models.CharField(db_column='AUFNR', max_length=12, blank=True,
                             null=True)  # Field name made lowercase.
    rsnum = models.CharField(db_column='RSNUM', max_length=10, blank=True,
                             null=True)  # Field name made lowercase.
    rspos = models.IntegerField(db_column='RSPOS', blank=True, null=True)  # Field name made lowercase.
    sjahr = models.IntegerField(db_column='SJAHR', blank=True, null=True)  # Field name made lowercase.
    smbln = models.CharField(db_column='SMBLN', max_length=10, blank=True,
                             null=True)  # Field name made lowercase.
    smblp = models.IntegerField(db_column='SMBLP', blank=True, null=True)  # Field name made lowercase.
    xblnr = models.CharField(db_column='XBLNR', max_length=16, blank=True,
                             null=True)  # Field name made lowercase.
    auart = models.CharField(db_column='AUART', max_length=4, blank=True,
                             null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='ESTADO', max_length=2, blank=True,
                              null=True)  # Field name made lowercase.
    fecpro = models.DateTimeField(db_column='FECPRO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IMaterial'

class Item2(ClaseModelo):
    nivel_contrato = models.FloatField(db_column='nivel contrato', blank=True,
                                       null=True)  # Field renamed to remove unsuitable characters.
    detalle = models.CharField(max_length=255, blank=True, null=True)
    unidad = models.CharField(max_length=255, blank=True, null=True)
    pu_field = models.FloatField(db_column='pu ', blank=True,
                                 null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    estado = models.FloatField(blank=True, null=True)
    codact = models.FloatField(blank=True, null=False, primary_key=True)
    codant = models.CharField(max_length=255, blank=True, null=True)
    ca = models.CharField(max_length=255, blank=True, null=True)
    cn = models.CharField(max_length=255, blank=True, null=True)
    idcontrato = models.FloatField(blank=True, null=True)
    idareadm = models.FloatField(blank=True, null=True)
    idloc = models.FloatField(blank=True, null=True)
    ctatipo = models.CharField(max_length=255, blank=True, null=True)
    ctastipo = models.CharField(max_length=255, blank=True, null=True)
    cantidad = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Item2'

# class Liqar4(ClaseModelo):
#     liqnu1 = models.AutoField(db_column='Liqnu1')  # Field name made lowercase.
#     liqnu2 = models.BigIntegerField(db_column='Liqnu2', blank=True, null=True)  # Field name made lowercase.
#     liqnu3 = models.BigIntegerField(db_column='Liqnu3', blank=True, null=True)  # Field name made lowercase.
#     liqfec = models.DateTimeField(db_column='LiqFec', blank=True, null=True)  # Field name made lowercase.
#     liqeje = models.CharField(db_column='LiqEje', max_length=10, blank=True,
#                               null=True)  # Field name made lowercase.
#     codliquidador = models.CharField(db_column='CodLiquidador', max_length=10, blank=True,
#                                      null=True)  # Field name made lowercase.
#     observacion = models.CharField(db_column='Observacion', max_length=250, blank=True,
#                                    null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'Liqar4'
#
# class Liqar5(ClaseModelo):
#     liqnu4 = models.BigIntegerField(db_column='LiqNu4', blank=True, null=True)  # Field name made lowercase.
#     liqco7 = models.IntegerField(db_column='LiqCo7', blank=True, null=True)  # Field name made lowercase.
#     liqmat = models.CharField(db_column='LiqMat', max_length=10, blank=True,
#                               null=True)  # Field name made lowercase.
#     liqcan = models.DecimalField(db_column='LiqCan', max_digits=11, decimal_places=2, blank=True,
#                                  null=True)  # Field name made lowercase.
#     identificador1 = models.CharField(db_column='Identificador1', max_length=100, blank=True,
#                                       null=True)  # Field name made lowercase.
#     identificador2 = models.CharField(db_column='Identificador2', max_length=100, blank=True,
#                                       null=True)  # Field name made lowercase.
#     subestacion = models.CharField(db_column='Subestacion', max_length=10, blank=True,
#                                    null=True)  # Field name made lowercase.
#     set1 = models.CharField(db_column='Set1', max_length=10, blank=True,
#                             null=True)  # Field name made lowercase.
#     alimentador = models.CharField(db_column='Alimentador', max_length=10, blank=True,
#                                    null=True)  # Field name made lowercase.
#     feceje = models.CharField(db_column='FecEje', max_length=10, blank=True,
#                               null=True)  # Field name made lowercase.
#     tipo = models.CharField(db_column='Tipo', max_length=10, blank=True,
#                             null=True)  # Field name made lowercase.
#     lineas = models.CharField(db_column='Lineas', max_length=10, blank=True,
#                               null=True)  # Field name made lowercase.
#     idem = models.CharField(max_length=10, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'Liqar5'

class Mataut(ClaseModelo):
    idusuario = models.IntegerField(db_column='IDUsuario', blank=True, null=False, primary_key=True)  # Field name made lowercase.
    idgerencia = models.IntegerField(db_column='IDGerencia', blank=True,
                                     null=True)  # Field name made lowercase.
    idunidad = models.IntegerField(db_column='IDUnidad', blank=True, null=True)  # Field name made lowercase.
    flagrev = models.CharField(db_column='FlagRev', max_length=1, blank=True,
                               null=True)  # Field name made lowercase.
    flagaut = models.CharField(db_column='FlagAut', max_length=1, blank=True,
                               null=True)  # Field name made lowercase.
    fecalta = models.DateTimeField(db_column='FecAlta', blank=True, null=True)  # Field name made lowercase.
    fecbaja = models.DateTimeField(db_column='FecBaja', blank=True, null=True)  # Field name made lowercase.
    flaging = models.CharField(db_column='FlagIng', max_length=1, blank=True,
                               null=True)  # Field name made lowercase.
    flagcom = models.CharField(db_column='FlagCom', max_length=1, blank=True,
                               null=True)  # Field name made lowercase.
    flagreving = models.CharField(db_column='FlagRevIng', max_length=1, blank=True,
                                  null=True)  # Field name made lowercase.
    flagliqui = models.CharField(db_column='FlagLiqui', max_length=1, blank=True,
                                 null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MatAut'

class Nimaz(ClaseModelo):
    nimaz = models.FloatField(db_column='NIMAZ', blank=True, null=False, primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Nimaz'

class Nimc2(ClaseModelo):
    suministro = models.FloatField(blank=True, null=False, primary_key=True)
    serie = models.FloatField(blank=True, null=True)
    nim = models.FloatField(blank=True, null=True)
    fechaejecucion = models.DateTimeField(db_column='FechaEjecucion', blank=True,
                                          null=True)  # Field name made lowercase.
    orden = models.CharField(max_length=255, blank=True, null=True)
    tipo = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Nimc2'

class Nimcrev1(ClaseModelo):
    nim = models.FloatField(db_column='NIM', blank=True, null=False, primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Nimcrev1'

class Nimcrev2(ClaseModelo):
    nimr2 = models.FloatField(blank=True, null=False, primary_key=True)

    class Meta:
        managed = False
        db_table = 'Nimcrev2'

class Nomcontratos(ClaseModelo):
    item = models.AutoField(primary_key=True)
    idcontrato = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(db_column='Nombre', max_length=50, blank=True,
                              null=True)  # Field name made lowercase.
    estado = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'NomContratos'

class Notdet(ClaseModelo):
    nrosolsal = models.BigIntegerField(db_column='NroSolSal', blank=True,
                                       null=False, primary_key=True)  # Field name made lowercase.
    nroressap = models.CharField(db_column='NroResSap', max_length=20, blank=True,
                                 null=True)  # Field name made lowercase.
    nrosapsal = models.CharField(db_column='NroSapSal', max_length=20, blank=True,
                                 null=True)  # Field name made lowercase.
    item = models.IntegerField(db_column='Item', blank=True, null=True)  # Field name made lowercase.
    codmat = models.CharField(db_column='CodMat', max_length=10, blank=True,
                              null=True)  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=15, decimal_places=2, blank=True,
                                   null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NotDet'

class Noting(ClaseModelo):
    nrosoling = models.BigAutoField(db_column='NroSolIng', primary_key=True)  # Field name made lowercase.
    nroing = models.BigIntegerField(db_column='NroIng', blank=True, null=True)  # Field name made lowercase.
    fecela = models.DateTimeField(db_column='FecEla', blank=True, null=True)  # Field name made lowercase.
    fecrev = models.DateTimeField(db_column='FecRev', blank=True, null=True)  # Field name made lowercase.
    fecing = models.DateTimeField(db_column='FecIng', blank=True, null=True)  # Field name made lowercase.
    almacen = models.CharField(db_column='Almacen', max_length=10, blank=True,
                               null=True)  # Field name made lowercase.
    gerencia = models.CharField(db_column='Gerencia', max_length=10, blank=True,
                                null=True)  # Field name made lowercase.
    unidad = models.CharField(db_column='Unidad', max_length=10, blank=True,
                              null=True)  # Field name made lowercase.
    emplaza = models.CharField(db_column='Emplaza', max_length=10, blank=True,
                               null=True)  # Field name made lowercase.
    empresa = models.CharField(db_column='Empresa', max_length=10, blank=True,
                               null=True)  # Field name made lowercase.
    codtiping = models.IntegerField(db_column='CodTipIng', blank=True, null=True)  # Field name made lowercase.
    motivo = models.CharField(db_column='Motivo', max_length=350, blank=True,
                              null=True)  # Field name made lowercase.
    nrosolsal = models.IntegerField(db_column='NroSolSal', blank=True, null=True)  # Field name made lowercase.
    entcodigo = models.CharField(db_column='EntCodigo', max_length=10, blank=True,
                                 null=True)  # Field name made lowercase.
    codrevision = models.CharField(db_column='CodRevision', max_length=10, blank=True,
                                   null=True)  # Field name made lowercase.
    codalmacenero = models.CharField(db_column='CodAlmacenero', max_length=10, blank=True,
                                     null=True)  # Field name made lowercase.
    nroordensap = models.CharField(db_column='NroOrdenSap', max_length=20, blank=True,
                                   null=True)  # Field name made lowercase.
    estnoting = models.CharField(db_column='EstNotIng', max_length=1, blank=True,
                                 null=True)  # Field name made lowercase.
    nroorden = models.CharField(db_column='NroOrden', max_length=20, blank=True,
                                null=True)  # Field name made lowercase.
    nrosapsal = models.CharField(db_column='NroSapSal', max_length=20, blank=True,
                                 null=True)  # Field name made lowercase.
    nroressal = models.CharField(db_column='NroResSal', max_length=20, blank=True,
                                 null=True)  # Field name made lowercase.
    nroingsap = models.CharField(db_column='NroIngSap', max_length=20, blank=True,
                                 null=True)  # Field name made lowercase.
    nroguia = models.CharField(db_column='NroGuia', max_length=20, blank=True,
                               null=True)  # Field name made lowercase.
    codurs = models.IntegerField(db_column='CodUrs', blank=True, null=True)  # Field name made lowercase.
    observacion = models.CharField(db_column='Observacion', max_length=350, blank=True,
                                   null=True)  # Field name made lowercase.
    calificacion = models.CharField(db_column='Calificacion', max_length=1, blank=True,
                                    null=True)  # Field name made lowercase.
    fecanu = models.DateTimeField(db_column='FecAnu', blank=True, null=True)  # Field name made lowercase.
    desanu = models.CharField(db_column='DesAnu', max_length=350, blank=True,
                              null=True)  # Field name made lowercase.
    codanu = models.CharField(db_column='CodAnu', max_length=10, blank=True,
                              null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NotIng'

class Notingdet(ClaseModelo):
    nrosoling = models.BigIntegerField(db_column='NroSolIng', blank=True,
                                       null=False, primary_key=True)  # Field name made lowercase.
    nroing = models.BigIntegerField(db_column='NroIng', blank=True, null=True)  # Field name made lowercase.
    nroingsap = models.CharField(db_column='NroIngSap', max_length=20, blank=True,
                                 null=True)  # Field name made lowercase.
    item = models.IntegerField(db_column='Item', blank=True, null=True)  # Field name made lowercase.
    codmat = models.CharField(db_column='CodMat', max_length=10, blank=True,
                              null=True)  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=15, decimal_places=2, blank=True,
                                   null=True)  # Field name made lowercase.
    codaf = models.CharField(db_column='CodAF', max_length=20, blank=True,
                             null=True)  # Field name made lowercase.
    codafsap = models.CharField(db_column='CodAFSap', max_length=20, blank=True,
                                null=True)  # Field name made lowercase.
    nroordensap = models.CharField(db_column='NroOrdenSAP', max_length=20, blank=True,
                                   null=True)  # Field name made lowercase.
    condini = models.CharField(db_column='CondIni', max_length=50, blank=True,
                               null=True)  # Field name made lowercase.
    condfin = models.CharField(db_column='Condfin', max_length=50, blank=True,
                               null=True)  # Field name made lowercase.
    codcal = models.CharField(max_length=50, blank=True, null=True)
    nroseal = models.CharField(max_length=100, blank=True, null=True)
    nodo = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'NotIngDet'

class Notsal(ClaseModelo):
    nrosolsal = models.BigAutoField(db_column='NroSolSal', primary_key=True)  # Field name made lowercase.
    fecela = models.DateTimeField(db_column='FecEla', blank=True, null=True)  # Field name made lowercase.
    fecrev = models.DateTimeField(db_column='FecRev', blank=True, null=True)  # Field name made lowercase.
    fecaut = models.DateTimeField(db_column='FecAut', blank=True, null=True)  # Field name made lowercase.
    almacen = models.CharField(db_column='Almacen', max_length=10, blank=True,
                               null=True)  # Field name made lowercase.
    gerencia = models.CharField(db_column='Gerencia', max_length=10, blank=True,
                                null=True)  # Field name made lowercase.
    unidad = models.CharField(db_column='Unidad', max_length=10, blank=True,
                              null=True)  # Field name made lowercase.
    emplaza = models.CharField(db_column='Emplaza', max_length=10, blank=True,
                               null=True)  # Field name made lowercase.
    empresa = models.CharField(db_column='Empresa', max_length=10, blank=True,
                               null=True)  # Field name made lowercase.
    solcodigo = models.CharField(db_column='SolCodigo', max_length=10, blank=True,
                                 null=True)  # Field name made lowercase.
    reccodigo = models.CharField(db_column='RecCodigo', max_length=10, blank=True,
                                 null=True)  # Field name made lowercase.
    codrevision = models.CharField(db_column='CodRevision', max_length=10, blank=True,
                                   null=True)  # Field name made lowercase.
    codautorizador = models.CharField(db_column='CodAutorizador', max_length=10, blank=True,
                                      null=True)  # Field name made lowercase.
    nroordensap = models.CharField(db_column='NroOrdenSap', max_length=20, blank=True,
                                   null=True)  # Field name made lowercase.
    locdes = models.CharField(db_column='LocDes', max_length=10, blank=True,
                              null=True)  # Field name made lowercase.
    estliq = models.CharField(db_column='Estliq', max_length=1, blank=True,
                              null=True)  # Field name made lowercase.
    estnotsal = models.CharField(db_column='EstNotSal', max_length=1, blank=True,
                                 null=True)  # Field name made lowercase.
    nroorden = models.CharField(db_column='NroOrden', max_length=20, blank=True,
                                null=True)  # Field name made lowercase.
    nrosapsal = models.CharField(db_column='NroSapSal', max_length=20, blank=True,
                                 null=True)  # Field name made lowercase.
    nroressal = models.CharField(db_column='NroResSal', max_length=20, blank=True,
                                 null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=350, blank=True,
                                   null=True)  # Field name made lowercase.
    observacion = models.CharField(db_column='Observacion', max_length=350, blank=True,
                                   null=True)  # Field name made lowercase.
    fecrec = models.DateTimeField(db_column='FecRec', blank=True, null=True)  # Field name made lowercase.
    desrec = models.CharField(db_column='DesRec', max_length=350, blank=True,
                              null=True)  # Field name made lowercase.
    codrec = models.CharField(db_column='CodRec', max_length=10, blank=True,
                              null=True)  # Field name made lowercase.
    fecanu = models.DateTimeField(db_column='FecAnu', blank=True, null=True)  # Field name made lowercase.
    desanu = models.CharField(db_column='DesAnu', max_length=350, blank=True,
                              null=True)  # Field name made lowercase.
    codanu = models.CharField(db_column='CodAnu', max_length=10, blank=True,
                              null=True)  # Field name made lowercase.
    fecdes = models.CharField(db_column='FecDes', max_length=10, blank=True,
                              null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NotSal'

class OtActividades(ClaseModelo):
    idactividad = models.AutoField(db_column='IDActividad', primary_key=True)  # Field name made lowercase.
    nivelcontrato = models.IntegerField(db_column='NivelContrato')  # Field name made lowercase.
    detalle = models.CharField(db_column='Detalle', max_length=190, blank=True,
                               null=True)  # Field name made lowercase.
    unidad = models.CharField(db_column='Unidad', max_length=50)  # Field name made lowercase.
    pu = models.DecimalField(db_column='PU', max_digits=8, decimal_places=2)  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado')  # Field name made lowercase.
    codactividad = models.IntegerField(db_column='CodActividad')  # Field name made lowercase.
    codantiguo = models.CharField(db_column='CodAntiguo', max_length=50, blank=True,
                                  null=True)  # Field name made lowercase.
    ca = models.IntegerField(db_column='CA', blank=True, null=True)  # Field name made lowercase.
    cn = models.IntegerField(db_column='CN', blank=True, null=True)  # Field name made lowercase.
    idcontrato = models.IntegerField(db_column='IDContrato', blank=True,
                                     null=True)  # Field name made lowercase.
    idareaadm = models.IntegerField(db_column='IDAreaAdm', blank=True, null=True)  # Field name made lowercase.
    idlocalidad = models.IntegerField(db_column='IDLocalidad', blank=True,
                                      null=True)  # Field name made lowercase.
    ctatipo = models.CharField(db_column='CtaTipo', max_length=1, blank=True,
                               null=True)  # Field name made lowercase.
    ctastipo = models.CharField(db_column='CtaSTipo', max_length=1, blank=True,
                                null=True)  # Field name made lowercase.
    cantidad = models.BigIntegerField(db_column='Cantidad', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_Actividades'

class OtAlmatipot(ClaseModelo):
    idtipot = models.IntegerField(db_column='IDTipoT', primary_key=True)  # Field name made lowercase.
    idunidad = models.IntegerField(db_column='IDUnidad', blank=True, null=True)  # Field name made lowercase.
    codcateg = models.IntegerField(db_column='CodCateg', blank=True, null=True)  # Field name made lowercase.
    descripciontt = models.CharField(db_column='DescripcionTT', max_length=50, blank=True,
                                     null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_AlmaTipoT'

class OtAlmacenes(ClaseModelo):
    codigo = models.IntegerField(db_column='Codigo', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.
    unidad = models.CharField(db_column='Unidad', max_length=50, blank=True,
                              null=True)  # Field name made lowercase.
    codigoa = models.IntegerField(db_column='CodigoA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_Almacenes'

class OtAreaadm(ClaseModelo):
    idareaadm = models.AutoField(db_column='IDAreaAdm', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50)  # Field name made lowercase.
    alias = models.CharField(db_column='Alias', max_length=3, blank=True,
                             null=True)  # Field name made lowercase.
    activo = models.BooleanField(db_column='Activo')  # Field name made lowercase.
    as400 = models.IntegerField(db_column='As400', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_AreaAdm'

class OtAreacontrato(ClaseModelo):
    idarea = models.AutoField(db_column='IDArea', primary_key=True)  # Field name made lowercase.
    idcontrato = models.ForeignKey('OtContratos', models.DO_NOTHING,
                                   db_column='IDContrato')  # Field name made lowercase.
    idareaadm = models.ForeignKey('OtAreaadm', models.DO_NOTHING,
                                  db_column='IDAreaAdm')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_AreaContrato'

class OtAreaderiva(ClaseModelo):
    idareaderiva = models.AutoField(db_column='IDAreaDeriva', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50)  # Field name made lowercase.
    idareaadm = models.IntegerField(db_column='IDAreaAdm', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_AreaDeriva'

class OtAreanivel(ClaseModelo):
    idareaadm = models.ForeignKey('OtAreaadm', models.DO_NOTHING,
                                  db_column='IDAreaAdm', primary_key=True)  # Field name made lowercase.
    idnivel = models.IntegerField(db_column='IDNivel')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_AreaNivel'

class OtCodigoreclamo(ClaseModelo):
    idcodigo = models.BigIntegerField(db_column='IDCodigo', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_CodigoReclamo'

class OtContratistas(ClaseModelo):
    idcontratista = models.AutoField(db_column='IDContratista', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=50, blank=True,
                                 null=True)  # Field name made lowercase.
    ruc = models.CharField(db_column='RUC', max_length=11, blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=10, blank=True,
                                null=True)  # Field name made lowercase.
    contacto = models.CharField(db_column='Contacto', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_Contratistas'

class OtContratos(ClaseModelo):
    idcontrato = models.IntegerField(db_column='IDContrato', primary_key=True)  # Field name made lowercase.
    nrocontrato = models.CharField(db_column='NroContrato', max_length=30)  # Field name made lowercase.
    contratista = models.ForeignKey('OtContratistas', models.DO_NOTHING,
                                    db_column='Contratista')  # Field name made lowercase.
    fechainicio = models.DateTimeField(db_column='FechaInicio')  # Field name made lowercase.
    fechafin = models.DateTimeField(db_column='FechaFin')  # Field name made lowercase.
    montocontrato = models.DecimalField(db_column='MontoContrato', max_digits=18,
                                        decimal_places=2)  # Field name made lowercase.
    estado = models.SmallIntegerField(db_column='Estado')  # Field name made lowercase.
    ccas = models.IntegerField(db_column='CCAs', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_Contratos'

class OtContratosB(ClaseModelo):
    iditem = models.IntegerField(db_column='Iditem', blank=True, null=False, primary_key=True)  # Field name made lowercase.
    contrato = models.CharField(db_column='Contrato', max_length=100, blank=True,
                                null=True)  # Field name made lowercase.
    usuaut = models.IntegerField(db_column='UsuAut', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_Contratos_B'

class OtDatos(ClaseModelo):
    igv = models.DecimalField(db_column='IGV', max_digits=10, decimal_places=2, blank=True,
                              null=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=50, blank=True,
                               null=False, primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_Datos'

class OtDianh(ClaseModelo):
    iddianh = models.AutoField(db_column='IDDiaNH', primary_key=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_DiaNH'

class OtDisalmacenes(ClaseModelo):
    iddisalm = models.BigAutoField(db_column='IDDisAlm', primary_key=True)  # Field name made lowercase.
    idreclamo = models.ForeignKey('OtReclamo', models.DO_NOTHING,
                                  db_column='IDReclamo')  # Field name made lowercase.
    idmovalm = models.ForeignKey('OtMovalmacenes', models.DO_NOTHING,
                                 db_column='IDMovAlm')  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=18, decimal_places=2, blank=True,
                                   null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_DisAlmacenes'

class OtEstadosolicitud(ClaseModelo):
    ideso = models.IntegerField(db_column='IDESO', primary_key=True)  # Field name made lowercase.
    sol_descripcion = models.CharField(db_column='SOL_Descripcion', max_length=20, blank=True,
                                       null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_EstadoSolicitud'

class OtEstados(ClaseModelo):
    idestado = models.SmallIntegerField(db_column='IDEstado', primary_key=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=20)  # Field name made lowercase.
    fv = models.BooleanField(db_column='Fv')  # Field name made lowercase.
    mensaje = models.CharField(db_column='Mensaje', max_length=30)  # Field name made lowercase.
    dias = models.IntegerField(db_column='Dias')  # Field name made lowercase.
    tipo = models.IntegerField(db_column='Tipo')  # Field name made lowercase.
    orden = models.IntegerField(db_column='Orden', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_Estados'

class OtFactibilidadact(ClaseModelo):
    idactfactibilidad = models.AutoField(db_column='IDActFactibilidad',
                                         primary_key=True)  # Field name made lowercase.
    idfactibilidad = models.IntegerField(db_column='IDFactibilidad')  # Field name made lowercase.
    idactividad = models.IntegerField(db_column='IDActividad')  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=10,
                                   decimal_places=2)  # Field name made lowercase.
    idnodo = models.IntegerField(db_column='IDNodo')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    cantidadpre = models.DecimalField(db_column='CantidadPre', max_digits=10,
                                      decimal_places=2)  # Field name made lowercase.
    idnivel = models.IntegerField(db_column='IDNivel', blank=True, null=True)  # Field name made lowercase.
    costo = models.DecimalField(db_column='Costo', max_digits=10,
                                decimal_places=2)  # Field name made lowercase.
    estadoact = models.IntegerField(db_column='EstadoAct', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_FactibilidadAct'

class OtFactibilidades(ClaseModelo):
    idfactibilidad = models.AutoField(db_column='IDFactibilidad',
                                      primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=150)  # Field name made lowercase.
    contrato = models.IntegerField(db_column='Contrato')  # Field name made lowercase.
    areaadm = models.IntegerField(db_column='AreaAdm')  # Field name made lowercase.
    localidad = models.IntegerField(db_column='Localidad')  # Field name made lowercase.
    tipofactibilidad = models.IntegerField(db_column='TipoFactibilidad')  # Field name made lowercase.
    fechaelab = models.DateTimeField(db_column='FechaElab')  # Field name made lowercase.
    perelabora = models.IntegerField(db_column='PerElabora')  # Field name made lowercase.
    fechasup = models.DateTimeField(db_column='FechaSup', blank=True, null=True)  # Field name made lowercase.
    persupervisa = models.IntegerField(db_column='PerSupervisa')  # Field name made lowercase.
    origen = models.IntegerField(db_column='Origen')  # Field name made lowercase.
    docorigen = models.CharField(db_column='DocOrigen', max_length=50, blank=True,
                                 null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=250)  # Field name made lowercase.
    fechaejecten = models.DateTimeField(db_column='FechaEjecTen')  # Field name made lowercase.
    plazoeje = models.SmallIntegerField(db_column='PlazoEje')  # Field name made lowercase.
    cuadrillaeje = models.CharField(db_column='CuadrillaEje', max_length=50, blank=True,
                                    null=True)  # Field name made lowercase.
    estado = models.SmallIntegerField(db_column='Estado')  # Field name made lowercase.
    inicioe = models.DateTimeField(db_column='InicioE', blank=True, null=True)  # Field name made lowercase.
    fine = models.DateTimeField(db_column='FinE', blank=True, null=True)  # Field name made lowercase.
    fechafac = models.DateTimeField(db_column='FechaFac', blank=True, null=True)  # Field name made lowercase.
    perfac = models.IntegerField(db_column='PerFac', blank=True, null=True)  # Field name made lowercase.
    montofac = models.DecimalField(db_column='MontoFac', max_digits=10, decimal_places=2, blank=True,
                                   null=True)  # Field name made lowercase.
    referencia = models.CharField(db_column='Referencia', max_length=150, blank=True,
                                  null=True)  # Field name made lowercase.
    nroanterior = models.CharField(db_column='NroAnterior', max_length=20, blank=True,
                                   null=True)  # Field name made lowercase.
    tranfer = models.CharField(db_column='Tranfer', max_length=10)  # Field name made lowercase.
    nivelfactibilidad = models.IntegerField(db_column='NivelFactibilidad', blank=True,
                                            null=True)  # Field name made lowercase.
    gis = models.BooleanField(db_column='GIS')  # Field name made lowercase.
    fecgis = models.DateTimeField(db_column='FecGis', blank=True, null=True)  # Field name made lowercase.
    pergis = models.IntegerField(db_column='PerGis', blank=True, null=True)  # Field name made lowercase.
    observada = models.BooleanField(db_column='Observada', blank=True, null=True)  # Field name made lowercase.
    grupo = models.SmallIntegerField(db_column='Grupo')  # Field name made lowercase.
    codgrupo = models.CharField(db_column='CodGrupo', max_length=15)  # Field name made lowercase.
    fechaalmacen = models.DateTimeField(db_column='FechaAlmacen', blank=True,
                                        null=True)  # Field name made lowercase.
    penalizada = models.BooleanField(db_column='Penalizada', blank=True,
                                     null=True)  # Field name made lowercase.
    fecaproba = models.DateTimeField(db_column='FecAproba', blank=True, null=True)  # Field name made lowercase.
    peraproba = models.IntegerField(db_column='PerAproba', blank=True, null=True)  # Field name made lowercase.
    gastos = models.DecimalField(db_column='Gastos', max_digits=18, decimal_places=2, blank=True,
                                 null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_Factibilidades'

class OtGrupos(ClaseModelo):
    idgrupo = models.AutoField(db_column='IDGrupo', primary_key=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    percrea = models.IntegerField(db_column='PerCrea')  # Field name made lowercase.
    contrato = models.ForeignKey('OtContratos', models.DO_NOTHING,
                                 db_column='Contrato')  # Field name made lowercase.
    fechafac = models.DateTimeField(db_column='FechaFac', blank=True, null=True)  # Field name made lowercase.
    nrodoc = models.CharField(db_column='NroDoc', max_length=30, blank=True,
                              null=True)  # Field name made lowercase.
    nroots = models.IntegerField(db_column='NroOTs')  # Field name made lowercase.
    monto = models.DecimalField(db_column='Monto', max_digits=10,
                                decimal_places=2)  # Field name made lowercase.
    igv = models.DecimalField(db_column='IGV', max_digits=10, decimal_places=2)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=12,
                                decimal_places=2)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=100, blank=True,
                                     null=True)  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado')  # Field name made lowercase.
    ruc = models.CharField(db_column='RUC', max_length=11, blank=True, null=True)  # Field name made lowercase.
    tipoots = models.ForeignKey('OtNivel', models.DO_NOTHING, db_column='TipoOTs')  # Field name made lowercase.
    localidad = models.ForeignKey('OtLocalidad', models.DO_NOTHING,
                                  db_column='Localidad')  # Field name made lowercase.
    permodi = models.IntegerField(db_column='PerModi', blank=True, null=True)  # Field name made lowercase.
    montoamor = models.DecimalField(db_column='MontoAmor', max_digits=10, decimal_places=2, blank=True,
                                    null=True)  # Field name made lowercase.
    montosub = models.DecimalField(db_column='MontoSub', max_digits=10, decimal_places=2, blank=True,
                                   null=True)  # Field name made lowercase.
    igva = models.DecimalField(db_column='IGVA', max_digits=10, decimal_places=2, blank=True,
                               null=True)  # Field name made lowercase.
    totala = models.DecimalField(db_column='TotalA', max_digits=12, decimal_places=2, blank=True,
                                 null=True)  # Field name made lowercase.
    igvt = models.DecimalField(db_column='IGVT', max_digits=10, decimal_places=2, blank=True,
                               null=True)  # Field name made lowercase.
    totalt = models.DecimalField(db_column='TotalT', max_digits=12, decimal_places=2, blank=True,
                                 null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_Grupos'

class OtInformes(ClaseModelo):
    idinforme = models.AutoField(db_column='IDInforme', primary_key=True)  # Field name made lowercase.
    idot = models.ForeignKey('OtOts', models.DO_NOTHING, db_column='IDOT')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    percrea = models.IntegerField(db_column='PerCrea')  # Field name made lowercase.
    texto = models.TextField(db_column='Texto', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_Informes'

class OtLiquidaciones(ClaseModelo):
    idliq = models.AutoField(db_column='IDLiq', primary_key=True)  # Field name made lowercase.
    idot = models.IntegerField(db_column='IDOT')  # Field name made lowercase.
    idnodo = models.IntegerField(db_column='IDNodo')  # Field name made lowercase.
    codigo = models.IntegerField(db_column='Codigo')  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=8,
                                   decimal_places=2)  # Field name made lowercase.
    documento = models.IntegerField(db_column='Documento', blank=True, null=True)  # Field name made lowercase.
    marca = models.CharField(db_column='Marca', max_length=50, blank=True,
                             null=True)  # Field name made lowercase.
    modelo = models.CharField(db_column='Modelo', max_length=50, blank=True,
                              null=True)  # Field name made lowercase.
    serie = models.CharField(db_column='Serie', max_length=50, blank=True,
                             null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_Liquidaciones'

class OtListamateriales(ClaseModelo):
    idslmat = models.AutoField(db_column='IDSLMAT', primary_key=True)  # Field name made lowercase.
    idot = models.IntegerField(db_column='IDOT')  # Field name made lowercase.
    codigomat = models.IntegerField(db_column='CodigoMat')  # Field name made lowercase.
    cantidad = models.FloatField(db_column='Cantidad')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    estadomat = models.BooleanField(db_column='EstadoMat')  # Field name made lowercase.
    idgrsal = models.IntegerField(db_column='IDGRSAL', blank=True, null=True)  # Field name made lowercase.
    nodoid = models.IntegerField(db_column='NodoID', blank=True, null=True)  # Field name made lowercase.
    utilizado = models.FloatField(db_column='Utilizado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_ListaMateriales'

class OtLocalidad(ClaseModelo):
    idlocalidad = models.AutoField(db_column='IDLocalidad', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50)  # Field name made lowercase.
    cod2 = models.CharField(db_column='Cod2', max_length=20, blank=True,
                            null=True)  # Field name made lowercase.
    las400 = models.IntegerField(db_column='LAS400', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_Localidad'

class OtLogs(ClaseModelo):
    idlog = models.AutoField(db_column='IDLOg', primary_key=True)  # Field name made lowercase.
    otid = models.ForeignKey('OtOts', models.DO_NOTHING, db_column='OTid')  # Field name made lowercase.
    estado = models.ForeignKey('OtEstados', models.DO_NOTHING, db_column='Estado')  # Field name made lowercase.
    persona = models.IntegerField(db_column='Persona')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    extras = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'OT_Logs'

class OtLogsf(ClaseModelo):
    idlogf = models.AutoField(db_column='IDLogF', primary_key=True)  # Field name made lowercase.
    idfactibilidad = models.IntegerField(db_column='IDFactibilidad')  # Field name made lowercase.
    estado = models.SmallIntegerField(db_column='Estado')  # Field name made lowercase.
    persona = models.IntegerField(db_column='Persona')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_LogsF'

class OtLogsm(ClaseModelo):
    codigoalm = models.IntegerField(db_column='CodigoAlm', primary_key=True)  # Field name made lowercase.
    descanterior = models.CharField(db_column='DescAnterior', max_length=50)  # Field name made lowercase.
    descnueva = models.CharField(db_column='DescNueva', max_length=50)  # Field name made lowercase.
    fechacambio = models.DateTimeField(db_column='FechaCambio')  # Field name made lowercase.
    idot = models.IntegerField(db_column='IDOT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_LogsM'

class OtLogsp(ClaseModelo):
    idlogp = models.AutoField(db_column='IDLogP', primary_key=True)  # Field name made lowercase.
    idpresupuesto = models.IntegerField(db_column='IDPresupuesto', blank=True,
                                        null=True)  # Field name made lowercase.
    estado = models.SmallIntegerField(db_column='Estado')  # Field name made lowercase.
    persona = models.IntegerField(db_column='Persona')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_LogsP'

class OtMovalmacenes(ClaseModelo):
    idot = models.IntegerField(db_column='IDOT')  # Field name made lowercase.
    codigo = models.IntegerField(db_column='Codigo')  # Field name made lowercase.
    salida = models.DecimalField(db_column='Salida', max_digits=8,
                                 decimal_places=2)  # Field name made lowercase.
    ingreso = models.DecimalField(db_column='Ingreso', max_digits=8,
                                  decimal_places=2)  # Field name made lowercase.
    docsalida = models.DecimalField(db_column='DocSalida', max_digits=18,
                                    decimal_places=0)  # Field name made lowercase.
    docingreso = models.DecimalField(db_column='DocIngreso', max_digits=18,
                                     decimal_places=0)  # Field name made lowercase.
    tipo = models.SmallIntegerField(db_column='Tipo')  # Field name made lowercase.
    fechasalida = models.CharField(db_column='FechaSalida', max_length=50, blank=True,
                                   null=True)  # Field name made lowercase.
    fechaingreso = models.CharField(db_column='FechaIngreso', max_length=50, blank=True,
                                    null=True)  # Field name made lowercase.
    nrosolicitud = models.IntegerField(db_column='NroSolicitud')  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    liquidado = models.DecimalField(db_column='Liquidado', max_digits=8,
                                    decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_MovAlmacenes'

class OtMovalmacenes2(ClaseModelo):
    idot = models.IntegerField(db_column='IDOT')  # Field name made lowercase.
    codigo = models.IntegerField(db_column='Codigo')  # Field name made lowercase.
    salida = models.DecimalField(db_column='Salida', max_digits=8,
                                 decimal_places=2)  # Field name made lowercase.
    ingreso = models.DecimalField(db_column='Ingreso', max_digits=8,
                                  decimal_places=2)  # Field name made lowercase.
    docsalida = models.IntegerField(db_column='DocSalida')  # Field name made lowercase.
    docingreso = models.IntegerField(db_column='DocIngreso')  # Field name made lowercase.
    tipo = models.SmallIntegerField(db_column='Tipo')  # Field name made lowercase.
    fechasalida = models.CharField(db_column='FechaSalida', max_length=50, blank=True,
                                   null=True)  # Field name made lowercase.
    fechaingreso = models.CharField(db_column='FechaIngreso', max_length=50, blank=True,
                                    null=True)  # Field name made lowercase.
    nrosolicitud = models.IntegerField(db_column='NroSolicitud')  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    liquidado = models.DecimalField(db_column='Liquidado', max_digits=8,
                                    decimal_places=2)  # Field name made lowercase.
    factura = models.CharField(db_column='Factura', max_length=20, blank=True,
                               null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_MovAlmacenes2'

class OtMovalmacenes7(ClaseModelo):
    idot = models.IntegerField(db_column='IDOT', blank=True, null=False)  # Field name made lowercase.
    codigo = models.IntegerField(db_column='Codigo', blank=True, null=True)  # Field name made lowercase.
    salida = models.DecimalField(db_column='Salida', max_digits=8, decimal_places=2, blank=True,
                                 null=True)  # Field name made lowercase.
    ingreso = models.DecimalField(db_column='Ingreso', max_digits=8, decimal_places=2, blank=True,
                                  null=True)  # Field name made lowercase.
    docsalida = models.DecimalField(db_column='DocSalida', max_digits=18, decimal_places=0, blank=True,
                                    null=True)  # Field name made lowercase.
    docingreso = models.DecimalField(db_column='DocIngreso', max_digits=18, decimal_places=0, blank=True,
                                     null=True)  # Field name made lowercase.
    tipo = models.SmallIntegerField(db_column='Tipo', blank=True, null=True)  # Field name made lowercase.
    fechasalida = models.CharField(db_column='FechaSalida', max_length=50, blank=True,
                                   null=True)  # Field name made lowercase.
    fechaingreso = models.CharField(db_column='FechaIngreso', max_length=50, blank=True,
                                    null=True)  # Field name made lowercase.
    nrosolicitud = models.DecimalField(db_column='NroSolicitud', max_digits=18, decimal_places=0, blank=True,
                                       null=True)  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    liquidado = models.DecimalField(db_column='Liquidado', max_digits=8, decimal_places=2, blank=True,
                                    null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_MovAlmacenes7'

class OtNiif(ClaseModelo):
    idot = models.IntegerField(db_column='IDOT', blank=True, null=False, primary_key=True)  # Field name made lowercase.
    idactividad = models.CharField(db_column='IdActividad', max_length=3, blank=True,
                                   null=True)  # Field name made lowercase.
    idcuenta = models.CharField(db_column='IdCuenta', max_length=3, blank=True,
                                null=True)  # Field name made lowercase.
    idtipo = models.CharField(db_column='IdTipo', max_length=3, blank=True,
                              null=True)  # Field name made lowercase.
    idubicacion = models.CharField(db_column='IdUbicacion', max_length=5, blank=True,
                                   null=True)  # Field name made lowercase.
    idcomponente = models.CharField(db_column='IdComponente', max_length=4, blank=True,
                                    null=True)  # Field name made lowercase.
    idelemento = models.CharField(db_column='IdElemento', max_length=4, blank=True,
                                  null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_NIIF'

class OtNivel(ClaseModelo):
    idnivel = models.AutoField(db_column='IDNivel', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.
    publica = models.BooleanField(db_column='Publica')  # Field name made lowercase.
    idcontrato = models.IntegerField(db_column='IDCOntrato')  # Field name made lowercase.
    alias = models.CharField(db_column='Alias', max_length=3)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_Nivel'

class OtNivelcontrato(ClaseModelo):
    idcnivel = models.AutoField(db_column='IDCNivel', primary_key=True)  # Field name made lowercase.
    nivel = models.ForeignKey('OtNivel', models.DO_NOTHING, db_column='Nivel')  # Field name made lowercase.
    contrato = models.ForeignKey('OtContratos', models.DO_NOTHING,
                                 db_column='Contrato')  # Field name made lowercase.
    responsable = models.CharField(db_column='Responsable', max_length=50, blank=True,
                                   null=True)  # Field name made lowercase.
    localidad = models.ForeignKey('OtLocalidad', models.DO_NOTHING, db_column='Localidad', blank=True,
                                  null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_NivelContrato'

class OtNodoh(ClaseModelo):
    item = models.IntegerField(blank=True, null=False, primary_key=True)
    codnodop = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True, null=True)
    fecreg = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'OT_NodoH'

class OtNodop(ClaseModelo):
    item = models.IntegerField(db_column='Item', blank=True, null=False, primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True, null=True)
    fecreg = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'OT_NodoP'

class OtNodoreferencia(ClaseModelo):
    idnodoreferencia = models.AutoField(db_column='IDNodoReferencia',
                                        primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_NodoReferencia'

class OtNodos(ClaseModelo):
    idnodo = models.AutoField(db_column='IDNodo', primary_key=True)  # Field name made lowercase.
    idot = models.ForeignKey('OtOts', models.DO_NOTHING, db_column='IDOT', blank=True,
                             null=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=20)  # Field name made lowercase.
    tiponodo = models.ForeignKey('OtTiponodo', models.DO_NOTHING,
                                 db_column='TipoNodo')  # Field name made lowercase.
    referencia = models.CharField(db_column='Referencia', max_length=200, blank=True,
                                  null=True)  # Field name made lowercase.
    observacion = models.CharField(db_column='Observacion', max_length=200, blank=True,
                                   null=True)  # Field name made lowercase.
    usuariomod = models.IntegerField(db_column='UsuarioMod', blank=True,
                                     null=True)  # Field name made lowercase.
    ant = models.IntegerField(blank=True, null=True)
    idpresupuesto = models.IntegerField(db_column='IDPresupuesto', blank=True,
                                        null=True)  # Field name made lowercase.
    idfactibilidad = models.IntegerField(db_column='IDFactibilidad', blank=True,
                                         null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_Nodos'

class OtOtact(ClaseModelo):
    idactot = models.AutoField(db_column='IDActOT', primary_key=True)  # Field name made lowercase.
    idot = models.ForeignKey('OtOts', models.DO_NOTHING, db_column='IDOT')  # Field name made lowercase.
    idactividad = models.IntegerField(db_column='IDActividad')  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=10,
                                   decimal_places=2)  # Field name made lowercase.
    idnodo = models.ForeignKey('OtNodos', models.DO_NOTHING, db_column='IDNodo')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    cantidadpre = models.DecimalField(db_column='CantidadPre', max_digits=10,
                                      decimal_places=2)  # Field name made lowercase.
    idnivel = models.IntegerField(db_column='IDNivel', blank=True, null=True)  # Field name made lowercase.
    costo = models.DecimalField(db_column='Costo', max_digits=10,
                                decimal_places=2)  # Field name made lowercase.
    estadoact = models.IntegerField(db_column='EstadoAct', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_OTAct'

class OtOtpen(ClaseModelo):
    idpenot = models.AutoField(db_column='IDPenOT', primary_key=True)  # Field name made lowercase.
    idot = models.IntegerField(db_column='IDOT')  # Field name made lowercase.
    idpenalidad = models.IntegerField(db_column='IDPenalidad')  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=18,
                                   decimal_places=4)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    idtipopenalidad = models.IntegerField(db_column='IDTipoPenalidad', blank=True,
                                          null=True)  # Field name made lowercase.
    costo = models.DecimalField(db_column='Costo', max_digits=18,
                                decimal_places=2)  # Field name made lowercase.
    estadopen = models.IntegerField(db_column='EstadoPen', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_OTPen'

class OtOtrec(ClaseModelo):
    id_otreclamo = models.BigAutoField(db_column='ID_OTReclamo', primary_key=True)  # Field name made lowercase.
    idot = models.ForeignKey('OtOts', models.DO_NOTHING, db_column='IDOT')  # Field name made lowercase.
    idreclamo = models.ForeignKey('OtReclamo', models.DO_NOTHING,
                                  db_column='IDReclamo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_OTRec'

class OtOts(ClaseModelo):
    idot = models.AutoField(db_column='IDOT', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=150)  # Field name made lowercase.
    contrato = models.ForeignKey('OtContratos', models.DO_NOTHING,
                                 db_column='Contrato')  # Field name made lowercase.
    areaadm = models.IntegerField(db_column='AreaAdm')  # Field name made lowercase.
    localidad = models.ForeignKey('OtLocalidad', models.DO_NOTHING,
                                  db_column='Localidad')  # Field name made lowercase.
    tipoot = models.IntegerField(db_column='TipoOt')  # Field name made lowercase.
    fechaelab = models.DateTimeField(db_column='FechaElab')  # Field name made lowercase.
    perelabora = models.IntegerField(db_column='PerElabora')  # Field name made lowercase.
    fechasup = models.DateTimeField(db_column='FechaSup', blank=True, null=True)  # Field name made lowercase.
    persupervisa = models.IntegerField(db_column='PerSupervisa')  # Field name made lowercase.
    origen = models.ForeignKey('OtOrigen', models.DO_NOTHING, db_column='Origen')  # Field name made lowercase.
    docorigen = models.CharField(db_column='DocOrigen', max_length=50, blank=True,
                                 null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=250, blank=True,
                                     null=True)  # Field name made lowercase.
    fechaejecten = models.DateTimeField(db_column='FechaEjecTen')  # Field name made lowercase.
    plazoeje = models.SmallIntegerField(db_column='PlazoEje')  # Field name made lowercase.
    cuadrillaeje = models.CharField(db_column='CuadrillaEje', max_length=50, blank=True,
                                    null=True)  # Field name made lowercase.
    estado = models.ForeignKey('OtEstados', models.DO_NOTHING, db_column='Estado')  # Field name made lowercase.
    inicioe = models.DateTimeField(db_column='InicioE', blank=True, null=True)  # Field name made lowercase.
    fine = models.DateTimeField(db_column='FinE', blank=True, null=True)  # Field name made lowercase.
    fechaliq = models.DateTimeField(db_column='FechaLiq', blank=True, null=True)  # Field name made lowercase.
    perliq = models.IntegerField(db_column='PerLiq')  # Field name made lowercase.
    fechafac = models.DateTimeField(db_column='FechaFac', blank=True, null=True)  # Field name made lowercase.
    perfac = models.IntegerField(db_column='PerFac')  # Field name made lowercase.
    grupofac = models.IntegerField(db_column='GrupoFac', blank=True, null=True)  # Field name made lowercase.
    montofac = models.DecimalField(db_column='MontoFac', max_digits=10, decimal_places=2, blank=True,
                                   null=True)  # Field name made lowercase.
    referencia = models.CharField(db_column='Referencia', max_length=150, blank=True,
                                  null=True)  # Field name made lowercase.
    nroanterior = models.CharField(db_column='NroAnterior', max_length=20, blank=True,
                                   null=True)  # Field name made lowercase.
    tranfer = models.BooleanField(db_column='Tranfer')  # Field name made lowercase.
    nivelot = models.IntegerField(db_column='NivelOT', blank=True, null=True)  # Field name made lowercase.
    gis = models.BooleanField(db_column='GIS')  # Field name made lowercase.
    fecgis = models.DateTimeField(db_column='FecGis', blank=True, null=True)  # Field name made lowercase.
    pergis = models.IntegerField(db_column='PerGis')  # Field name made lowercase.
    fecharec = models.DateTimeField(db_column='FechaRec', blank=True, null=True)  # Field name made lowercase.
    perrec = models.IntegerField(db_column='PerRec', blank=True, null=True)  # Field name made lowercase.
    recepcionada = models.BooleanField(db_column='Recepcionada', blank=True,
                                       null=True)  # Field name made lowercase.
    observada = models.BooleanField(db_column='Observada')  # Field name made lowercase.
    grupo = models.SmallIntegerField(db_column='Grupo', blank=True, null=True)  # Field name made lowercase.
    codgrupo = models.CharField(db_column='CodGrupo', max_length=15, blank=True,
                                null=True)  # Field name made lowercase.
    fechaalmacen = models.DateTimeField(db_column='FechaAlmacen', blank=True,
                                        null=True)  # Field name made lowercase.
    penalizada = models.BooleanField(db_column='Penalizada', blank=True,
                                     null=True)  # Field name made lowercase.
    fechareccontra = models.DateTimeField(db_column='FechaRecContra', blank=True,
                                          null=True)  # Field name made lowercase.
    perreccontra = models.IntegerField(db_column='PerRecContra', blank=True,
                                       null=True)  # Field name made lowercase.
    fecaproba = models.DateTimeField(db_column='FecAproba', blank=True, null=True)  # Field name made lowercase.
    peraproba = models.IntegerField(db_column='PerAproba', blank=True, null=True)  # Field name made lowercase.
    materiales = models.BooleanField(db_column='Materiales', blank=True,
                                     null=True)  # Field name made lowercase.
    inicioer = models.DateTimeField(db_column='InicioER', blank=True, null=True)  # Field name made lowercase.
    inicioem = models.DateTimeField(db_column='InicioEM', blank=True, null=True)  # Field name made lowercase.
    plazoejeh = models.SmallIntegerField(db_column='PlazoEjeH', blank=True,
                                         null=True)  # Field name made lowercase.
    bloqueado = models.BooleanField(db_column='Bloqueado', blank=True, null=True)  # Field name made lowercase.
    enmendar = models.BooleanField(db_column='Enmendar', blank=True, null=True)  # Field name made lowercase.
    aurt = models.CharField(db_column='AURT', max_length=4, blank=True, null=True)  # Field name made lowercase.
    prctr = models.CharField(db_column='PRCTR', max_length=10, blank=True,
                             null=True)  # Field name made lowercase.
    kostv = models.CharField(db_column='KOSTV', max_length=10, blank=True,
                             null=True)  # Field name made lowercase.
    veraa_user = models.CharField(db_column='VERAA_USER', max_length=12, blank=True,
                                  null=True)  # Field name made lowercase.
    akstl = models.CharField(db_column='AKSTL', max_length=10, blank=True,
                             null=True)  # Field name made lowercase.
    nrosap = models.CharField(db_column='NROSAP', max_length=12, blank=True,
                              null=True)  # Field name made lowercase.
    tipocuenta = models.IntegerField(db_column='TipoCuenta', blank=True,
                                     null=True)  # Field name made lowercase.
    gerencia = models.CharField(db_column='GERENCIA', max_length=1, blank=True,
                                null=True)  # Field name made lowercase.
    otnueva = models.CharField(db_column='OTNUEVA', max_length=12, blank=True,
                               null=True)  # Field name made lowercase.
    otblo = models.CharField(db_column='OTBLO', max_length=1, blank=True,
                             null=True)  # Field name made lowercase.
    otfr1 = models.CharField(db_column='OTFR1', max_length=1, blank=True,
                             null=True)  # Field name made lowercase.
    otfr2 = models.CharField(db_column='OTFR2', max_length=1, blank=True,
                             null=True)  # Field name made lowercase.
    flagplazo = models.CharField(db_column='FlagPlazo', max_length=1, blank=True,
                                 null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_OTs'

class OtObservaciones(ClaseModelo):
    idobs = models.AutoField(db_column='idObs', primary_key=True)  # Field name made lowercase.
    idot = models.IntegerField(db_column='IDOT')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    perobserva = models.IntegerField(db_column='PerObserva')  # Field name made lowercase.
    motivo = models.TextField(db_column='Motivo', blank=True, null=True)  # Field name made lowercase.
    fechades = models.DateTimeField(db_column='FechaDes', blank=True, null=True)  # Field name made lowercase.
    descargo = models.TextField(db_column='Descargo', blank=True, null=True)  # Field name made lowercase.
    activo = models.BooleanField(db_column='Activo', blank=True, null=True)  # Field name made lowercase.
    perdescarga = models.IntegerField(db_column='PerDescarga', blank=True,
                                      null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_Observaciones'

class OtOrigen(ClaseModelo):
    idorigen = models.AutoField(db_column='IDOrigen', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=40)  # Field name made lowercase.
    activo = models.BooleanField(db_column='Activo')  # Field name made lowercase.
    gerencia = models.IntegerField(db_column='Gerencia', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_Origen'

class OtPedmaterial(ClaseModelo):
    idcm = models.AutoField(db_column='IDCM', primary_key=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    otid = models.IntegerField(db_column='OTID')  # Field name made lowercase.
    tiposolicitud = models.CharField(db_column='TipoSolicitud', max_length=20)  # Field name made lowercase.
    motivo = models.CharField(db_column='Motivo', max_length=10)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=200, blank=True,
                                   null=True)  # Field name made lowercase.
    noid = models.CharField(db_column='NoID', max_length=20, blank=True,
                            null=True)  # Field name made lowercase.
    nodesc = models.CharField(db_column='NODesc', max_length=50, blank=True,
                              null=True)  # Field name made lowercase.
    estadosol = models.IntegerField(db_column='EstadoSol')  # Field name made lowercase.
    nrosolicitud = models.CharField(db_column='NroSolicitud', max_length=20, blank=True,
                                    null=True)  # Field name made lowercase.
    fechavb1 = models.DateTimeField(db_column='FechaVB1', blank=True, null=True)  # Field name made lowercase.
    fechavb2 = models.DateTimeField(db_column='FechaVB2', blank=True, null=True)  # Field name made lowercase.
    tipodoc = models.IntegerField(db_column='TipoDoc')  # Field name made lowercase.
    observacionessol = models.CharField(db_column='ObservacionesSol', max_length=500, blank=True,
                                        null=True)  # Field name made lowercase.
    codrecepciona = models.CharField(db_column='CodRecepciona', max_length=8, blank=True,
                                     null=True)  # Field name made lowercase.
    tipot = models.IntegerField(db_column='TipoT', blank=True, null=True)  # Field name made lowercase.
    codcta = models.IntegerField(db_column='CodCta', blank=True, null=True)  # Field name made lowercase.
    observacionesdev = models.CharField(db_column='ObservacionesDev', max_length=500, blank=True,
                                        null=True)  # Field name made lowercase.
    coddevuelve = models.CharField(db_column='CodDevuelve', max_length=8, blank=True,
                                   null=True)  # Field name made lowercase.
    motivodev = models.CharField(db_column='MotivoDev', max_length=200, blank=True,
                                 null=True)  # Field name made lowercase.
    estadodev = models.IntegerField(db_column='EstadoDev', blank=True, null=True)  # Field name made lowercase.
    fechadev = models.DateTimeField(db_column='FechaDev', blank=True, null=True)  # Field name made lowercase.
    nrosolicituddev = models.CharField(db_column='NroSolicitudDev', max_length=20, blank=True,
                                       null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_PedMaterial'

class OtPenalidad(ClaseModelo):
    idpenalidad = models.AutoField(db_column='IDPenalidad', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=8, blank=True,
                              null=True)  # Field name made lowercase.
    idtipopenalidad = models.IntegerField(db_column='IDTipoPenalidad')  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=500, blank=True,
                              null=True)  # Field name made lowercase.
    unidad = models.CharField(db_column='Unidad', max_length=50)  # Field name made lowercase.
    pu = models.DecimalField(db_column='PU', max_digits=18, decimal_places=2)  # Field name made lowercase.
    adicional = models.CharField(db_column='Adicional', max_length=500, blank=True,
                                 null=True)  # Field name made lowercase.
    idcontrato = models.IntegerField(db_column='IDContrato')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_Penalidad'

class OtPlazo(ClaseModelo):
    iditem = models.IntegerField(db_column='IdItem', blank=True, null=False, primary_key=True)  # Field name made lowercase.
    plazo = models.IntegerField(db_column='Plazo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_Plazo'

class OtPrecios(ClaseModelo):
    idprecio = models.BigAutoField(db_column='IDPrecio', primary_key=True)  # Field name made lowercase.
    codigoalmacen = models.IntegerField(db_column='CodigoAlmacen')  # Field name made lowercase.
    monto = models.DecimalField(db_column='Monto', max_digits=18,
                                decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_Precios'

class OtPresupuestoact(ClaseModelo):
    idactpresupuesto = models.AutoField(db_column='IDActPresupuesto',
                                        primary_key=True)  # Field name made lowercase.
    idpresupuesto = models.IntegerField(db_column='IDPresupuesto')  # Field name made lowercase.
    idactividad = models.IntegerField(db_column='IDActividad')  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=10,
                                   decimal_places=2)  # Field name made lowercase.
    idnodo = models.IntegerField(db_column='IDNodo')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    cantidadpre = models.DecimalField(db_column='CantidadPre', max_digits=10,
                                      decimal_places=2)  # Field name made lowercase.
    idnivel = models.IntegerField(db_column='IDNivel', blank=True, null=True)  # Field name made lowercase.
    costo = models.DecimalField(db_column='Costo', max_digits=10,
                                decimal_places=2)  # Field name made lowercase.
    estadoact = models.IntegerField(db_column='EstadoAct', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_PresupuestoAct'

class OtPresupuestos(ClaseModelo):
    idpresupuesto = models.AutoField(db_column='IDPresupuesto', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=150)  # Field name made lowercase.
    contrato = models.IntegerField(db_column='Contrato')  # Field name made lowercase.
    areaadm = models.IntegerField(db_column='AreaAdm')  # Field name made lowercase.
    localidad = models.IntegerField(db_column='Localidad')  # Field name made lowercase.
    tipopresupuesto = models.IntegerField(db_column='TipoPresupuesto')  # Field name made lowercase.
    fechaelab = models.DateTimeField(db_column='FechaElab')  # Field name made lowercase.
    perelabora = models.IntegerField(db_column='PerElabora')  # Field name made lowercase.
    fechasup = models.DateTimeField(db_column='FechaSup', blank=True, null=True)  # Field name made lowercase.
    persupervisa = models.IntegerField(db_column='PerSupervisa')  # Field name made lowercase.
    origen = models.IntegerField(db_column='Origen')  # Field name made lowercase.
    docorigen = models.CharField(db_column='DocOrigen', max_length=50, blank=True,
                                 null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=250)  # Field name made lowercase.
    fechaejecten = models.DateTimeField(db_column='FechaEjecTen')  # Field name made lowercase.
    plazoeje = models.SmallIntegerField(db_column='PlazoEje')  # Field name made lowercase.
    cuadrillaeje = models.CharField(db_column='CuadrillaEje', max_length=50, blank=True,
                                    null=True)  # Field name made lowercase.
    estado = models.SmallIntegerField(db_column='Estado')  # Field name made lowercase.
    inicioe = models.DateTimeField(db_column='InicioE', blank=True, null=True)  # Field name made lowercase.
    fine = models.DateTimeField(db_column='FinE', blank=True, null=True)  # Field name made lowercase.
    fechafac = models.DateTimeField(db_column='FechaFac', blank=True, null=True)  # Field name made lowercase.
    perfac = models.CharField(db_column='PerFac', max_length=10, blank=True,
                              null=True)  # Field name made lowercase.
    montofac = models.DecimalField(db_column='MontoFac', max_digits=18, decimal_places=2, blank=True,
                                   null=True)  # Field name made lowercase.
    referencia = models.CharField(db_column='Referencia', max_length=150, blank=True,
                                  null=True)  # Field name made lowercase.
    nroanterior = models.CharField(db_column='NroAnterior', max_length=20, blank=True,
                                   null=True)  # Field name made lowercase.
    tranfer = models.BooleanField(db_column='Tranfer')  # Field name made lowercase.
    nivelpresupuesto = models.IntegerField(db_column='NivelPresupuesto', blank=True,
                                           null=True)  # Field name made lowercase.
    gis = models.BooleanField(db_column='GIS', blank=True, null=True)  # Field name made lowercase.
    fecgis = models.DateTimeField(db_column='FecGIS', blank=True, null=True)  # Field name made lowercase.
    pergis = models.IntegerField(db_column='PerGis', blank=True, null=True)  # Field name made lowercase.
    observada = models.IntegerField(db_column='Observada', blank=True, null=True)  # Field name made lowercase.
    grupo = models.SmallIntegerField(db_column='Grupo')  # Field name made lowercase.
    codgrupo = models.CharField(db_column='CodGrupo', max_length=15)  # Field name made lowercase.
    fechaalmacen = models.DateTimeField(db_column='FechaAlmacen', blank=True,
                                        null=True)  # Field name made lowercase.
    penalizada = models.BooleanField(db_column='Penalizada', blank=True,
                                     null=True)  # Field name made lowercase.
    fecaproba = models.DateTimeField(db_column='FecAproba', blank=True, null=True)  # Field name made lowercase.
    peraproba = models.IntegerField(db_column='PerAproba', blank=True, null=True)  # Field name made lowercase.
    gastos = models.DecimalField(db_column='Gastos', max_digits=18, decimal_places=2, blank=True,
                                 null=True)  # Field name made lowercase.
    norma = models.DecimalField(db_column='Norma', max_digits=18, decimal_places=2, blank=True,
                                null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_Presupuestos'

class OtReclamo(ClaseModelo):
    idreclamo = models.IntegerField(db_column='IDReclamo', primary_key=True)  # Field name made lowercase.
    fecharegistro = models.DateTimeField(db_column='FechaRegistro', blank=True,
                                         null=True)  # Field name made lowercase.
    nombresolicitante = models.CharField(db_column='NombreSolicitante', max_length=200, blank=True,
                                         null=True)  # Field name made lowercase.
    direccionsolicitante = models.CharField(db_column='DireccionSolicitante', max_length=200, blank=True,
                                            null=True)  # Field name made lowercase.
    responsable = models.CharField(db_column='Responsable', max_length=50, blank=True,
                                   null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100, blank=True,
                                   null=True)  # Field name made lowercase.
    departamento = models.CharField(db_column='Departamento', max_length=100, blank=True,
                                    null=True)  # Field name made lowercase.
    provincia = models.CharField(db_column='Provincia', max_length=100, blank=True,
                                 null=True)  # Field name made lowercase.
    distrito = models.CharField(db_column='Distrito', max_length=100, blank=True,
                                null=True)  # Field name made lowercase.
    codigosuministro = models.IntegerField(db_column='CodigoSuministro', blank=True,
                                           null=True)  # Field name made lowercase.
    nombreamt = models.CharField(db_column='NombreAMT', max_length=100, blank=True,
                                 null=True)  # Field name made lowercase.
    nombresed = models.CharField(db_column='NombreSED', max_length=50, blank=True,
                                 null=True)  # Field name made lowercase.
    ta = models.DateTimeField(db_column='TA', blank=True, null=True)  # Field name made lowercase.
    tb = models.DateTimeField(db_column='TB', blank=True, null=True)  # Field name made lowercase.
    tc = models.DateTimeField(db_column='TC', blank=True, null=True)  # Field name made lowercase.
    observacion = models.CharField(db_column='Observacion', max_length=200, blank=True,
                                   null=True)  # Field name made lowercase.
    idareaderiva = models.IntegerField(db_column='IDAreaDeriva', blank=True,
                                       null=True)  # Field name made lowercase.
    codigo = models.IntegerField(db_column='Codigo', blank=True, null=True)  # Field name made lowercase.
    servicio = models.BooleanField(db_column='Servicio', blank=True, null=True)  # Field name made lowercase.
    solucion = models.IntegerField(db_column='Solucion', blank=True, null=True)  # Field name made lowercase.
    sellos = models.BooleanField(db_column='Sellos', blank=True, null=True)  # Field name made lowercase.
    caja = models.BooleanField(db_column='Caja', blank=True, null=True)  # Field name made lowercase.
    medidor = models.BooleanField(db_column='Medidor', blank=True, null=True)  # Field name made lowercase.
    acometida = models.DecimalField(db_column='Acometida', max_digits=18, decimal_places=2, blank=True,
                                    null=True)  # Field name made lowercase.
    termico = models.DecimalField(db_column='Termico', max_digits=18, decimal_places=2, blank=True,
                                  null=True)  # Field name made lowercase.
    regleta = models.DecimalField(db_column='Regleta', max_digits=18, decimal_places=2, blank=True,
                                  null=True)  # Field name made lowercase.
    baston = models.DecimalField(db_column='Baston', max_digits=18, decimal_places=2, blank=True,
                                 null=True)  # Field name made lowercase.
    reubicacion = models.BooleanField(db_column='Reubicacion', blank=True,
                                      null=True)  # Field name made lowercase.
    atendido = models.BooleanField(db_column='Atendido', blank=True, null=True)  # Field name made lowercase.
    descripcionsolucion = models.CharField(db_column='DescripcionSolucion', max_length=200, blank=True,
                                           null=True)  # Field name made lowercase.
    fechasolucion = models.DateTimeField(db_column='FechaSolucion', blank=True,
                                         null=True)  # Field name made lowercase.
    resuelto = models.BooleanField(db_column='Resuelto', blank=True, null=True)  # Field name made lowercase.
    idperresuelto = models.IntegerField(db_column='IDPerResuelto', blank=True,
                                        null=True)  # Field name made lowercase.
    modoresuelto = models.CharField(db_column='ModoResuelto', max_length=200, blank=True,
                                    null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_Reclamo'

class OtRequerimientos(ClaseModelo):
    idrequerimiento = models.BigAutoField(db_column='IDRequerimiento',
                                          primary_key=True)  # Field name made lowercase.
    codigoalmacen = models.IntegerField(db_column='CodigoAlmacen')  # Field name made lowercase.
    idpresupuesto = models.IntegerField(db_column='IDPresupuesto', blank=True,
                                        null=True)  # Field name made lowercase.
    idfactibilidad = models.IntegerField(db_column='IDFactibilidad', blank=True,
                                         null=True)  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=18,
                                   decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_Requerimientos'

class OtRoles(ClaseModelo):
    idrol = models.AutoField(db_column='IDRol', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_Roles'

class OtSupervisor(ClaseModelo):
    idcontrato = models.IntegerField(db_column='IDContrato')  # Field name made lowercase.
    idarea = models.IntegerField(db_column='IDArea')  # Field name made lowercase., primary_key=True
    iduser = models.IntegerField(db_column='IDUser')  # Field name made lowercase.
    idlocalidad = models.IntegerField(db_column='IDLocalidad', blank=True,
                                      null=True)  # Field name made lowercase.
    idr = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'OT_Supervisor'

class OtTiponodo(ClaseModelo):
    idtnodo = models.AutoField(db_column='IDTNodo', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=20)  # Field name made lowercase.
    simbolo = models.SmallIntegerField(db_column='Simbolo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_TipoNodo'

class OtTipopenalidad(ClaseModelo):
    idtipopenalidad = models.AutoField(db_column='IDTipoPenalidad',
                                       primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_TipoPenalidad'

class OtTiporeclamo(ClaseModelo):
    idtiporeclamo = models.BigIntegerField(db_column='IDTipoReclamo',
                                           primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_TipoReclamo'

class OtUsuamp(ClaseModelo):
    codaut = models.IntegerField(db_column='CodAut', blank=True, null=False, primary_key=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_UsuAmp'

class OtUsuarioarea(ClaseModelo):
    idarea = models.ForeignKey('OtAreaadm', models.DO_NOTHING, db_column='IDArea', primary_key=True)  # Field name made lowercase.
    idusuario = models.ForeignKey('OtUsuarios', models.DO_NOTHING,
                                  db_column='IDUsuario')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_UsuarioArea'

class OtUsuariocontrato(ClaseModelo):
    userid = models.ForeignKey('OtUsuarios', models.DO_NOTHING,
                               db_column='UserID', primary_key=True)  # Field name made lowercase.
    contratoid = models.ForeignKey('OtContratos', models.DO_NOTHING,
                                   db_column='ContratoID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_UsuarioContrato'

class OtUsuarioestado(ClaseModelo):
    idestado = models.ForeignKey('OtEstados', models.DO_NOTHING,
                                 db_column='IDEstado', primary_key=True)  # Field name made lowercase.
    idusuario = models.ForeignKey('OtUsuarios', models.DO_NOTHING,
                                  db_column='IDUsuario')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_UsuarioEstado'

class OtUsuariolocalidad(ClaseModelo):
    idusuario = models.ForeignKey('OtUsuarios', models.DO_NOTHING,
                                  db_column='IDUsuario', primary_key=True)  # Field name made lowercase.
    idlocalidad = models.ForeignKey('OtLocalidad', models.DO_NOTHING,
                                    db_column='IDLocalidad')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_UsuarioLocalidad'

class OtUsuarios(ClaseModelo):
    idu = models.AutoField(db_column='idU', primary_key=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', unique=True, max_length=20)  # Field name made lowercase.
    clave = models.CharField(db_column='Clave', max_length=20)  # Field name made lowercase.
    nombres = models.CharField(db_column='Nombres', max_length=50)  # Field name made lowercase.
    nivel = models.SmallIntegerField(db_column='Nivel')  # Field name made lowercase.
    estado = models.SmallIntegerField(db_column='Estado')  # Field name made lowercase.
    empresa = models.CharField(db_column='Empresa', max_length=50, blank=True,
                               null=True)  # Field name made lowercase.
    nivel2 = models.SmallIntegerField(blank=True, null=True)
    codseal = models.IntegerField(blank=True, null=True)
    idrol = models.ForeignKey('OtRoles', models.DO_NOTHING, db_column='IDRol')  # Field name made lowercase.
    archivo = models.BooleanField(db_column='Archivo', blank=True, null=True)  # Field name made lowercase.
    marchivo = models.CharField(db_column='MArchivo', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    ot = models.BooleanField(db_column='OT', blank=True, null=True)  # Field name made lowercase.
    mot = models.CharField(db_column='MOT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    presupuesto = models.BooleanField(db_column='Presupuesto', blank=True,
                                      null=True)  # Field name made lowercase.
    mpresupuesto = models.CharField(db_column='MPresupuesto', max_length=50, blank=True,
                                    null=True)  # Field name made lowercase.
    factibilidad = models.BooleanField(db_column='Factibilidad', blank=True,
                                       null=True)  # Field name made lowercase.
    mfactibilidad = models.CharField(db_column='MFactibilidad', max_length=50, blank=True,
                                     null=True)  # Field name made lowercase.
    herramientas = models.BooleanField(db_column='Herramientas', blank=True,
                                       null=True)  # Field name made lowercase.
    mherramientas = models.CharField(db_column='MHerramientas', max_length=50, blank=True,
                                     null=True)  # Field name made lowercase.
    reportes = models.BooleanField(db_column='Reportes', blank=True, null=True)  # Field name made lowercase.
    mreportes = models.CharField(db_column='MReportes', max_length=50, blank=True,
                                 null=True)  # Field name made lowercase.
    actividades = models.BooleanField(db_column='Actividades', blank=True,
                                      null=True)  # Field name made lowercase.
    actpc = models.BooleanField(db_column='ActPC', blank=True, null=True)  # Field name made lowercase.
    pcname = models.CharField(db_column='PCName', max_length=10, blank=True,
                              null=True)  # Field name made lowercase.
    penalidades = models.BooleanField(db_column='Penalidades', blank=True,
                                      null=True)  # Field name made lowercase.
    mpenalidades = models.CharField(db_column='MPenalidades', max_length=50, blank=True,
                                    null=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='CODIGO', max_length=10, blank=True,
                              null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OT_Usuarios'

class Ordenescerradas(ClaseModelo):
    item = models.AutoField(primary_key=True)
    nroroden = models.CharField(max_length=20, blank=True, null=True)
    tipo = models.CharField(max_length=3, blank=True, null=True)
    recliq = models.CharField(max_length=20, blank=True, null=True)
    porcentaje = models.CharField(max_length=10, blank=True, null=True)
    importa = models.CharField(max_length=30, blank=True, null=True)
    factura = models.CharField(max_length=20, blank=True, null=True)
    descripcion = models.CharField(max_length=300, blank=True, null=True)
    perini = models.CharField(max_length=10, blank=True, null=True)
    ejeini = models.CharField(max_length=10, blank=True, null=True)
    perfin = models.CharField(max_length=10, blank=True, null=True)
    ejefin = models.CharField(max_length=10, blank=True, null=True)
    fechaproc = models.DateTimeField(blank=True, null=True)
    idot = models.CharField(max_length=10, blank=True, null=True)
    cuenta = models.CharField(max_length=1, blank=True, null=True)
    ordencontrato = models.CharField(max_length=20, blank=True, null=True)
    codcontrato = models.IntegerField(blank=True, null=True)
    codproveedor = models.CharField(max_length=20, blank=True, null=True)
    periodo = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'OrdenesCerradas'

class Ordenescerradasacu(ClaseModelo):
    item = models.AutoField(primary_key=True)
    idacu = models.IntegerField(blank=True, null=True)
    nroroden = models.CharField(max_length=20, blank=True, null=True)
    tipo = models.CharField(max_length=3, blank=True, null=True)
    recliq = models.CharField(max_length=20, blank=True, null=True)
    porcentaje = models.CharField(max_length=10, blank=True, null=True)
    importa = models.CharField(max_length=30, blank=True, null=True)
    factura = models.CharField(max_length=20, blank=True, null=True)
    descripcion = models.CharField(max_length=300, blank=True, null=True)
    perini = models.CharField(max_length=10, blank=True, null=True)
    ejeini = models.CharField(max_length=10, blank=True, null=True)
    perfin = models.CharField(max_length=10, blank=True, null=True)
    ejefin = models.CharField(max_length=10, blank=True, null=True)
    fechaproc = models.DateTimeField(blank=True, null=True)
    cuenta = models.CharField(max_length=1, blank=True, null=True)
    ordencontrato = models.CharField(max_length=20, blank=True, null=True)
    codcontrato = models.IntegerField(blank=True, null=True)
    codproveedor = models.CharField(max_length=20, blank=True, null=True)
    periodo = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'OrdenesCerradasAcu'

class Ordenescerradasacubk(ClaseModelo):
    idacu = models.IntegerField(blank=True, null=False, primary_key=True)
    nroroden = models.CharField(max_length=20, blank=True, null=True)
    tipo = models.CharField(max_length=3, blank=True, null=True)
    recliq = models.CharField(max_length=20, blank=True, null=True)
    porcentaje = models.CharField(max_length=10, blank=True, null=True)
    importa = models.CharField(max_length=30, blank=True, null=True)
    factura = models.CharField(max_length=20, blank=True, null=True)
    descripcion = models.CharField(max_length=300, blank=True, null=True)
    perini = models.CharField(max_length=10, blank=True, null=True)
    ejeini = models.CharField(max_length=10, blank=True, null=True)
    perfin = models.CharField(max_length=10, blank=True, null=True)
    ejefin = models.CharField(max_length=10, blank=True, null=True)
    fechaproc = models.DateTimeField(blank=True, null=True)
    cuenta = models.CharField(max_length=1, blank=True, null=True)
    ordencontrato = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'OrdenesCerradasAcubk'

class Ordenescerradasbk(ClaseModelo):
    nroroden = models.CharField(max_length=20, blank=True, null=False, primary_key=True)
    tipo = models.CharField(max_length=3, blank=True, null=True)
    recliq = models.CharField(max_length=20, blank=True, null=True)
    porcentaje = models.CharField(max_length=10, blank=True, null=True)
    importa = models.CharField(max_length=30, blank=True, null=True)
    factura = models.CharField(max_length=20, blank=True, null=True)
    descripcion = models.CharField(max_length=300, blank=True, null=True)
    perini = models.CharField(max_length=10, blank=True, null=True)
    ejeini = models.CharField(max_length=10, blank=True, null=True)
    perfin = models.CharField(max_length=10, blank=True, null=True)
    ejefin = models.CharField(max_length=10, blank=True, null=True)
    fechaproc = models.DateTimeField(blank=True, null=True)
    idot = models.CharField(max_length=10, blank=True, null=True)
    cuenta = models.CharField(max_length=1, blank=True, null=True)
    ordencontrato = models.CharField(max_length=20, blank=True, null=True)
    codcontrato = models.IntegerField(blank=True, null=True)
    codproveedor = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'OrdenesCerradasbk'

class Ordenessaling(ClaseModelo):
    item = models.AutoField(primary_key=True)
    nroorden = models.CharField(max_length=20, blank=True, null=True)
    idot = models.CharField(max_length=10, blank=True, null=True)
    nrosal = models.CharField(max_length=10, blank=True, null=True)
    nrores = models.CharField(max_length=20, blank=True, null=True)
    nrosoling = models.CharField(max_length=20, blank=True, null=True)
    fechaproc = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'OrdenesSalIng'


class ProveedorS(ClaseModelo):
    item = models.AutoField(primary_key=True)
    idcontrato = models.IntegerField(blank=True, null=True)
    proveedor = models.CharField(max_length=50, blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True, null=True)
    ruc = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Proveedor'

class Reservasabril(ClaseModelo):
    reserva = models.FloatField(db_column='Reserva', blank=True, null=False, primary_key=True)  # Field name made lowercase.
    orden = models.FloatField(db_column='Orden', blank=True, null=True)  # Field name made lowercase.
    imputación = models.FloatField(db_column='Imputación', blank=True, null=True)  # Field name made lowercase.
    ce_coste = models.CharField(db_column='Ce#coste', max_length=255, blank=True,
                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    material = models.FloatField(db_column='Material', blank=True, null=True)  # Field name made lowercase.
    texto_breve_de_material = models.CharField(db_column='Texto breve de material', max_length=255, blank=True,
                                               null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    umb = models.CharField(db_column='UMB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ctd_nec_field = models.FloatField(db_column='Ctd#nec#', blank=True,
                                      null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ctd_dif_field = models.FloatField(db_column='Ctd#dif#', blank=True,
                                      null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    cmv = models.FloatField(db_column='CMv', blank=True, null=True)  # Field name made lowercase.
    alm_field = models.FloatField(db_column='Alm#', blank=True,
                                  null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    rec_field = models.CharField(db_column='Rec#', max_length=255, blank=True,
                                 null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    fecha_nec_field = models.CharField(db_column='Fecha nec#', max_length=255, blank=True,
                                       null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    sfin = models.CharField(db_column='SFin', max_length=255, blank=True,
                            null=True)  # Field name made lowercase.
    tpr = models.CharField(db_column='TpR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fecha_base = models.CharField(db_column='Fecha base', max_length=255, blank=True,
                                  null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    act_fijo = models.CharField(db_column='Act#fijo', max_length=255, blank=True,
                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    destinatario = models.FloatField(db_column='Destinatario', blank=True,
                                     null=True)  # Field name made lowercase.
    bor = models.CharField(db_column='Bor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    clr = models.CharField(db_column='ClR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mov = models.CharField(db_column='Mov', max_length=255, blank=True, null=True)  # Field name made lowercase.
    str = models.CharField(db_column='StR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cnec = models.CharField(db_column='CNec', max_length=255, blank=True,
                            null=True)  # Field name made lowercase.
    ce_field = models.CharField(db_column='Ce#', max_length=255, blank=True,
                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    usuario = models.CharField(db_column='Usuario', max_length=255, blank=True,
                               null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RESERVASABRIL'

class Reservasenero(ClaseModelo):
    reserva = models.FloatField(db_column='Reserva', blank=True, null=False, primary_key=True)  # Field name made lowercase.
    orden = models.FloatField(db_column='Orden', blank=True, null=True)  # Field name made lowercase.
    imputación = models.FloatField(db_column='Imputación', blank=True, null=True)  # Field name made lowercase.
    ce_coste = models.CharField(db_column='Ce#coste', max_length=255, blank=True,
                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    material = models.FloatField(db_column='Material', blank=True, null=True)  # Field name made lowercase.
    texto_breve_de_material = models.CharField(db_column='Texto breve de material', max_length=255, blank=True,
                                               null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    umb = models.CharField(db_column='UMB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ctd_nec_field = models.FloatField(db_column='Ctd#nec#', blank=True,
                                      null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ctd_dif_field = models.FloatField(db_column='Ctd#dif#', blank=True,
                                      null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    cmv = models.FloatField(db_column='CMv', blank=True, null=True)  # Field name made lowercase.
    alm_field = models.FloatField(db_column='Alm#', blank=True,
                                  null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    rec_field = models.CharField(db_column='Rec#', max_length=255, blank=True,
                                 null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    fecha_nec_field = models.CharField(db_column='Fecha nec#', max_length=255, blank=True,
                                       null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    sfin = models.CharField(db_column='SFin', max_length=255, blank=True,
                            null=True)  # Field name made lowercase.
    tpr = models.CharField(db_column='TpR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fecha_base = models.CharField(db_column='Fecha base', max_length=255, blank=True,
                                  null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    destinat_field = models.FloatField(db_column='Destinat#', blank=True,
                                       null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    bor = models.CharField(db_column='Bor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    clr = models.CharField(db_column='ClR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mov = models.CharField(db_column='Mov', max_length=255, blank=True, null=True)  # Field name made lowercase.
    str = models.CharField(db_column='StR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cnec = models.CharField(db_column='CNec', max_length=255, blank=True,
                            null=True)  # Field name made lowercase.
    ce_field = models.CharField(db_column='Ce#', max_length=255, blank=True,
                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'RESERVASENERO$'

class Reservasfebrero(ClaseModelo):
    reserva = models.FloatField(db_column='Reserva', blank=True, null=False, primary_key=True)  # Field name made lowercase.
    orden = models.FloatField(db_column='Orden', blank=True, null=True)  # Field name made lowercase.
    imputacion = models.FloatField(db_column='Imputacion', blank=True, null=True)  # Field name made lowercase.
    ce_coste = models.CharField(db_column='Ce#coste', max_length=255, blank=True,
                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    material = models.FloatField(db_column='Material', blank=True, null=True)  # Field name made lowercase.
    texto_breve_de_material = models.CharField(db_column='Texto breve de material', max_length=255, blank=True,
                                               null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    umb = models.CharField(db_column='UMB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ctd_nec_field = models.FloatField(db_column='Ctd#nec#', blank=True,
                                      null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ctd_dif_field = models.FloatField(db_column='Ctd#dif#', blank=True,
                                      null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    cmv = models.FloatField(db_column='CMv', blank=True, null=True)  # Field name made lowercase.
    alm_field = models.FloatField(db_column='Alm#', blank=True,
                                  null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    rec_field = models.CharField(db_column='Rec#', max_length=255, blank=True,
                                 null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    fecha_nec_field = models.CharField(db_column='Fecha nec#', max_length=255, blank=True,
                                       null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    sfin = models.CharField(db_column='SFin', max_length=255, blank=True,
                            null=True)  # Field name made lowercase.
    tpr = models.CharField(db_column='TpR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fecha_base = models.CharField(db_column='Fecha base', max_length=255, blank=True,
                                  null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    act_fijo = models.CharField(db_column='Act#fijo', max_length=255, blank=True,
                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    destinatario = models.FloatField(db_column='Destinatario', blank=True,
                                     null=True)  # Field name made lowercase.
    bor = models.CharField(db_column='Bor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    clr = models.CharField(db_column='ClR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mov = models.CharField(db_column='Mov', max_length=255, blank=True, null=True)  # Field name made lowercase.
    str = models.CharField(db_column='StR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cnec = models.CharField(db_column='CNec', max_length=255, blank=True,
                            null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RESERVASFEBRERO'

class Reservasmarzo(ClaseModelo):
    reserva = models.FloatField(db_column='Reserva', blank=True, null=False, primary_key=True)  # Field name made lowercase.
    orden = models.FloatField(db_column='Orden', blank=True, null=True)  # Field name made lowercase.
    imputación = models.FloatField(db_column='Imputación', blank=True, null=True)  # Field name made lowercase.
    ce_coste = models.CharField(db_column='Ce#coste', max_length=255, blank=True,
                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    material = models.FloatField(db_column='Material', blank=True, null=True)  # Field name made lowercase.
    texto_breve_de_material = models.CharField(db_column='Texto breve de material', max_length=255, blank=True,
                                               null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    umb = models.CharField(db_column='UMB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ctd_nec_field = models.FloatField(db_column='Ctd#nec#', blank=True,
                                      null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ctd_dif_field = models.FloatField(db_column='Ctd#dif#', blank=True,
                                      null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    cmv = models.FloatField(db_column='CMv', blank=True, null=True)  # Field name made lowercase.
    alm_field = models.FloatField(db_column='Alm#', blank=True,
                                  null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    rec_field = models.CharField(db_column='Rec#', max_length=255, blank=True,
                                 null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    fecha_nec_field = models.CharField(db_column='Fecha nec#', max_length=255, blank=True,
                                       null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    sfin = models.CharField(db_column='SFin', max_length=255, blank=True,
                            null=True)  # Field name made lowercase.
    tpr = models.CharField(db_column='TpR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fecha_base = models.CharField(db_column='Fecha base', max_length=255, blank=True,
                                  null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    act_fijo = models.CharField(db_column='Act#fijo', max_length=255, blank=True,
                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    destinatario = models.FloatField(db_column='Destinatario', blank=True,
                                     null=True)  # Field name made lowercase.
    bor = models.CharField(db_column='Bor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    clr = models.CharField(db_column='ClR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mov = models.CharField(db_column='Mov', max_length=255, blank=True, null=True)  # Field name made lowercase.
    str = models.CharField(db_column='StR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cnec = models.CharField(db_column='CNec', max_length=255, blank=True,
                            null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RESERVASMARZO'

class Reservasmayo(ClaseModelo):
    reserva = models.FloatField(db_column='Reserva', blank=True, null=False, primary_key=True)  # Field name made lowercase.
    orden = models.FloatField(db_column='Orden', blank=True, null=True)  # Field name made lowercase.
    imputación = models.FloatField(db_column='Imputación', blank=True, null=True)  # Field name made lowercase.
    ce_coste = models.CharField(db_column='Ce#coste', max_length=255, blank=True,
                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    material = models.FloatField(db_column='Material', blank=True, null=True)  # Field name made lowercase.
    texto_breve_de_material = models.CharField(db_column='Texto breve de material', max_length=255, blank=True,
                                               null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    umb = models.CharField(db_column='UMB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ctd_nec_field = models.FloatField(db_column='Ctd#nec#', blank=True,
                                      null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ctd_dif_field = models.FloatField(db_column='Ctd#dif#', blank=True,
                                      null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    cmv = models.FloatField(db_column='CMv', blank=True, null=True)  # Field name made lowercase.
    alm_field = models.FloatField(db_column='Alm#', blank=True,
                                  null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    rec_field = models.CharField(db_column='Rec#', max_length=255, blank=True,
                                 null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    fecha_nec_field = models.CharField(db_column='Fecha nec#', max_length=255, blank=True,
                                       null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    sfin = models.CharField(db_column='SFin', max_length=255, blank=True,
                            null=True)  # Field name made lowercase.
    tpr = models.CharField(db_column='TpR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fecha_base = models.CharField(db_column='Fecha base', max_length=255, blank=True,
                                  null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    act_fijo = models.CharField(db_column='Act#fijo', max_length=255, blank=True,
                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    destinatario = models.FloatField(db_column='Destinatario', blank=True,
                                     null=True)  # Field name made lowercase.
    bor = models.CharField(db_column='Bor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    clr = models.CharField(db_column='ClR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mov = models.CharField(db_column='Mov', max_length=255, blank=True, null=True)  # Field name made lowercase.
    str = models.CharField(db_column='StR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cnec = models.CharField(db_column='CNec', max_length=255, blank=True,
                            null=True)  # Field name made lowercase.
    ce_field = models.CharField(db_column='Ce#', max_length=255, blank=True,
                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    usuario = models.CharField(db_column='Usuario', max_length=255, blank=True,
                               null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RESERVASMAYO'

class Vingreso2(ClaseModelo):
    notn07 = models.DecimalField(db_column='NOTN07', max_digits=8, decimal_places=0, blank=True,
                                 null=False, primary_key=True)  # Field name made lowercase.
    tipde2 = models.CharField(db_column='TIPDE2', max_length=35, blank=True,
                              null=True)  # Field name made lowercase.
    notord = models.CharField(db_column='NOTORD', max_length=10, blank=True,
                              null=True)  # Field name made lowercase.
    notor2 = models.CharField(db_column='NOTOR2', max_length=10, blank=True,
                              null=True)  # Field name made lowercase.
    notmat = models.DecimalField(db_column='NOTMAT', max_digits=6, decimal_places=0, blank=True,
                                 null=True)  # Field name made lowercase.
    almdes = models.CharField(db_column='ALMDES', max_length=50, blank=True,
                              null=True)  # Field name made lowercase.
    notca2 = models.DecimalField(db_column='NOTCA2', max_digits=10, decimal_places=3, blank=True,
                                 null=True)  # Field name made lowercase.
    notn13 = models.DecimalField(db_column='NOTN13', max_digits=8, decimal_places=0, blank=True,
                                 null=True)  # Field name made lowercase.
    notf08 = models.DecimalField(db_column='NOTF08', max_digits=8, decimal_places=0, blank=True,
                                 null=True)  # Field name made lowercase.
    notn10 = models.DecimalField(db_column='NOTN10', max_digits=8, decimal_places=0, blank=True,
                                 null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VINGRESO2'

class Vsalidas(ClaseModelo):
    notn03 = models.DecimalField(db_column='NOTN03', max_digits=8, decimal_places=0, blank=True,
                                 null=False, primary_key=True)  # Field name made lowercase.
    notord = models.CharField(db_column='NOTORD', max_length=10, blank=True,
                              null=True)  # Field name made lowercase.
    notco6 = models.DecimalField(db_column='NOTCO6', max_digits=6, decimal_places=0, blank=True,
                                 null=True)  # Field name made lowercase.
    almdes = models.CharField(db_column='ALMDES', max_length=50, blank=True,
                              null=True)  # Field name made lowercase.
    notcan = models.DecimalField(db_column='NOTCAN', max_digits=10, decimal_places=3, blank=True,
                                 null=True)  # Field name made lowercase.
    notn02 = models.DecimalField(db_column='NOTN02', max_digits=6, decimal_places=0, blank=True,
                                 null=True)  # Field name made lowercase.
    notf01 = models.DecimalField(db_column='NOTF01', max_digits=8, decimal_places=0, blank=True,
                                 null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VSALIDAS'

class Actividades017(ClaseModelo):
    a = models.FloatField(db_column='A', blank=True, null=False, primary_key=True)  # Field name made lowercase.
    b = models.CharField(db_column='B', max_length=255, blank=True, null=True)  # Field name made lowercase.
    c = models.CharField(db_column='C', max_length=255, blank=True, null=True)  # Field name made lowercase.
    d = models.FloatField(db_column='D', blank=True, null=True)  # Field name made lowercase.
    e = models.CharField(db_column='E', max_length=255, blank=True, null=True)  # Field name made lowercase.
    f = models.FloatField(db_column='F', blank=True, null=True)  # Field name made lowercase.
    g = models.FloatField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    h = models.CharField(db_column='H', max_length=255, blank=True, null=True)  # Field name made lowercase.
    i = models.CharField(db_column='I', max_length=255, blank=True, null=True)  # Field name made lowercase.
    j = models.CharField(db_column='J', max_length=255, blank=True, null=True)  # Field name made lowercase.
    k = models.FloatField(db_column='K', blank=True, null=True)  # Field name made lowercase.
    l = models.FloatField(db_column='L', blank=True, null=True)  # Field name made lowercase.
    m = models.FloatField(db_column='M', blank=True, null=True)  # Field name made lowercase.
    n = models.CharField(db_column='N', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'actividades017'

class Archivoformato(ClaseModelo):
    item = models.BigAutoField(primary_key=True)
    idot = models.BigIntegerField(db_column='IDOT', blank=True, null=True)  # Field name made lowercase.
    archivo = models.BinaryField(blank=True, null=True)
    fecreg = models.DateTimeField(blank=True, null=True)
    usureg = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'archivoFormato'

class Archivoing(ClaseModelo):
    item = models.BigAutoField(primary_key=True)
    nrosoling = models.BigIntegerField(db_column='Nrosoling', blank=True,
                                       null=True)  # Field name made lowercase.
    archivo = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'archivoing'

class Archivoplazo(ClaseModelo):
    item = models.BigAutoField(primary_key=True)
    idot = models.BigIntegerField(db_column='IDOT', blank=True, null=True)  # Field name made lowercase.
    archivo = models.BinaryField(blank=True, null=True)
    fecreg = models.DateTimeField(blank=True, null=True)
    usureg = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'archivoplazo'

class Cecosrural(ClaseModelo):
    codigo = models.FloatField(db_column='CODIGO', blank=True, null=False, primary_key=True)  # Field name made lowercase.
    descripcio = models.CharField(db_column='DESCRIPCIO', max_length=255, blank=True,
                                  null=True)  # Field name made lowercase.
    ccos = models.CharField(db_column='CCOS', max_length=255, blank=True,
                            null=True)  # Field name made lowercase.
    padre = models.FloatField(db_column='PADRE', blank=True, null=True)  # Field name made lowercase.
    ceges = models.CharField(db_column='CEGES', max_length=255, blank=True,
                             null=True)  # Field name made lowercase.
    cebes = models.CharField(db_column='CEBES', max_length=255, blank=True,
                             null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cecosrural'

class Con123(ClaseModelo):
    idactividad = models.CharField(db_column='IDActividad', max_length=255, blank=True,
                                   null=False, primary_key=True)  # Field name made lowercase.
    nivelcontrato = models.FloatField(db_column='NivelContrato', blank=True,
                                      null=True)  # Field name made lowercase.
    detalle = models.CharField(db_column='Detalle', max_length=255, blank=True,
                               null=True)  # Field name made lowercase.
    unidad = models.CharField(db_column='Unidad', max_length=255, blank=True,
                              null=True)  # Field name made lowercase.
    pu_s_field = models.FloatField(db_column='PU (S/#)', blank=True,
                                   null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    estado = models.FloatField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    codactividad = models.FloatField(db_column='CodActividad', blank=True,
                                     null=True)  # Field name made lowercase.
    codantiguo = models.CharField(db_column='CodAntiguo', max_length=255, blank=True,
                                  null=True)  # Field name made lowercase.
    ca = models.CharField(db_column='CA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cn = models.CharField(db_column='CN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    idcontrato = models.FloatField(db_column='IDContrato', blank=True, null=True)  # Field name made lowercase.
    idareaadm = models.FloatField(db_column='IDAreaAdm', blank=True, null=True)  # Field name made lowercase.
    idlocalidad = models.FloatField(db_column='IDLocalidad', blank=True,
                                    null=True)  # Field name made lowercase.
    ctatipo = models.CharField(db_column='CtaTipo', max_length=255, blank=True,
                               null=True)  # Field name made lowercase.
    ctastipo = models.CharField(db_column='CtaSTipo', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    cantidad = models.FloatField(db_column='Cantidad', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'con123'

class Con125(ClaseModelo):
    idactividad = models.CharField(db_column='IDActividad', max_length=255, blank=True,
                                   null=False, primary_key=True)  # Field name made lowercase.
    nivelcontrato = models.FloatField(db_column='NivelContrato', blank=True,
                                      null=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    unidad = models.CharField(db_column='Unidad', max_length=255, blank=True,
                              null=True)  # Field name made lowercase.
    pu = models.FloatField(db_column='PU', blank=True, null=True)  # Field name made lowercase.
    estado = models.FloatField(db_column='ESTADO', blank=True, null=True)  # Field name made lowercase.
    código_actividad = models.FloatField(db_column='Código Actividad', blank=True,
                                         null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    codantiguo = models.CharField(db_column='CodAntiguo', max_length=255, blank=True,
                                  null=True)  # Field name made lowercase.
    ca = models.CharField(db_column='CA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cn = models.CharField(db_column='CN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    idcontrato = models.FloatField(db_column='IDContrato', blank=True, null=True)  # Field name made lowercase.
    idareaadm = models.FloatField(db_column='IDAreaAdm', blank=True, null=True)  # Field name made lowercase.
    idlocalidad = models.FloatField(db_column='IDLocalidad', blank=True,
                                    null=True)  # Field name made lowercase.
    ctatipo = models.CharField(db_column='CtaTipo', max_length=255, blank=True,
                               null=True)  # Field name made lowercase.
    ctastipo = models.CharField(db_column='CtaSTipo', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    cantidad = models.FloatField(db_column='Cantidad', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'con125'

# class Nima(ClaseModelo):
#     nima = models.FloatField(db_column='NIMA', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'nima'
#
# class Nimat(ClaseModelo):
#     nimat = models.FloatField(db_column='NIMAT', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'nimat'
#
# class Nimc(ClaseModelo):
#     nim = models.FloatField(db_column='NIM', blank=True, null=True)  # Field name made lowercase.
#     serie = models.FloatField(blank=True, null=True)
#     suministro = models.FloatField(db_column='Suministro', blank=True, null=True)  # Field name made lowercase.
#     fecha_ejecución = models.DateTimeField(db_column='Fecha Ejecución', blank=True,
#                                            null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#
#     class Meta:
#         managed = False
#         db_table = 'nimc'
#
# class Nimra(ClaseModelo):
#     nimf = models.FloatField(db_column='NIMF', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'nimra'
#
# class Nimrobados(ClaseModelo):
#     nimr = models.FloatField(db_column='NIMR', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'nimrobados'

# class Ots2(ClaseModelo):
#     nuevov = models.DecimalField(max_digits=38, decimal_places=4, blank=True, null=True)
#     idot = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'ots2'

class Paratic(ClaseModelo):
    item = models.FloatField(blank=True, null=False, primary_key=True)
    idtipopenalidad = models.FloatField(db_column='idTipoPenalidad', blank=True,
                                        null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=255, blank=True,
                                   null=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=255, blank=True,
                              null=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=255, blank=True,
                              null=True)  # Field name made lowercase.
    unidad = models.CharField(db_column='Unidad', max_length=255, blank=True,
                              null=True)  # Field name made lowercase.
    pu = models.FloatField(db_column='PU', blank=True, null=True)  # Field name made lowercase.
    adicional = models.CharField(db_column='Adicional', max_length=255, blank=True,
                                 null=True)  # Field name made lowercase.
    contratos = models.CharField(db_column='Contratos', max_length=255, blank=True,
                                 null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'paratic'

# class Pen2(ClaseModelo):
#     codigo = models.FloatField(db_column='Codigo', blank=True, null=True)  # Field name made lowercase.
#     idtipopenalidad = models.FloatField(db_column='IDTipoPenalidad', blank=True,
#                                         null=True)  # Field name made lowercase.
#     nombre = models.CharField(db_column='Nombre', max_length=255, blank=True,
#                               null=True)  # Field name made lowercase.
#     unidad = models.CharField(db_column='Unidad', max_length=255, blank=True,
#                               null=True)  # Field name made lowercase.
#     pu = models.FloatField(db_column='PU', blank=True, null=True)  # Field name made lowercase.
#     adicional = models.CharField(db_column='Adicional', max_length=255, blank=True,
#                                  null=True)  # Field name made lowercase.
#     idcontrato = models.FloatField(db_column='IDContrato', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'pen2'

class Sysdiagrams(ClaseModelo):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)

# class Temporal11(ClaseModelo):
#     idot = models.IntegerField()
#     totalot = models.DecimalField(db_column='TotalOT', max_digits=38, decimal_places=4, blank=True,
#                                   null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'temporal11'
        
