from datetime import datetime
import json
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import generic
from django.http import HttpResponseRedirect, JsonResponse, JsonResponse, HttpResponse
from django.urls import reverse_lazy
from django.db.models import Sum
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from .models import (Idioma, Frase, Categoria, SubCategoria, Marca, UnidadMedida, Producto,
                     Proveedor, ComprasEnc, ComprasDet, Producto, Cliente, FacturaEnc, FacturaDet)
from .forms import (CategoriaForm, SubCategoriaForm, MarcaForm, UMForm, ProductoForm,
                    ProveedorForm, ComprasEncForm, ClienteForm)


# *********************************************************************
# *                        VIEWS FROM BASES                           *
# *********************************************************************


class MixinFormInvalid:
    def form_invalid(self,form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response


class SinPrivilegios(LoginRequiredMixin, PermissionRequiredMixin, MixinFormInvalid):
    login_url = 'bases:login'
    raise_exception=False
    redirect_field_name="redirecto_to"

    def handle_no_permission(self):
        from django.contrib.auth.models import AnonymousUser
        if not self.request.user==AnonymousUser():
            self.login_url='bases:sin_privilegios'
        return HttpResponseRedirect(reverse_lazy(self.login_url))


class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'bases/home.html'
    login_url='bases:login'


class HomeSinPrivilegios(LoginRequiredMixin, generic.TemplateView):
    login_url = "bases:login"
    template_name="bases/sin_privilegios.html"


class IdiomaList(generic.ListView):
    template_name = "bases/idiomas.html"
    model = Idioma
    context_object_name="obj"


class FraseList(generic.ListView):
    template_name = "bases/frases.html"
    model = Frase
    context_object_name="obj"

    def get_queryset(self):
        qs = Frase.objects.all()
        idioma_id = self.request.GET.get("lang")
        if idioma_id:
            qs = qs.filter(idioma__id=idioma_id)
        return qs


# *********************************************************************
# *                          VIEWS FROM INV                           *
# *********************************************************************


class CategoriaView(SinPrivilegios, generic.ListView):
    permission_required = "inv.view_categoria"
    model = Categoria
    template_name = "inv/categoria_list.html"
    context_object_name = "obj"


class CategoriaNew(SuccessMessageMixin, SinPrivilegios, generic.CreateView):
    permission_required = "inv.add_categoria"
    model = Categoria
    template_name = "inv/categoria_form.html"
    context_object_name = "obj"
    form_class = CategoriaForm
    success_url = reverse_lazy("inv:categoria_list")
    success_message = "Categoria Creada Satisfactoriamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class CategoriaEdit(SuccessMessageMixin, SinPrivilegios, generic.UpdateView):
    permission_required = "inv.change_categoria"
    model = Categoria
    template_name = "inv/categoria_form.html"
    context_object_name = "obj"
    form_class = CategoriaForm
    success_url = reverse_lazy("inv:categoria_list")
    success_message = "Categoria Actualizada Satisfactoriamente"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


class CategoriaDel(SuccessMessageMixin, SinPrivilegios, generic.DeleteView):
    permission_required = "inv.delete_categoria"
    model = Categoria
    template_name = 'inv/catalogos_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy("inv:categoria_list")
    success_message = "Categoría Eliminada Satisfactoriamente"


class SubCategoriaView(SinPrivilegios, generic.ListView):
    permission_required = "inv.view_subcategoria"
    model = SubCategoria
    template_name = "inv/subcategoria_list.html"
    context_object_name = "obj"


class SubCategoriaNew(SuccessMessageMixin, SinPrivilegios, generic.CreateView):
    model = SubCategoria
    template_name = "inv/subcategoria_form.html"
    context_object_name = "obj"
    form_class = SubCategoriaForm
    success_url = reverse_lazy("inv:subcategoria_list")
    success_message = "Sub Categoría Creada Satisfactoriamente"
    permission_required = "inv.add_subcategoria"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class SubCategoriaEdit(SuccessMessageMixin, SinPrivilegios, generic.UpdateView):
    model = SubCategoria
    template_name = "inv/subcategoria_form.html"
    context_object_name = "obj"
    form_class = SubCategoriaForm
    success_url = reverse_lazy("inv:subcategoria_list")
    success_message = "Sub Categoría Actualizada Satisfactoriamente"
    permission_required = "inv.change_subcatetoria"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


class SubCategoriaDel(SuccessMessageMixin, SinPrivilegios, generic.DeleteView):
    model = SubCategoria
    template_name = 'inv/catalogos_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy("inv:subcategoria_list")
    success_message = "Sub Categoría Eliminada"
    permission_required = "inv.delete_subcategoria"


class MarcaView(SinPrivilegios, generic.ListView):
    permission_required = "inv.view_marca"
    model = Marca
    template_name = "inv/marca_list.html"
    context_object_name = "obj"


class MarcaNew(SuccessMessageMixin, SinPrivilegios, generic.CreateView):
    model = Marca
    template_name = "inv/marca_form.html"
    context_object_name = 'obj'
    form_class = MarcaForm
    success_url = reverse_lazy("inv:marca_list")
    success_message = "Marca Creada"
    permission_required = "inv.add_marca"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class MarcaEdit(SuccessMessageMixin, SinPrivilegios, generic.UpdateView):
    model = Marca
    template_name = "inv/marca_form.html"
    context_object_name = 'obj'
    form_class = MarcaForm
    success_url = reverse_lazy("inv:marca_list")
    success_messag = "Marca Editada"
    permission_required = "inv.change_marca"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


@login_required(login_url='/login/')
@permission_required('inv.change_marca', login_url='bases:sin_privilegios')
def marca_inactivar(request, id):
    marca = Marca.objects.filter(pk=id).first()
    contexto = {}
    template_name = "inv/catalogos_del.html"

    if not marca:
        return redirect("inv:marca_list")

    if request.method == 'GET':
        contexto = {'obj': marca}

    if request.method == 'POST':
        marca.estado = False
        marca.save()
        messages.success(request, 'Marca Inactivada')
        return redirect("inv:marca_list")

    return render(request, template_name, contexto)


class UMView(SinPrivilegios, generic.ListView):
    model = UnidadMedida
    template_name = "inv/um_list.html"
    context_object_name = "obj"
    permission_required = "inv.view_unidadmedida"


class UMNew(SuccessMessageMixin, SinPrivilegios, generic.CreateView):
    model = UnidadMedida
    template_name = "inv/um_form.html"
    context_object_name = 'obj'
    form_class = UMForm
    success_url = reverse_lazy("inv:um_list")
    success_message = "Unidad Medida Creada"
    permission_required = "inv.add_unidadmedida"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        print(self.request.user.id)
        return super().form_valid(form)


class UMEdit(SuccessMessageMixin, SinPrivilegios, generic.UpdateView):
    model = UnidadMedida
    template_name = "inv/um_form.html"
    context_object_name = 'obj'
    form_class = UMForm
    success_url = reverse_lazy("inv:um_list")
    success_message = "Unidad Medida Editada"
    permission_required = "inv.change_unidadmedida"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        print(self.request.user.id)
        return super().form_valid(form)


@login_required(login_url="/login/")
@permission_required("inv.change_unidadmedida", login_url="/login/")
def um_inactivar(request, id):
    um = UnidadMedida.objects.filter(pk=id).first()
    contexto = {}
    template_name = "inv/catalogos_del.html"

    if not um:
        return redirect("inv:um_list")

    if request.method == 'GET':
        contexto = {'obj': um}

    if request.method == 'POST':
        um.estado = False
        um.save()
        return redirect("inv:um_list")

    return render(request, template_name, contexto)


class ProductoView(SinPrivilegios, generic.ListView):
    model = Producto
    template_name = "inv/prducto_list.html"
    context_object_name = "obj"
    permission_required = "inv.view_producto"


class ProductoNew(SuccessMessageMixin, SinPrivilegios, generic.CreateView):
    model = Producto
    template_name = "inv/producto_form.html"
    context_object_name = 'obj'
    form_class = ProductoForm
    success_url = reverse_lazy("inv:producto_list")
    success_message = "Producto Creado"
    permission_required = "inv.add_producto"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ProductoNew, self).get_context_data(**kwargs)
        context["categorias"] = Categoria.objects.all()
        context["subcategorias"] = SubCategoria.objects.all()
        return context


class ProductoEdit(SuccessMessageMixin, SinPrivilegios, generic.UpdateView):
    model = Producto
    template_name = "inv/producto_form.html"
    context_object_name = 'obj'
    form_class = ProductoForm
    success_url = reverse_lazy("inv:producto_list")
    success_message = "Producto Editado"
    permission_required = "inv.change_producto"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')

        context = super(ProductoEdit, self).get_context_data(**kwargs)
        context["categorias"] = Categoria.objects.all()
        context["subcategorias"] = SubCategoria.objects.all()
        context["obj"] = Producto.objects.filter(pk=pk).first()

        return context


@login_required(login_url="/login/")
@permission_required("inv.change_producto", login_url="/login/")
def producto_inactivar(request, id):
    prod = Producto.objects.filter(pk=id).first()
    contexto = {}
    template_name = "inv/catalogos_del.html"

    if not prod:
        return redirect("inv:producto_list")

    if request.method == 'GET':
        contexto = {'obj': prod}

    if request.method == 'POST':
        prod.estado = False
        prod.save()
        return redirect("inv:producto_list")

    return render(request, template_name, contexto)


# *********************************************************************
# *                          VIEWS FROM CMP                           *
# *********************************************************************

class ProveedorView(SinPrivilegios, generic.ListView):
    model = Proveedor
    template_name = "cmp/proveedor_list.html"
    context_object_name = "obj"
    permission_required = "cmp.view_proveedor"


class ProveedorNew(SuccessMessageMixin, SinPrivilegios, \
                   generic.CreateView):
    model = Proveedor
    template_name = "cmp/proveedor_form.html"
    context_object_name = 'obj'
    form_class = ProveedorForm
    success_url = reverse_lazy("cmp:proveedor_list")
    success_message = "Proveedor Nuevo"
    permission_required = "cmp.add_proveedor"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        # print(self.request.user.id)
        return super().form_valid(form)


class ProveedorEdit(SuccessMessageMixin, SinPrivilegios, \
                    generic.UpdateView):
    model = Proveedor
    template_name = "cmp/proveedor_form.html"
    context_object_name = 'obj'
    form_class = ProveedorForm
    success_url = reverse_lazy("cmp:proveedor_list")
    success_message = "Proveedor Editado"
    permission_required = "cmp.change_proveedor"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        print(self.request.user.id)
        return super().form_valid(form)


@login_required(login_url="/login/")
@permission_required("cmp.change_proveedor", login_url="/login/")
def proveedorInactivar(request, id):
    template_name = 'cmp/inactivar_prv.html'
    contexto = {}
    prv = Proveedor.objects.filter(pk=id).first()

    if not prv:
        return HttpResponse('Proveedor no existe ' + str(id))

    if request.method == 'GET':
        contexto = {'obj': prv}

    if request.method == 'POST':
        prv.estado = False
        prv.save()
        contexto = {'obj': 'OK'}
        return HttpResponse('Proveedor Inactivado')

    return render(request, template_name, contexto)


class ComprasView(SinPrivilegios, generic.ListView):
    model = ComprasEnc
    template_name = "cmp/compras_list.html"
    context_object_name = "obj"
    permission_required = "cmp.view_comprasenc"


@login_required(login_url='/login/')
@permission_required('cmp.view_comprasenc', login_url='bases:sin_privilegios')
def compras(request, compra_id=None):
    template_name = "cmp/compras.html"
    prod = Producto.objects.filter(estado=True)
    form_compras = {}
    contexto = {}

    if request.method == 'GET':
        form_compras = ComprasEncForm()
        enc = ComprasEnc.objects.filter(pk=compra_id).first()

        if enc:
            det = ComprasDet.objects.filter(compra=enc)
            fecha_compra = datetime.date.isoformat(enc.fecha_compra)
            fecha_factura = datetime.date.isoformat(enc.fecha_factura)
            e = {
                'fecha_compra': fecha_compra,
                'proveedor': enc.proveedor,
                'observacion': enc.observacion,
                'no_factura': enc.no_factura,
                'fecha_factura': fecha_factura,
                'sub_total': enc.sub_total,
                'descuento': enc.descuento,
                'total': enc.total
            }
            form_compras = ComprasEncForm(e)
        else:
            det = None

        contexto = {'productos': prod, 'encabezado': enc, 'detalle': det, 'form_enc': form_compras}

    if request.method == 'POST':
        fecha_compra = request.POST.get("fecha_compra")
        observacion = request.POST.get("observacion")
        no_factura = request.POST.get("no_factura")
        fecha_factura = request.POST.get("fecha_factura")
        proveedor = request.POST.get("proveedor")
        sub_total = 0
        descuento = 0
        total = 0

        if not compra_id:
            prov = Proveedor.objects.get(pk=proveedor)

            enc = ComprasEnc(
                fecha_compra=fecha_compra,
                observacion=observacion,
                no_factura=no_factura,
                fecha_factura=fecha_factura,
                proveedor=prov,
                uc=request.user
            )
            if enc:
                enc.save()
                compra_id = enc.id
        else:
            enc = ComprasEnc.objects.filter(pk=compra_id).first()
            if enc:
                enc.fecha_compra = fecha_compra
                enc.observacion = observacion
                enc.no_factura = no_factura
                enc.fecha_factura = fecha_factura
                enc.um = request.user.id
                enc.save()

        if not compra_id:
            return redirect("cmp:compras_list")

        producto = request.POST.get("id_id_producto")
        cantidad = request.POST.get("id_cantidad_detalle")
        precio = request.POST.get("id_precio_detalle")
        sub_total_detalle = request.POST.get("id_sub_total_detalle")
        descuento_detalle = request.POST.get("id_descuento_detalle")
        total_detalle = request.POST.get("id_total_detalle")

        prod = Producto.objects.get(pk=producto)

        det = ComprasDet(
            compra=enc,
            producto=prod,
            cantidad=cantidad,
            precio_prv=precio,
            descuento=descuento_detalle,
            costo=0,
            uc=request.user
        )

        if det:
            det.save()

            sub_total = ComprasDet.objects.filter(compra=compra_id).aggregate(Sum('sub_total'))
            descuento = ComprasDet.objects.filter(compra=compra_id).aggregate(Sum('descuento'))
            enc.sub_total = sub_total["sub_total__sum"]
            enc.descuento = descuento["descuento__sum"]
            enc.save()

        return redirect("cmp:compras_edit", compra_id=compra_id)

    return render(request, template_name, contexto)


class CompraDetDelete(SinPrivilegios, generic.DeleteView):
    permission_required = "cmp.delete_comprasdet"
    model = ComprasDet
    template_name = "cmp/compras_det_del.html"
    context_object_name = 'obj'

    def get_success_url(self):
        compra_id = self.kwargs['compra_id']
        return reverse_lazy('cmp:compras_edit', kwargs={'compra_id': compra_id})


# *********************************************************************
# *                        VIEWS FROM FAC                             *
# *********************************************************************


class ClienteView(SinPrivilegios, generic.ListView):
    model = Cliente
    template_name = "fac/cliente_list.html"
    context_object_name = "obj"
    permission_required = "cmp.view_cliente"


class VistaBaseCreate(SuccessMessageMixin, SinPrivilegios, \
                      generic.CreateView):
    context_object_name = 'obj'
    success_message = "Registro Agregado Satisfactoriamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class VistaBaseEdit(SuccessMessageMixin, SinPrivilegios, \
                    generic.UpdateView):
    context_object_name = 'obj'
    success_message = "Registro Actualizado Satisfactoriamente"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


class ClienteNew(VistaBaseCreate):
    model = Cliente
    template_name = "fac/cliente_form.html"
    form_class = ClienteForm
    success_url = reverse_lazy("fac:cliente_list")
    permission_required = "fac.add_cliente"

    def get(self, request, *args, **kwargs):
        print("sobre escribir get")

        try:
            t = request.GET["t"]
        except:
            t = None

        print(t)

        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form, 't': t})


class ClienteEdit(VistaBaseEdit):
    model = Cliente
    template_name = "fac/cliente_form.html"
    form_class = ClienteForm
    success_url = reverse_lazy("fac:cliente_list")
    permission_required = "fac.change_cliente"

    def get(self, request, *args, **kwargs):
        print("sobre escribir get en editar")

        print(request)

        try:
            t = request.GET["t"]
        except:
            t = None

        print(t)
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object=self.object, form=form, t=t)
        print(form_class, form, context)
        return self.render_to_response(context)


@login_required(login_url="/login/")
@permission_required("fac.change_cliente", login_url="/login/")
def clienteInactivar(request, id):
    cliente = Cliente.objects.filter(pk=id).first()

    if request.method == "POST":
        if cliente:
            cliente.estado = not cliente.estado
            cliente.save()
            return HttpResponse("OK")
        return HttpResponse("FAIL")

    return HttpResponse("FAIL")


class FacturaView(SinPrivilegios, generic.ListView):
    model = FacturaEnc
    template_name = "fac/factura_list.html"
    context_object_name = "obj"
    permission_required = "fac.view_facturaenc"

    def get_queryset(self):
        user = self.request.user
        # print(user,"usuario")
        qs = super().get_queryset()
        for q in qs:
            print(q.uc, q.id)

        if not user.is_superuser:
            qs = qs.filter(uc=user)

        for q in qs:
            print(q.uc, q.id)

        return qs


@login_required(login_url='/login/')
@permission_required('fac.change_facturaenc', login_url='bases:sin_privilegios')
def facturas(request, id=None):
    template_name = 'fac/facturas.html'

    detalle = {}
    clientes = Cliente.objects.filter(estado=True)

    if request.method == "GET":
        enc = FacturaEnc.objects.filter(pk=id).first()
        if id:
            if not enc:
                messages.error(request, 'Factura No Existe')
                return redirect("fac:factura_list")

            usr = request.user
            if not usr.is_superuser:
                if enc.uc != usr:
                    messages.error(request, 'Factura no fue creada por usuario')
                    return redirect("fac:factura_list")

        if not enc:
            encabezado = {
                'id': 0,
                'fecha': datetime.today(),
                'cliente': 0,
                'sub_total': 0.00,
                'descuento': 0.00,
                'total': 0.00
            }
            detalle = None
        else:
            encabezado = {
                'id': enc.id,
                'fecha': enc.fecha,
                'cliente': enc.cliente,
                'sub_total': enc.sub_total,
                'descuento': enc.descuento,
                'total': enc.total
            }

        detalle = FacturaDet.objects.filter(factura=enc)
        contexto = {"enc": encabezado, "det": detalle, "clientes": clientes}
        return render(request, template_name, contexto)

    if request.method == "POST":
        cliente = request.POST.get("enc_cliente")
        fecha = request.POST.get("fecha")
        cli = Cliente.objects.get(pk=cliente)

        if not id:
            enc = FacturaEnc(
                cliente=cli,
                fecha=fecha
            )
            if enc:
                enc.save()
                id = enc.id
        else:
            enc = FacturaEnc.objects.filter(pk=id).first()
            if enc:
                enc.cliente = cli
                enc.save()

        if not id:
            messages.error(request, 'No Puedo Continuar No Pude Detectar No. de Factura')
            return redirect("fac:factura_list")

        codigo = request.POST.get("codigo")
        cantidad = request.POST.get("cantidad")
        precio = request.POST.get("precio")
        s_total = request.POST.get("sub_total_detalle")
        descuento = request.POST.get("descuento_detalle")
        total = request.POST.get("total_detalle")

        prod = Producto.objects.get(codigo=codigo)
        det = FacturaDet(
            factura=enc,
            producto=prod,
            cantidad=cantidad,
            precio=precio,
            sub_total=s_total,
            descuento=descuento,
            total=total
        )

        if det:
            det.save()

        return redirect("fac:factura_edit", id=id)

    return render(request, template_name, context=None)


class FacProductoView(ProductoView):
    template_name = "fac/buscar_producto.html"


def borrar_detalle_factura(request, id):
    template_name = "fac/factura_borrar_detalle.html"

    det = FacturaDet.objects.get(pk=id)

    if request.method == "GET":
        context = {"det": det}

    if request.method == "POST":
        usr = request.POST.get("usuario")
        pas = request.POST.get("pass")

        user = authenticate(username=usr, password=pas)

        if not user:
            return HttpResponse("Usuario o Clave Incorrecta")

        if not user.is_active:
            return HttpResponse("Usuario Inactivo")

        if user.is_superuser or user.has_perm("fac.sup_caja_facturadet"):
            det.id = None
            det.cantidad = (-1 * det.cantidad)
            det.sub_total = (-1 * det.sub_total)
            det.descuento = (-1 * det.descuento)
            det.total = (-1 * det.total)
            det.save()

            return HttpResponse("ok")

        return HttpResponse("Usuario no autorizado")

    return render(request, template_name, context)


@login_required(login_url="/login/")
@permission_required("fac.change_cliente", login_url="/login/")
def cliente_add_modify(request, pk=None):
    template_name = "fac/cliente_form.html"
    context = {}

    if request.method == "GET":
        context["t"] = "fc"
        if not pk:
            form = ClienteForm()
        else:
            cliente = Cliente.objects.filter(id=pk).first()
            form = ClienteForm(instance=cliente)
            context["obj"] = cliente
        context["form"] = form
    else:
        nombres = request.POST.get("nombres")
        apellidos = request.POST.get("apellidos")
        celular = request.POST.get("celular")
        tipo = request.POST.get("tipo")
        usr = request.user

        if not pk:
            cliente = Cliente.objects.create(
                nombres=nombres,
                apellidos=apellidos,
                celular=celular,
                tipo=tipo,
                uc=usr,
            )
        else:
            cliente = Cliente.objects.filter(id=pk).first()
            cliente.nombres = nombres
            cliente.apellidos = apellidos
            cliente.celular = celular
            cliente.tipo = tipo
            cliente.um = usr.id

        cliente.save()
        if not cliente:
            return HttpResponse("No pude Guardar/Crear Cliente")

        id = cliente.id
        return HttpResponse(id)

    return render(request, template_name, context)
