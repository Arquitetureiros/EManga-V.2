<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <ToolbarMenu @leftDrawer="toggleLeftDrawer"/>
    </q-header>

    <q-page-container>
      <div class="q-pa-md" style="margin-top: 25px;">
        <div class="float-right">
          <MarketCart v-if="showCart" :products="getProductsOnCart()"/>
        </div>
        <div>
              <div class="row justify-center">
                <q-input style="width: 259px;" dense outlined v-model="text" label="Pesquisar mangá"/>
                <q-btn class="q-ml-md" color="primary" icon="fas fa-search" label="Pesquisar" />
              </div>
        </div>

          <div class="row justify-start">

            <div v-for="(product, p) in products" :key="p">
              <q-card id="my-card"  class="col-3 col-md-2 bg-grey-3 q-ma-lg q-hoverable">
                <div v-ripple @click="acessarAnuncio" class="cursor-pointer relative-position">
                  <img :src=product.url_image class="q-pa-md" style="height: 250px; width: 230px; border-radius: 20px;"/>
                  <span class="q-focus-helper"></span>
                </div>
                 <q-card-section>
                      <span class="text-subtitle2"> {{product.name}} </span><br>
                      <span class="text-subtitle3 text-grey" >{{ product.owner }} </span>
                      <div class="row justify-between">
                        <span class="text-subtitle2 text-green-14" >R$ {{ product.price }} </span>
                        <div>
                          <q-btn
                            color="grey-8"
                            round
                            flat
                            dense
                            icon="fa-solid fa-location-dot"
                            @click="expanded[p] = !expanded[p]"
                          >
                            <q-tooltip>
                              Localização
                            </q-tooltip>
                          </q-btn>
                            <q-btn icon="fa-solid fa-basket-shopping" @click="addToCart(product)" flat round color="blue">
                            <q-tooltip class="bg-blue">
                              Adicionar produto ao carrinho
                            </q-tooltip>
                          </q-btn>
                        </div>
                      </div>
                </q-card-section>
                <q-slide-transition>
                  <div v-show="expanded[p]">
                    <q-separator />
                    <q-card-section class="text-subitle2">
                     {{product.city}} - {{product.cd_uf}}
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

        <EssentialLink/>

      </q-list>
    </q-drawer>
  </q-layout>
</template>
<script>
import { useQuasar } from 'quasar'
import { defineComponent, ref } from 'vue'
import MarketCart from 'components/MarketCart.vue'
import EssentialLink from 'components/EssentialLink.vue'
import ToolbarMenu from 'components/ToolbarMenu.vue'

export default defineComponent({
  name: 'MainLayout',

  components: {
    EssentialLink,
    MarketCart,
    ToolbarMenu
  },

  setup () {
    const leftDrawerOpen = ref(false)
    const nrItens = ref(1)
    const busca = ref()
    const expanded = ref([])
    const $q = useQuasar()
    const products = ref(
      [{
        id: 1,
        name: 'Chainsaw Man vol.1',
        city: 'Maringá',
        cd_uf: 'PR',
        price: '14.25',
        url_image: 'public/chain.jpg',
        owner: 'Yuripa Mangás'
      }, {
        id: 2,
        name: 'Chainsaw Man vol.10',
        city: 'São Paulo',
        cd_uf: 'SP',
        price: '20.50',
        url_image: 'public/chainsaw.jpg',
        owner: 'Valentas'
      }, {
        id: 3,
        name: 'Chainsaw Man vol.9',
        city: 'Maringá',
        cd_uf: 'PR',
        price: '17.25',
        url_image: 'public/chainsa-vol-9.jpg',
        owner: 'Valentas'
      }, {
        id: 4,
        name: 'Jujutsu Kaisen vol.10',
        city: 'São Paulo',
        cd_uf: 'SP',
        price: '27.50',
        url_image: 'public/chainsaw.jpg',
        owner: 'Valentas'
      }, {
        id: 5,
        name: 'Chainsaw Man vol.1',
        city: 'Maringá',
        cd_uf: 'PR',
        price: '10.25',
        url_image: 'public/chain.jpg',
        owner: 'Valentas'
      }
      ])
    const inCart = ref([])
    const showCart = ref(false)

    function acessarAnuncio () {
      $q.notify(
        this.$router.push('/verManga')
      )
    }

    function addToCart (product) {
      inCart.value = JSON.parse(localStorage.getItem('cartProducts'))
      inCart.value.push(product)
      product.inOrder = true
      localStorage.setItem('cartProducts', JSON.stringify(inCart.value))
    }

    function toggleLeftDrawer () {
      leftDrawerOpen.value = !leftDrawerOpen.value
    }

    function getProductsOnCart () {
      console.log(JSON.parse(localStorage.getItem('cartProducts')))
      return JSON.parse(localStorage.getItem('cartProducts'))
    }

    return {
      MarketCart,
      nrItens,
      busca,
      expanded,
      acessarAnuncio,
      $q,
      addToCart,
      products,
      inCart,
      getProductsOnCart,
      showCart,
      leftDrawerOpen,
      toggleLeftDrawer
    }
  }
})
</script>
