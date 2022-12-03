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
          Busca Produto
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
      <div class="q-pa-md" style="margin-top: 25px;">

        <div class="row" style="display:flex; justify-content: space-between;">
          <div class="col">
            <span class="text-h5" style="margin-left: 35px;">Buscar por "Chainsaw man"</span>
          </div>
          <div class="col" >
            <div class="row" style="display: flex; align-items: center; gap: 8px; justify-content: flex-end; padding-right: 99px;">
              <div>
              <q-input  outlined v-model="text" label="Pesquisar mangá..." />
              </div>
            <div>
              <q-btn color="primary"  label="Pesquisar" />
            </div>
            </div>
          </div>
        </div>

          <div class="row" style="margin-top: 70px; margin-left: 35px;">
            <div class="col" id="card">
              <img src="public/chain.jpg" style="height: 230px; width: 100%; object-fit: cover;">
              <div class="row" style="display:flex; align-items: center">
                <div class="col">
                  <q-btn color="primary" label="Ver" style="margin-left: 10px; border-radius:7px"/>
                </div>
                <div class="col">
                  <h6 style="margin: 10px 0">R$14.90</h6>
                </div>
              </div>
            </div>

            <div class="col" id="card">
              <img src="public/chainsaw.jpg" style="height: 230px; width: 100%; object-fit: cover;">
              <div class="row" style="display:flex; align-items: center">
                <div class="col">
                  <q-btn color="primary" label="Ver" style="margin-left: 10px; border-radius:7px"/>
                </div>
                <div class="col">
                  <h6 style="margin: 10px 0">R$14.90</h6>
                </div>
              </div>
            </div>

            <div class="col" id="card">
              <img src="public/chain.jpg" style="height: 230px; width: 100%; object-fit: cover;">
              <div class="row" style="display:flex; align-items: center">
                <div class="col">
                  <q-btn color="primary" label="Ver" style="margin-left: 10px; border-radius:7px"/>
                </div>
                <div class="col">
                  <h6 style="margin: 10px 0">R$14.90</h6>
                </div>
              </div>
            </div>

            <div class="col" id="card">
              <img src="public/chainsaw.jpg" style="height: 230px; width: 100%; object-fit: cover;">
              <div class="row" style="display:flex; align-items: center">
                <div class="col">
                  <q-btn color="primary" label="Ver" style="margin-left: 10px; border-radius:7px"/>
                </div>
                <div class="col">
                  <h6 style="margin: 10px 0">R$14.90</h6>
                </div>
              </div>
            </div>

            <div class="col" id="card">
              <img src="public/chain.jpg" style="height: 230px; width: 100%; object-fit: cover;">
              <div class="row" style="display:flex; align-items: center">
                <div class="col">
                  <q-btn color="primary" label="Ver" style="margin-left: 10px; border-radius:7px"/>
                </div>
                <div class="col">
                  <h6 style="margin: 10px 0">R$14.90</h6>
                </div>
              </div>
            </div>

            <div class="col" id="card">
              <img src="public/chainsaw.jpg" style="height: 230px; width: 100%; object-fit: cover;">
              <div class="row" style="display:flex; align-items: center">
                <div class="col">
                  <q-btn color="primary" label="Ver" style="margin-left: 10px; border-radius:7px"/>
                </div>
                <div class="col">
                  <h6 style="margin: 10px 0">R$14.90</h6>
                </div>
              </div>
            </div>

            <div class="col" id="card">
              <img src="public/chain.jpg" style="height: 230px; width: 100%; object-fit: cover;">
              <div class="row" style="display:flex; align-items: center">
                <div class="col">
                  <q-btn color="primary" label="Ver" style="margin-left: 10px; border-radius:7px"/>
                </div>
                <div class="col">
                  <h6 style="margin: 10px 0">R$14.90</h6>
                </div>
              </div>
            </div>
          </div>

          <div class="row" style="margin-top: 70px; margin-left: 35px;">
            <div class="col" id="card">
              <img src="public/chainsaw.jpg" style="height: 230px; width: 100%; object-fit: cover;">
              <div class="row" style="display:flex; align-items: center">
                <div class="col">
                  <q-btn color="primary" label="Ver" style="margin-left: 10px; border-radius:7px"/>
                </div>
                <div class="col">
                  <h6 style="margin: 10px 0">R$14.90</h6>
                </div>
              </div>
            </div>
            <div class="col" id="card">
              <img src="public/chain.jpg" style="height: 230px; width: 100%; object-fit: cover;">
              <div class="row" style="display:flex; align-items: center">
                <div class="col">
                  <q-btn color="primary" label="Ver" style="margin-left: 10px; border-radius:7px"/>
                </div>
                <div class="col">
                  <h6 style="margin: 10px 0">R$14.90</h6>
                </div>
              </div>
            </div>
            <div class="col" id="card">
              <img src="public/chainsaw.jpg" style="height: 230px; width: 100%; object-fit: cover;">
              <div class="row" style="display:flex; align-items: center">
                <div class="col">
                  <q-btn color="primary" label="Ver" style="margin-left: 10px; border-radius:7px"/>
                </div>
                <div class="col">
                  <h6 style="margin: 10px 0">R$14.90</h6>
                </div>
              </div>
            </div>
            <div class="col" id="card">
              <img src="public/chain.jpg" style="height: 230px; width: 100%; object-fit: cover;">
              <div class="row" style="display:flex; align-items: center">
                <div class="col">
                  <q-btn color="primary" label="Ver" style="margin-left: 10px; border-radius:7px"/>
                </div>
                <div class="col">
                  <h6 style="margin: 10px 0">R$14.90</h6>
                </div>
              </div>
            </div>
            <div class="col" id="card">
              <img src="public/chainsaw.jpg" style="height: 230px; width: 100%; object-fit: cover;">
              <div class="row" style="display:flex; align-items: center">
                <div class="col">
                  <q-btn color="primary" label="Ver" style="margin-left: 10px; border-radius:7px"/>
                </div>
                <div class="col">
                  <h6 style="margin: 10px 0">R$14.90</h6>
                </div>
              </div>
            </div>
            <div class="col" id="card">
              <img src="public/chain.jpg" style="height: 230px; width: 100%; object-fit: cover;">
              <div class="row" style="display:flex; align-items: center">
                <div class="col">
                  <q-btn color="primary" label="Ver" style="margin-left: 10px; border-radius:7px"/>
                </div>
                <div class="col">
                  <h6 style="margin: 10px 0">R$14.90</h6>
                </div>
              </div>
            </div>
            <div class="col" id="card">
              <img src="public/chainsaw.jpg" style="height: 230px; width: 100%; object-fit: cover;">
              <div class="row" style="display:flex; align-items: center">
                <div class="col">
                  <q-btn color="primary" label="Ver" style="margin-left: 10px; border-radius:7px"/>
                </div>
                <div class="col">
                  <h6 style="margin: 10px 0">R$14.90</h6>
                </div>
              </div>
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

    return {
      essentialLinks: linksList,
      leftDrawerOpen,
      toggleLeftDrawer () {
        leftDrawerOpen.value = !leftDrawerOpen.value
      },
      nrItens,
      busca
    }
  }
})
</script>
