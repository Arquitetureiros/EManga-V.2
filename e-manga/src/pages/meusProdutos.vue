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
          Meus produtos
        </q-toolbar-title>
        <div>
          <q-btn to="/login" flat color="white" label="Entrar/Cadastrar"
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
      <h4 style="text-align: center;">Meus produtos</h4>
      <div class="flex justify-around">
        <q-card class="my-card" style="width: 49%;">
          <q-card-section>
            <div class="row justify-between items-stretch">
              <div class="row items-center" style="width: 80%;">
                <div style="width: 20%;" class="flex justify-center">
                  <img src="public/chain.jpg" style="height: 140px;">
                </div>
                <div style="width: 60%; height: 100%;" class="flex column">
                  <div style="height: 50%;" class="flex justify-start">
                    <h6>Chainsaw man vol. 1</h6>
                  </div>
                </div>
              </div>
              <div style="width: 20%;" class="flex justify-center items-center">
                <q-btn to="/manterManga" color="primary" label="Editar"/>
              </div>
            </div>
          </q-card-section>
        </q-card>
        <q-card class="my-card" style="width: 49%;">
          <q-card-section>
            <div class="row justify-between items-stretch">
              <div class="row items-center" style="width: 80%;">
                <div style="width: 20%;" class="flex justify-center">
                  <img src="public/frieren.jpg" style="height: 140px;">
                </div>
                <div style="width: 60%; height: 100%;" class="flex column">
                  <div style="height: 50%;" class="flex justify-start">
                    <h6>Sousou no Frieren vol. 1</h6>
                  </div>
                </div>
              </div>
              <div style="width: 20%;" class="flex justify-center items-center">
                <q-btn to="/manterManga" color="primary" label="Editar"/>
              </div>
            </div>
          </q-card-section>
        </q-card>
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
    link: '#/buscar'
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
    const nrItens = ref(1)
    const titulo = ref()
    const desc = ref()
    const quant = ref(1)
    const imagem = ref()
    const imagem1 = ref()
    const imagem2 = ref()
    const imagem3 = ref()
    const imagem4 = ref()

    return {
      essentialLinks: linksList,
      leftDrawerOpen,
      toggleLeftDrawer () {
        leftDrawerOpen.value = !leftDrawerOpen.value
      },
      nrItens,
      titulo,
      desc,
      quant,
      imagem,
      imagem1,
      imagem2,
      imagem3,
      imagem4
    }
  }
})
</script>
