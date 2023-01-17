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
          Editar Perfil
        </q-toolbar-title>
        <div>
          <q-btn flat color="white" label="Entrar/Cadastrar"
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

    <q-page-container class="flex justify-center">

    <div class="column justify-center">
      <div style="width: 100%;" class="row justify-center">
        <q-avatar size="100px">
          <img src="public/avatar.png">
        </q-avatar>
      </div>

      <form action="">
        <q-input ref="" outlined v-model="name" label="Nome" :dense="dense" lazy-rules :rules="nameRules" />

        <div class="row">
          <q-input ref="" outlined v-model="name" label="Cep" :dense="dense" lazy-rules :rules="nameRules" />

          <q-input ref="" outlined v-model="name" label="Num" :dense="dense" lazy-rules :rules="nameRules"/>
        </div>

        <q-input ref="" outlined v-model="name" label="Logradouro" :dense="dense" lazy-rules :rules="nameRules" />

        <div class="row">
          <q-input ref="" outlined v-model="name" label="Cidade" :dense="dense" lazy-rules :rules="nameRules" />

          <q-input ref="" outlined v-model="name" label="UF" :dense="dense" lazy-rules :rules="nameRules" />
        </div>
        <div class="row content-center">
          <q-icon name="font_download" size="25px" color="green"/>
          Novo Endereço
        </div>

        <q-card class="my-card">
          <q-card-section class="row justify-between">
            <div class="text-h6">Meus Cartões</div>
            <div class="text-subtitle2">
              <q-icon name="font_download" size="25px" color="green"/>
              Novo Cartão
            </div>
          </q-card-section>

          <q-separator />

          <q-card-actions vertical>
            <div class="row">
              <q-icon name="font_download" size="25px" color="green"/>
              <q-btn flat>Cartao 1</q-btn>
              <p>****</p>
              <q-icon name="font_download" size="25px" color="green"/>
            </div>
            <div class="row">
              <q-icon name="font_download" size="25px" color="green"/>
              <q-btn flat>Cartao 2</q-btn>
              <p>****</p>
              <q-icon name="font_download" size="25px" color="green"/>
            </div>
          </q-card-actions>
        </q-card>

        <q-btn label="Salvar Perfil" color="positive"/>
      </form>
    </div>
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
    link: 'https://quasar.dev'
  },
  {
    title: 'Pedidos',
    icon: 'code',
    link: 'https://github.com/quasarframework'
  },
  {
    title: 'Criar anúncio',
    icon: 'chat',
    link: 'https://chat.quasar.dev'
  },
  {
    title: 'Minhas vendas',
    icon: 'record_voice_over',
    link: 'https://forum.quasar.dev'
  },
  {
    title: 'Meus produtos',
    icon: 'rss_feed',
    link: 'https://twitter.quasar.dev'
  },
  {
    title: 'Carrinho',
    icon: 'public',
    link: 'https://facebook.quasar.dev'
  },
  {
    title: 'Meu perfil',
    icon: 'favorite',
    link: 'https://awesome.quasar.dev'
  },
  {
    title: 'Pagamentos',
    icon: 'receipt',
    link: 'localhost:9000/#/'
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
