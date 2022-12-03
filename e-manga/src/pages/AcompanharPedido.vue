<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar class="bg-primary">
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"
        />

        <q-toolbar-title class="bg-primary">
          Acompanhar Pedido
        </q-toolbar-title>
        <div>
          <q-btn flat color="white" label="Meu perfil"
          size="13px"
          />
        </div>
        <div>
          <q-btn round>
            <q-avatar size="42px">
              <img src="public/avatar.png">
            </q-avatar>
          </q-btn>
        </div>
      </q-toolbar>
    </q-header>

    <q-page-container>
      <h4 style="text-align: center;">Meus pedidos</h4>
      <q-card class="my-card">
        <q-card-section>
          <div class="row justify-between items-stretch">
            <div class="row items-center" style="width: 80%;">
              <div style="width: 20%;" class="flex justify-center">
                <img src="hunterxhunter.jpg" style="height: 140px;">
              </div>
              <div style="width: 60%; height: 100%;" class="flex column">
                <div style="height: 50%;" class="flex justify-start">
                  <h6>Hunter x Hunter vol. 1</h6>
                </div>
                <div style="width: 50%; height: 50%;" class="flex justify-start items-center">
                  <p>Vendido por Yuripa Mangás</p>
                  <p>Produto entregue em 09/10/2022</p>
                </div>
              </div>
            </div>
            <div style="width: 20%;" class="flex justify-center items-center">
              <h6>Avaliar Vendedor</h6>
              <q-rating size="2rem" v-model="ratingModel" :max="5" color="yellow" />
            </div>
          </div>
        </q-card-section>
      </q-card>
      <q-card class="my-card">
        <q-card-section>
          <div class="row justify-between items-stretch">
            <div class="row items-center" style="width: 80%;">
              <div style="width: 20%;" class="flex justify-center">
                <img src="jujutsu-kaisen.jpg" style="height: 140px;">
              </div>
              <div style="width: 60%; height: 100%;" class="flex column">
                <div style="height: 50%;" class="flex justify-start">
                  <h6>Jujutsu Kaisen vol. 1</h6>
                </div>
                <div style="width: auto; height: auto;" class="flex column justify-between items-start">
                  <p>Vendido por Yuripa Mangás</p>
                  <p>Produto em trânsito</p>
                </div>
              </div>
            </div>
            <div style="width: 20%;" class="flex justify-center items-center">
              <h6>Avaliar Vendedor</h6>
              <p style="text-align: center;">Avaliação disponível após a entrega ser efetuada</p>
            </div>
          </div>
        </q-card-section>
      </q-card>
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
          v-for="link in essentialLinks"
          :key="link.title"
          v-bind="link"
        />

      </q-list>
    </q-drawer>
  </q-layout>
</template>

<script>
import { defineComponent, ref } from 'vue'
import EssentialLink from 'components/EssentialLink.vue'

const linksList = [
  {
    title: 'Início',
    icon: 'school',
    link: '#'
  },
  {
    title: 'Criar Anuncio',
    icon: 'chat',
    link: '#/manterManga'
  },
  {
    title: 'Carrinho/Pagamento',
    icon: 'receipt',
    link: '#/pagamentos'
  },
  {
    title: 'Meus Pedidos',
    icon: 'record_voice_over',
    link: '#/acompanharpedido'
  },
  {
    title: 'Meus Produtos',
    icon: 'favorite',
    link: '#/meusProdutos'
  }
]

export default defineComponent({
  name: 'MainLayout',

  components: {
    EssentialLink
  },

  setup () {
    const leftDrawerOpen = ref(false)
    return {
      essentialLinks: linksList,
      leftDrawerOpen,
      toggleLeftDrawer () {
        leftDrawerOpen.value = !leftDrawerOpen.value
      }
    }
  }
})
</script>
