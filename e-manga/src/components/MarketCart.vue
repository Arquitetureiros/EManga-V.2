<template>
  <div class="q-pa-md q-gutter-sm">
    <q-btn icon="fa-solid fa-basket-shopping" flat color="white" @click="seamless = !seamless; getProductsOnCart()">
      <q-badge color="orange" floating> {{products.length}} </q-badge>
      <q-tooltip>
        Ver Carrinho
      </q-tooltip>
    </q-btn>
    <q-dialog v-model="seamless" seamless position="right">
      <q-card style="width: 350px">
        <q-linear-progress :value="1" color="primary" />
        <div class="row justify-between">
          <div class='col-4 q-px-md q-py-sm text-h6 text-primary'>
            <span> Carrinho </span>
          </div>
          <div class="col-2">
            <q-btn flat @click="seamless = !seamless" icon="fa-regular fa-x" color="primary"></q-btn>
          </div>
        </div>
        <q-card-section class="row items-center">
          <div v-if="products.length == 0" class="text-grey">Vazio</div>
          <div class="row q-py-sm" v-else v-for="(product, p) in products" :key="p">
            <div class="col-9 rounded-borders q-pl-md">
              <q-img :src="product.url_image" style="height: 200px; width: 150px; border-radius: 5px;"/>
              <div class="text-weight-bold">{{product.name}}</div>
              <!-- <span> {{ product.quantity }}</span> -->
              <div class="text-green">R$ {{product.price}}</div>
            </div>
            <div class="col-3 q-pb-sm">
              <q-btn flat color="primary" icon="fa-solid fa-trash" @click="removeProduct(p)">
                <q-tooltip class="bg-primary text-white">Remover produto</q-tooltip>
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
import { defineComponent, onMounted, ref } from 'vue'
export default defineComponent({
  name: 'MarketCart',

  setup () {
    const seamless = ref(false)
    const products = ref([])
    const quantityOnCart = ref()

    function getProductsOnCart () {
      if(localStorage.getItem('cartProducts')) {
        products.value = JSON.parse(localStorage.getItem('cartProducts'))
      }

    }

    function removeProduct (index) {
      products.value.splice(index, 1)
      localStorage.setItem('cartProducts', JSON.stringify(products.value))
      getProductsOnCart()
    }

    onMounted(() => {
      getProductsOnCart()
    })

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
