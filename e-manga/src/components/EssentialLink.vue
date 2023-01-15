<template>
  <q-item
  v-for="(link,l) in linksList" :key="l"
    clickable
    tag="a"
    :href="link.link"
  >
    <q-item-section
      v-if="link.icon"
      avatar
    >
      <q-icon :name="link.icon" />
    </q-item-section>

    <q-item-section>
      <q-item-label>{{ link.title }}</q-item-label>
      <q-item-label caption>{{ link.caption }}</q-item-label>
    </q-item-section>
  </q-item>
</template>

<script>
import { defineComponent, ref } from 'vue'

export default defineComponent({
  name: 'EssentialLink',
  props: {
    title: {
      type: String,
      required: true
    },

    caption: {
      type: String,
      default: ''
    },

    link: {
      type: String,
      default: '#'
    },

    icon: {
      type: String,
      default: ''
    }
  },
  setup () {
    const linksList = ref([
      {
        title: 'Anúncios',
        icon: 'fa-solid fa-store',
        link: '#/buscar'
      },
      {
        title: 'Novo Anúncio',
        icon: 'fa-solid fa-plus',
        link: '#/manterManga'
      },
      {
        title: 'Meus Pedidos',
        icon: 'fa-solid fa-box',
        link: '#/acompanharpedido'
      },
      {
        title: 'Meus Anúncios',

        icon: 'fa-solid fa-folder',
        link: '#/meusProdutos'
      },
      {
        title: 'Carrinho/Pagamento',
        icon: 'fa-solid fa-cart-shopping',
        link: '#/pagamentos'
      }
    ])
    return { linksList }
  }
})
</script>
