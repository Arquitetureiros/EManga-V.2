<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
     <ToolbarMenu @leftDrawer="toggleLeftDrawer"/>
    </q-header>

    <q-page-container>
      <div class="q-pa-md flex justify-center">
        <div class="text-h4 q-pa-md">
        </div>
        <div class="items-center flex justify-around" style="height: auto; width: 60%;">
          <div className="q-pt-md">
            Atualizar imagens :
            <div style="width: 200px; height: 300px" className="q-pt-lg relative-position">
              <q-img
                      v-if="mangaAtt.fotoCaminho"
                      :src=mangaAtt.fotoCaminho
                      spinner-color="white"
                      style="height: 100%; width: 100%"
                      className="absolute-center"
              ></q-img>
            </div>
            <div style="display: flex; margin-top: 10px; justify-content: space-between;">
              <div style="max-width: 80px; max-height: 80px" className="q-pt-lg relative-position">
              <q-file v-model="image2"
                      label="+"
                      filled
                      style="background-color: #eee; width: 100%; height: 100%"
                      >
              </q-file>
              <q-img
                      v-if="imageUrl2"
                      :src="imageUrl2"
                      spinner-color="white"
                      style="height: 100%; width: 100%"
                      className="absolute-center"
                      accept=".jpg, image/*"
              ></q-img>
              </div>
              <div style="width: 80px; height: 80px" className="q-pt-lg relative-position">
              <q-file v-model="image3"
                      label="+"
                      filled
                      style="background-color: #eee; width: 100%; height: 100%"
                      >
              </q-file>
              <q-img
                      v-if="imageUrl3"
                      :src="imageUrl3"
                      spinner-color="white"
                      style="height: 100%; width: 100%"
                      className="absolute-center"
                      accept=".jpg, image/*"
              ></q-img>
              </div>
              <div style="width: 80px; height: 80px" className="q-pt-lg relative-position">
              <q-file v-model="image4"
                      label="+"
                      filled
                      style="background-color: #eee; width: 100%; height: 100%"
                      >
              </q-file>
              <q-img
                      v-if="imageUrl4"
                      :src="imageUrl4"
                      spinner-color="white"
                      style="height: 100%; width: 100%"
                      className="absolute-center"
                      accept=".jpg, image/*"
              ></q-img>
              </div>
              <div style="width: 80px; height: 80px" className="q-pt-lg relative-position">
              <q-file v-model="image5"
                      label="+"
                      filled
                      style="background-color: #eee; width: 100%; height: 100%"
                      >
              </q-file>
              <q-img
                      v-if="imageUrl5"
                      :src="imageUrl5"
                      spinner-color="white"
                      style="height: 100%; width: 100%"
                      className="absolute-center"
              ></q-img>
              </div>
            </div>
          </div>
          <div class="">
            <div class="q-pa-md" style="max-width: 300px">
              Atualizar titulo do anúncio:
              <q-input outlined v-model="mangaAtt.ds_titulo" label="Titulo" />
            </div>
            <div class="q-pa-md" style="max-width: 300px">
              Atualizar descrição do anúncio: <br>
              <q-input v-model="mangaAtt.ds_sinopse" outlined type="textarea" />
            </div>
            <div class="q-pa-md row" style="max-width: 400px">
              <div class="q-pr-md" style="max-width: 150px">
                Cidade
                <q-input outlined v-model="mangaAtt.cidade" label="Cidade" />
              </div>
              <div class="q-pr-md" style="max-width: 150px">
                Estado abrevidado:
                <q-input outlined v-model="mangaAtt.estado" label="Estado" />
              </div>
            </div>
            <div class="q-pa-md row" style="max-width: 300px">
              <div class="q-pr-md" style="max-width: 300px">
                Quantidade:
                <q-input v-model.number="mangaAtt.quantidade" type="number" style="max-width: 100px" dense outlined />
              </div>
              <div class="q-pr-md" style="max-width: 300px">
                Preço:
                <q-input outlined v-model="mangaAtt.valor" type="number" prefix="R$" dense style="max-width: 100px" />
              </div>
              <div class="q-pa-md">
                <q-btn color="primary" to="/meusProdutos" label="Atualizar anúncio" @click="AtualizarManga" />
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

import MangaDataService from 'src/services/MangaDataService'

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
    },
    AtualizarManga () {
      console.log(this.mangaAtt)
      MangaDataService.atualizar(this.mangaAtt)
        .then(() => {
          alert('manga atualizado')
        })
    }
  },
  mounted () {
    this.obterPorId()
  }
})
</script>
