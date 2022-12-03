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
          Pagamento
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
      <div class="q-pa-xl">
      <div>
        <div class="text-h4">
          Meu carrinho
        </div>
        <div class="q-pa-md">
          Quantidade de itens: {{nrItens}}
        </div>

        <div>
          <div class="row justify-between">
            <div class="row">
            <div>
            <q-checkbox v-model="val"/>
              <q-img
              :src="img"
              style="height: 200px; width: 150px"
              >
              <div class="absolute-bottom text-subtitle1 text-center"> Vol. 1 </div>
              </q-img>
              </div>
              <div class="q-pl-md">
                <span class="text-h6">{{item}}</span>
                <p class="text-subtitle1" style="opacity: 0.7"> Vendido por: {{ vendedor }}</p>
                <div class="row q-pt-xl">
                  <div class="col">
                    <q-input
                    v-model.number="qtd"
                    dense
                    type="number"
                    outlined
                    style="max-width: 200px; max-height: 10px"
                    label="Quantidade:"
                    />
                  </div>
                  <div class ="row q-pl-md">
                    <div>
                      <span>Valor unitário: </span>
                      <span class="text-positive">R${{valor}}</span><br>
                      <span>Valor total: </span>
                      <span class="text-positive">R${{valor*qtd}}</span>
                    </div>
                    <div>
                      <q-btn
                      flat
                      round
                      icon="fas fa-trash"
                      color="primary">
                      <q-tooltip class="bg-primary">Excluir item</q-tooltip>
                      </q-btn>
                    </div>
                  </div>
                </div>
              </div>
              </div>
              <div class="q-pl-xl">
                <div class="text-h6">Endereço de Envio:
                <q-card class="my-card">
                    <q-card-section class="text-body1">
                      Rua dos Bobos, 0, Formiga - Minas Gerais<br>
                      CEP 42069-123
                      <q-btn flat dense color="primary" icon="edit">
                        <q-tooltip>Editar</q-tooltip>
                      </q-btn>
                    </q-card-section>
                </q-card>
              </div>
          <div class="q-pt-md">
            <p class="text-h6">Opções de Frete:</p>
            <q-radio v-model="opFrete" val=8.00 label="PAC" color="green" /> <span class="text-positive">- R$8,00</span><br>
            <q-radio v-model="opFrete" val=18.00 label="SEDEX" color="green" /> <span class="text-positive">- R$18,00</span>
          </div>
          <div class="text-h6">Total: <span class="text-positive">R$ {{total()}}</span></div>
        </div>
          </div>
            <div class="q-pa-md">
            <span class="text-h5"> Forma de Pagamento:</span>
            <div class="row">
              <q-tabs
              v-model="tab"
              class="text-primary"
              >
              <q-tab name="card" icon="fa-solid fa-credit-card" label="Cartão" />
              <q-tab name="boleto" icon="fa-solid fa-barcode" label="Boleto" />
              <q-tab name="pix" icon="fa-solid fa-qrcode" label="Pix" />
              </q-tabs>
            </div>
              <div v-if="tab == 'pix'">
                <div class="text-h6">
                  Pix
                </div>
                <div class="q-pr-xs">
                  <q-img src="public/qrcode_pix.png" style="height: 250px; width: 250px;"/>
                </div>
                <span>Escaneie o QR Code para realizar o pagamento</span>
              </div>
              <div v-if="tab == 'card'">
                <div class="text-h6">
                  Cartão
                </div>
              </div>
              <div v-if="tab == 'boleto'">
                <div class="text-h6">
                  Boleto
                </div>
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
    const nrItens = ref(1)
    const img = ref('https://images-na.ssl-images-amazon.com/images/I/71bELfIWTDL.jpg')
    const item = ref('My Hero Academia Vol. 1')
    const val = ref(true)
    const vendedor = ref('Valentas Mangas Express')
    const qtd = ref(1)
    const valor = ref(14.90)
    const tab = ref('card')
    const opFrete = ref(0)

    function total () {
      const vltotal = ((valor.value * qtd.value) + parseFloat(opFrete.value))
      return vltotal
    }

    return {
      essentialLinks: linksList,
      leftDrawerOpen,
      toggleLeftDrawer () {
        leftDrawerOpen.value = !leftDrawerOpen.value
      },
      nrItens,
      img,
      item,
      val,
      vendedor,
      qtd,
      valor,
      tab,
      opFrete,
      total
    }
  }
})
</script>
