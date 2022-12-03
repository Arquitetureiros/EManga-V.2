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
          e-Manga
        </q-toolbar-title>
        <div>
          <q-btn to="/login" flat color="white" label="Entrar/Cadastrar"
          size="13px"
          />
        </div>
        <div>
          <q-btn round>
            <q-avatar size="42px">
              <img src="public/blankicon.jpeg">
            </q-avatar>
          </q-btn>
        </div>
      </q-toolbar>
    </q-header>

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
    <div class="q-pa-md">
      <q-page-container>
        <q-img src="https://d5y9g7a5.rocketcdn.me/wp-content/uploads/2020/08/manga-o-que-e-historia-principais-caracteristicas-e-tipos-1024x576.png"
        alt="carequinha"
        style="height: 400px; width: 400px"
        />
      </q-page-container>
    </div>
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
