from django.urls import include, re_path
from emanga import views

urlpatterns = [
    re_path(r'^usuario$', views.usuarioApi, name="usuario"),
    re_path(r'^usuario/([0-9]+)$', views.usuarioApi, name='usuario_byid'),
    
    re_path(r'^endereco$', views.enderecoApi, name="endereco"),
    re_path(r'^endereco/([0-9]+)$', views.enderecoApi),
    re_path(r'^endereco/usuario/([0-9]+)$', views.enderecoApi),

    re_path(r'^cartao$', views.cartaoApi, name="cartao"),
    re_path(r'^cartao/([0-9]+)$', views.cartaoApi),
    re_path(r'^cartao/usuario/([0-9]+)$', views.cartaoApi),
    
    re_path(r'^manga$', views.mangaApi),
    re_path(r'^manga/([0-9]+)$', views.mangaApi),
    re_path(r'^manga/usuario/([0-9]+)$', views.mangaApi),

    re_path(r'^pedido$', views.pedidoApi, name="pedido"),
    re_path(r'^pedido/([0-9]+)$', views.pedidoApi),
    re_path(r'^pedido/usuario/([0-9]+)$', views.pedidoApi),

    re_path(r'^itempedido$', views.itempedidoApi),
    re_path(r'^itempedido/([0-9]+)$', views.itempedidoApi),
    re_path(r'^itempedido/pedido/([0-9]+)$', views.itempedidoApi)
]