from django.urls import path, include
from django.contrib.auth import views as auth_views

from .views import *
from .reportes import *


bases_urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='bases/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='bases/login.html'), name='logout'),

    path('sin_privilegios/', HomeSinPrivilegios.as_view(), name='sin_privilegios'),

    path('idiomas/', IdiomaList.as_view(), name="idiomas"),
    path('frases/', FraseList.as_view(), name="frases"),
]


cmp_urlpatterns = [
    path('proveedores/', ProveedorView.as_view(), name="proveedor_list"),
    path('proveedores/new', ProveedorNew.as_view(), name="proveedor_new"),
    path('proveedores/edit/<int:pk>', ProveedorEdit.as_view(), name="proveedor_edit"),
    path('proveedores/inactivar/<int:id>', proveedorInactivar, name="proveedor_inactivar"),

    path('compras/', ComprasView.as_view(), name="compras_list"),
    path('compras/new', compras, name="compras_new"),
    path('compras/edit/<int:compra_id>', compras, name="compras_edit"),
    path('compras/<int:compra_id>/delete/<int:pk>', CompraDetDelete.as_view(), name="compras_del"),

    path('compras/listado', reporte_compras, name='compras_print_all'),
    path('compras/<int:compra_id>/imprimir', imprimir_compra, name="compras_print_one"),
]


fac_urlpatterns = [
    path('clientes/',ClienteView.as_view(), name="cliente_list"),
    path('clientes/new',ClienteNew.as_view(), name="cliente_new"),
    path('clientes/<int:pk>',ClienteEdit.as_view(), name="cliente_edit"),
    path('clientes/estado/<int:id>',clienteInactivar, name="cliente_inactivar"),

    path('facturas/',FacturaView.as_view(), name="factura_list"),
    path('facturas/new',facturas, name="factura_new"),
    path('facturas/edit/<int:id>',facturas, name="factura_edit"),

    path('facturas/buscar-producto',ProductoView.as_view(), name="factura_producto"),

    path('facturas/borrar-detalle/<int:id>',borrar_detalle_factura, name="factura_borrar_detalle"),

    path('facturas/imprimir/<int:id>',imprimir_factura_recibo, name="factura_imprimir_one"),

    path('facturas/imprimir-todas/<str:f1>/<str:f2>',imprimir_factura_list, name="factura_imprimir_all"),

    path('facturas/clientes/new/',cliente_add_modify,name="fac_cliente_add"),
    path('facturas/clientes/<int:pk>',cliente_add_modify,name="fac_cliente_mod"),
]


inv_urlpatterns = [
    path('categorias/', CategoriaView.as_view(), name='categoria_list'),
    path('categorias/new', CategoriaNew.as_view(), name='categoria_new'),
    path('categorias/edit/<int:pk>', CategoriaEdit.as_view(), name='categoria_edit'),
    path('categorias/delete/<int:pk>', CategoriaDel.as_view(), name='categoria_del'),

    path('subcategorias/', SubCategoriaView.as_view(), name='subcategoria_list'),
    path('subcategorias/new', SubCategoriaNew.as_view(), name='subcategoria_new'),
    path('subcategorias/edit/<int:pk>', SubCategoriaEdit.as_view(), name='subcategoria_edit'),
    path('subcategorias/delete/<int:pk>', SubCategoriaDel.as_view(), name='subcategoria_del'),

    path('marcas/', MarcaView.as_view(), name="marca_list"),
    path('marcas/new', MarcaNew.as_view(), name="marca_new"),
    path('marcas/edit/<int:pk>', MarcaEdit.as_view(), name="marca_edit"),
    path('marcas/inactivar/<int:id>', marca_inactivar, name="marca_inactivar"),

    path('um/', UMView.as_view(), name="um_list"),
    path('um/new', UMNew.as_view(), name="um_new"),
    path('um/edit/<int:pk>', UMEdit.as_view(), name="um_edit"),
    path('um/inactivar/<int:id>', um_inactivar, name="um_inactivar"),

    path('productos/', ProductoView.as_view(), name="producto_list"),
    path('productos/new', ProductoNew.as_view(), name="producto_new"),
    path('productos/edit/<int:pk>', ProductoEdit.as_view(), name="producto_edit"),
    path('productos/inactivar/<int:id>', producto_inactivar, name="producto_inactivar"),
]
