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
          Anúncios
        </q-toolbar-title>
        <div>
          <q-btn to="/login" flat color="white" label="Meu Perfil"
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
      <div class="q-pa-md" style="margin-top: 25px;">

        <div>
              <div class="row justify-center">
                <q-input style="width: 259px;" dense outlined v-model="text" label="Pesquisar mangá ou editora"/>
                <q-btn class="q-ml-md" color="primary" icon="fas fa-search" label="Pesquisar" />
              </div>
        </div>

          <div class="row justify-center">

            <div v-for="n in 24" :key="n">
              <q-card clickable class="col-3 col-md-2 bg-grey-3 q-ma-lg q-hoverable">
                <img src="public/chain.jpg" class="q-pa-md" style="height: 250px; width: 230px; border-radius: 20px;"/>
                <span class="q-focus-helper"></span>
                 <q-card-section>
                      <span class="text-subtitle2">TITULO DO ANUNCIO</span><br>
                      <div class="row justify-between">
                        <span class="text-subtitle2">R$14.90</span>
                        <div>
                            <q-btn icon="fa-solid fa-basket-shopping" flat round color="blue">
                            <q-tooltip class="bg-blue">
                              Adicionar produto ao carrinho
                            </q-tooltip>
                          </q-btn>
                          <q-btn
                            color="grey-9"
                            round
                            flat
                            dense
                            :icon="expanded ? 'fa-solid fa-angle-up' : 'fa-solid fa-angle-down'"
                            @click="expanded = !expanded"
                          />
                        </div>
                      </div>
                </q-card-section>
                <q-slide-transition>
                  <div v-show="expanded">
                    <q-separator />
                    <q-card-section class="text-subitle2">
                      Descrição do anúncio
                    </q-card-section>
                  </div>
                </q-slide-transition>
              </q-card>
            </div>
            </div>

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
    const busca = ref()
    const expanded = ref(false)

    return {
      essentialLinks: linksList,
      leftDrawerOpen,
      toggleLeftDrawer () {
        leftDrawerOpen.value = !leftDrawerOpen.value
      },
      nrItens,
      busca,
      expanded
    }
  }
})
</script>
