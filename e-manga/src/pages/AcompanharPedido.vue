<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <ToolbarMenu @leftDrawer="toggleLeftDrawer"/>
    </q-header>

    <q-page-container>
      <h4 style="text-align: center;">Meus pedidos</h4>
      <q-card class="my-card" v-for="pedido in this.pedidos">
        <q-card-section class="row" style="width: 100%">
          <span style="width: 20%; text-align: center;">{{pedido.id}}</span>
          <span v-if="pedido.entregue" style="width: 60%; text-align: center;">Produto entregue em <br> {{pedido.dh_pedido}}</span>
          <span v-if="!pedido.entregue" style="width: 60%; text-align: center;">Produto em Transito</span>
          <q-btn flat @click="ToggleItensPedido(pedido.id)" style="width: 20%">Itens</q-btn>
        </q-card-section>
      </q-card>

      <q-dialog v-model="itensPedido">
      <q-card style="width: 30%;">
        <q-card-section>
          <div class="text-h6">Itens do Pedido: </div>
        </q-card-section>

        <q-card-section class="q-pt-none row" v-for="item in this.itens" style="width: 100%;">
          <img :src="item.fotoCaminho" style="width: 50%;">
          <q-card class="column" style="width: 50%; justify-content: center; align-items: end;">
            <div style="margin: 20px;">Vendido por: <br>{{ item.usuario }}</div>
            <div style="margin: 20px;">Quantidade: {{ item.qt_pedido }}</div>
            <div style="margin: 20px;">Valor Total: {{ item.vl_total }}</div>
          </q-card>
        </q-card-section>

        <q-card-actions>
          <q-btn style="width: 100%; padding: 0;" label="Fechar" color="red" v-close-popup @click="SalvarCartao"/>
        </q-card-actions>
      </q-card>
    </q-dialog>
    </q-page-container>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
    >
      <q-list>
        <q-item-label
          header
        >
        Opções
        </q-item-label>

        <EssentialLink
        />

      </q-list>
    </q-drawer>
  </q-layout>
</template>

<script>
import { defineComponent, ref } from 'vue'
import ToolbarMenu from 'components/ToolbarMenu.vue'
import EssentialLink from 'components/EssentialLink.vue'

import PedidoDataService from 'src/services/PedidoDataService'
import ItemPedidoDataService from 'src/services/ItemPedidoDataService'
import MangaDataService from 'src/services/MangaDataService'

import jwtDecode from 'jwt-decode';
import UsuarioDataService from 'src/services/UsuarioDataService'

export default defineComponent({
  name: 'MainLayout',

  components: {
    EssentialLink,
    ToolbarMenu
  },

  setup () {
    const leftDrawerOpen = ref(false)
    return {
      leftDrawerOpen,
      toggleLeftDrawer () {
        leftDrawerOpen.value = !leftDrawerOpen.value
      }
    }
  },
  data ()
  {
    return {
      pedidos: [],
      itensPedido: false,
      itens: []
    }
  },
  methods: {
    ListarPedidos()
    {
      const token = localStorage.getItem('jwt');
      if(!token) { return; }

      const decodedToken = jwtDecode(token);

      PedidoDataService.listarPorUsuario(decodedToken['user_id'])
        .then((response) => {
          this.pedidos = response.data
        })
    },
    ListarItensPedido(id)
    {
      ItemPedidoDataService.listar()
      .then((response) => {
          console.log(response.data)
        })
    },
    ListarManga(id)
    {
      MangaDataService.listar()
      .then((response) => {
          console.log(response.data)
        })
    },
    ToggleItensPedido(id)
    {
      ItemPedidoDataService.listarPorPedido(id)
        .then((response) => {
          this.itens = response.data;
          
          for(let item of this.itens)
          {
            console.log(item)
            MangaDataService.obter(item.manga)
              .then((response) => {
                item.fotoCaminho = response.data.fotoCaminho;
                UsuarioDataService.obter(response.data.user_id)
                  .then((response) => {
                      item.usuario = response.data.nome;
                  })
              })
          }
        })

      this.itensPedido = !this.itensPedido
    }
  },
  mounted()
  {
    this.ListarPedidos()
    this.ListarItensPedido()
    this.ListarManga()
  }
})
</script>
