<template>
  <div>
    <p v-for="(product,p) in products" :key="p">
     {{product.name}}
    </p>
  </div>
</template>
<script>
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'MarketCart',
  props: {
    products: {
      type: Array
    }
  }
})
</script>
