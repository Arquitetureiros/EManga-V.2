<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
     <ToolbarMenu @leftDrawer="toggleLeftDrawer"/>
    </q-header>

    <q-page-container>
      <div class="q-pa-md q-pt-xl flex justify-center">
        <div class="items-center flex justify-around" style="height: auto; width: 60%;">
          <div class="">
              <div style="padding: 40px" >
                  <img :src=mangaAtt.fotoCaminho style="height: 400px; width: 280px" alt="">
              </div>
              <div style="display: flex; margin-top: 10px; justify-content: space-between;">
                <q-file color="red" v-model="imagem1" style="background-color: #eee; height: 80px; width: 80px" accept=".jpg, image/*">
                <template v-slot:prepend>
                </template>
              </q-file>
              <q-file color="red" v-model="imagem2" style="background-color: #eee; height: 80px; width: 80px" accept=".jpg, image/*">
                <template v-slot:prepend>
                </template>
              </q-file>
              <q-file color="red" v-model="imagem3" style="background-color: #eee; height: 80px; width: 80px" accept=".jpg, image/*">
                <template v-slot:prepend>
                </template>
              </q-file>
              <q-file color="red" v-model="imagem4" style="background-color: #eee; height: 80px; width: 80px" accept=".jpg, image/*">
                <template v-slot:prepend>
                </template>
              </q-file>
              </div>
          </div>
          <div class="">
            <div class="q-pa-md" style="max-width: 300px">
              <h4 style="margin:0" >{{ mangaAtt.ds_titulo }}</h4>
            </div>
            <div class="q-pa-md" style="max-width: 300px">
              <p>{{ mangaAtt.ds_sinopse }}</p>
            </div>
            <div class="q-pa-md row" style="max-width: 400px">
              <div class="q-pr-md" style="max-width: 150px">
                Cidade
                <p>{{ mangaAtt.cidade }}</p>
              </div>
              <div class="q-pr-md" style="max-width: 150px">
                Estado abrevidado:
                <p>{{ mangaAtt.estado }}</p>
              </div>
            </div>
            <div class="q-pa-md row" style="max-width: 300px">
              <div class="q-pr-md" style="max-width: 300px">
                Quantidade:
                <q-input
                   v-model.number="quant"
                   type="number"
                   style="max-width: 100px"
                   dense
                   outlined
                   max="2"
                   min="1"
                />
                (Disponivel 2)
              </div>
              <div class="q-pr-md" style="max-width: 300px; display: flex; flex-direction: column; gap: 9px;">
                Preço:
                <p style="font-size: large;">{{ mangaAtt.valor }}</p>
              </div>
              <div class="q-pa-md">
                <q-btn to="/buscar" color="primary" label="Adicionar ao carrinho"/>
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
        />

      </q-list>
    </q-drawer>
  </q-layout>
</template>

<script>
import { defineComponent, ref } from 'vue'
import EssentialLink from 'components/EssentialLink.vue'
import ToolbarMenu from 'components/ToolbarMenu.vue'
import MangaDataService from 'src/services/mangaDataService'

export default defineComponent({
  name: 'MainLayout',

  components: {
    EssentialLink,
    ToolbarMenu
  },

  setup () {
    const leftDrawerOpen = ref(false)
    const nrItens = ref(1)
    const titulo = ref()
    const desc = ref()
    const quant = ref(1)
    const imagem = ref()
    const imagem1 = ref()
    const imagem2 = ref()
    const imagem3 = ref()
    const imagem4 = ref()
    const ratingModel = ref(3)
    const product = ref()
    const manga = ref()

    return {
      leftDrawerOpen,
      toggleLeftDrawer () {
        leftDrawerOpen.value = !leftDrawerOpen.value
      },
      nrItens,
      titulo,
      desc,
      quant,
      imagem,
      imagem1,
      imagem2,
      imagem3,
      imagem4,
      ratingModel,
      product,
      manga
    }
  },
  data () {
    return {
      mangaAtt: {}
    }
  },
  methods: {
    obterPorId () {
      const id = this.$route.params.id // Obter o ID da rota
      Number(id)
      MangaDataService.obterPorId(id).then((response) => {
        this.product = response.data
        console.log(this.product)
        this.manga = this.product[0]
        console.log(this.manga)

        this.mangaAtt = {
          id: this.manga.id,
          ds_titulo: this.manga.ds_titulo,
          ds_sinopse: this.manga.ds_sinopse,
          cidade: this.manga.cidade,
          estado: this.manga.estado,
          valor: this.manga.valor,
          fotoCaminho: this.manga.fotoCaminho,
          quantidade: this.manga.quantidade
        }
      })
    }
  },
  mounted () {
    this.obterPorId()
  }
})
</script>
