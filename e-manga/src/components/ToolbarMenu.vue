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
        <MarketCart :seamless="showCart"/>
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
  </div>
</template>
<script>
import MarketCart from 'components/MarketCart.vue'

export default {
  components: {
    MarketCart
  },
  setup () {
    // window.addEventlistener('storage', (event) => {
    //   console.log(localStorage.getItem(event.key))
    // })

    return { }
  }
}
</script>
