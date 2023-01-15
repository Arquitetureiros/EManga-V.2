<template>
  <div>
    <q-toolbar class="bg-primary">
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="$emit('leftDrawer')"
        />

        <q-toolbar-title class="bg-primary">
          Anúncios
        </q-toolbar-title>
        <q-btn icon="fa-solid fa-basket-shopping" flat color="white" @click="showCart = !showCart">
          <q-badge color="orange" floating> {{quantityOnCart}} </q-badge>
          <q-tooltip>
            Ver Carrinho
          </q-tooltip>
        </q-btn>
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
      <div class="float-right">
        <MarketCart v-if="showCart" :products="getProductsOnCart()"/>
      </div>
  </div>
</template>
<script>
import { ref } from 'vue'
export default {
  setup () {
    const showCart = ref(false)
    const quantityOnCart = ref(JSON.parse(localStorage.getItem('cartProducts')) ? JSON.parse(localStorage.getItem('cartProducts')).length : 0)

    function getQuantityOnCart () {
      quantityOnCart.value = JSON.parse(localStorage.getItem('cartProducts')).length
    }

    function getProductsOnCart () {
      console.log(localStorage.getItem('cartProducts'))
      return JSON.parse(localStorage.getItem('cartProducts'))
    }

    document.onstorage = () => {
      console.log(localStorage.getItem('cartProducts'))
      getQuantityOnCart()
    }

    // window.addEventlistener('storage', (event) => {
    //   console.log(localStorage.getItem(event.key))
    // })

    return { showCart, getProductsOnCart, quantityOnCart, getQuantityOnCart }
  }
}
</script>
