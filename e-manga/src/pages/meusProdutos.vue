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
                <q-input style="width: 259px;" dense outlined v-model="text" label="Pesquisar seu anúncio"/>
                <q-btn class="q-ml-md" color="primary" icon="fas fa-search" label="Pesquisar" />
              </div>
        </div>

          <div class="row justify-start">

            <div v-for="(product, p) in products" :key="p">
              <q-card id="my-card"  class="col-3 col-md-2 bg-grey-3 q-ma-lg q-hoverable">
                <div v-ripple to="/verManga" class="cursor-pointer relative-position">
                  <img :src=product.url_image class="q-pa-md" style="height: 250px; width: 230px; border-radius: 20px;"/>
                  <span class="q-focus-helper"></span>
                </div>
                 <q-card-section>
                      <span class="text-subtitle2"> {{product.name}} </span><br>
                      <div class="row justify-between">
                        <span class="text-subtitle2 text-green-14" ></span>
                        <div>
                          <q-btn
                            color="grey-8"
                            round
                            flat
                            dense
                            icon="fa-solid fa-pencil"
                            to="/editarManga"
                          >
                            <q-tooltip>
                              Editar mangá
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
    const $router = useQuasar()
    const products = ref(
      [{
      }
      ])
    const inCart = ref([])
    const showCart = ref(false)
    function acessarAnuncio () {
      $router.replace('/verManga')
    }

    function addToCart (product) {
      inCart.value.push(product)
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
      $router,
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
