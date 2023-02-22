<template>
  <div class="q-pa-md q-gutter-sm">
    <q-btn icon="fa-solid fa-basket-shopping" flat color="white" @click="seamless = !seamless; getProductsOnCart()">
      <q-badge color="orange" floating> {{quantityOnCart}} </q-badge>
      <q-tooltip>
        Ver Carrinho
      </q-tooltip>
    </q-btn>
    <q-dialog v-model="seamless" seamless position="right">
      <q-card style="width: 350px">
        <q-linear-progress :value="1" color="primary" />
        <div class="row">
          <q-btn class="col-2 self-end" flat @click="seamless = !seamless" icon="fa-regular fa-x" color="primary"></q-btn>
        </div>
        <q-card-section class="row items-center">
          <div class="row q-py-sm" v-for="(product, p) in products" :key="p">
            <div class="col-9">
              <q-img :src="product.url_image" style="height: 200px; width: 150px"/>
              <div class="text-weight-bold">{{product.name}}</div>
              <div class="text-green">R$ {{product.price}}</div>
            </div>
            <div class="col-3">
              <q-btn flat color="primary" icon="fa-solid fa-trash" @click="removeProduct(product)">
              </q-btn>
            </div>
            <div class="col-12">

            <hr/>
            </div>
            <!-- <div class="text-grey">{{product}}</div> -->
          </div>
        </q-card-section>
      </q-card>
    </q-dialog>
  </div>
</template>
<script>
import { defineComponent, ref } from 'vue'
export default defineComponent({
  name: 'MarketCart',

  setup () {
    const seamless = ref(false)
    const products = ref([])
    const quantityOnCart = ref(JSON.parse(localStorage.getItem('cartProducts')) ? JSON.parse(localStorage.getItem('cartProducts')).length : 0)

    function getProductsOnCart () {
      products.value = JSON.parse(localStorage.getItem('cartProducts'))
    }

    function removeProduct (product) {
      products.value.pop(products.value.indexOf(product))
      localStorage.setItem('cartProducts', JSON.stringify(products.value))
      getProductsOnCart()
    }

    return {
      seamless,
      products,
      quantityOnCart,
      removeProduct,
      getProductsOnCart
    }
  }
})
</script>
