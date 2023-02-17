<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <ToolbarMenu @leftDrawer="toggleLeftDrawer" />
    </q-header>

    <q-page-container>
      <div class="q-pa-md flex justify-center">
        <div class="text-h4 q-pa-md">
        </div>
        <div class="items-center flex justify-around" style="height: auto; width: 60%;">
          <div className="q-pt-md">
            Adicionar imagens :
            <div style="width: 200px; height: 300px" className="q-pt-lg relative-position">
              <q-file v-model="image"
                      label="+"
                      filled
                      style="width: 100%; height: 100%"
                      @update:model-value="handleUploadImage()"
                      accept=".jpg, image/*"
              ></q-file>
              <q-img
                      v-if="imageUrl"
                      :src="imageUrl"
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
                      @update:model-value="handleUploadImage2()">
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
                      @update:model-value="handleUploadImage3()">
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
                      @update:model-value="handleUploadImage4()">
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
                      @update:model-value="handleUploadImage5()"
                      accept=".jpg, image/*">
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
              Adicionar titulo do anúncio:
              <q-input outlined v-model="manga.ds_titulo" label="Titulo" />
            </div>
            <div class="q-pa-md" style="max-width: 300px">
              Adicionar descrição do anúncio:
              <q-input v-model="manga.ds_sinopse" outlined type="textarea" />
            </div>
            <div class="q-pa-md row" style="max-width: 300px">
              <div class="q-pr-md" style="max-width: 300px">
                Quantidade:
                <q-input v-model.number="manga.quantidade" type="number" style="max-width: 100px" dense outlined />
              </div>
              <div class="q-pr-md" style="max-width: 300px">
                Preço:
                <q-input outlined v-model="manga.valor" type="number" prefix="R$" dense style="max-width: 100px" />
              </div>
              <div class="q-pa-md">
                <q-btn to="/meusProdutos" color="primary" label="Adicionar anúncio" @click="AdicionarManga"/>
              </div>
            </div>
          </div>
        </div>
      </div>
    </q-page-container>

    <q-drawer v-model="leftDrawerOpen" show-if-above bordered>
      <q-list>
        <q-item-label header>
          Opções
        </q-item-label>

        <EssentialLink />

      </q-list>
    </q-drawer>
  </q-layout>
</template>

<script>
import { defineComponent } from 'vue'
import EssentialLink from 'components/EssentialLink.vue'
import ToolbarMenu from 'components/ToolbarMenu.vue'
// import axios from 'axios'

import MangaDataService from 'src/services/MangaDataService'

export default defineComponent({
  name: 'MainLayout',

  components: {
    EssentialLink,
    ToolbarMenu
  },

  // setup () {
  //   const leftDrawerOpen = ref(false)
  //   const nrItens = ref(1)
  //   const titulo = ref()
  //   const desc = ref()
  //   const quant = ref(1)
  //   const image = ref(null)
  //   const imageUrl = ref('')
  //   const image2 = ref(null)
  //   const imageUrl2 = ref('')
  //   const image3 = ref(null)
  //   const imageUrl3 = ref('')
  //   const image4 = ref(null)
  //   const imageUrl4 = ref('')
  //   const image5 = ref(null)
  //   const imageUrl5 = ref('')

  //   function get () {
  //     axios.get('http://127.0.0.1:8000/api/opabao')
  //       .then(response => {
  //         this.valortes = response.data.valortes
  //       })
  //   }

  //   function enviarDado () {
  //     axios.post('http://127.0.0.1:8000/api/opabao', {
  //       titulo: this.titulo
  //     })
  //       .then(response => {
  //         console.log(response.titulo)
  //       })
  //       .catch(error => {
  //         console.log(error)
  //       })
  //   }

  //   const handleUploadImage = () => {
  //     if (image.value) {
  //       imageUrl.value = URL.createObjectURL(image.value)
  //     }
  //   }
  //   const handleUploadImage2 = () => {
  //     if (image2.value) {
  //       imageUrl2.value = URL.createObjectURL(image2.value)
  //     }
  //   }
  //   const handleUploadImage3 = () => {
  //     if (image3.value) {
  //       imageUrl3.value = URL.createObjectURL(image3.value)
  //     }
  //   }
  //   const handleUploadImage4 = () => {
  //     if (image4.value) {
  //       imageUrl4.value = URL.createObjectURL(image4.value)
  //     }
  //   }
  //   const handleUploadImage5 = () => {
  //     if (image5.value) {
  //       imageUrl5.value = URL.createObjectURL(image5.value)
  //     }
  //   }

  //   onMounted(() => {
  //     get()
  //   })

  //   return {
  //     leftDrawerOpen,
  //     toggleLeftDrawer () {
  //       leftDrawerOpen.value = !leftDrawerOpen.value
  //     },
  //     nrItens,
  //     titulo,
  //     desc,
  //     quant,
  //     image,
  //     imageUrl,
  //     image2,
  //     imageUrl2,
  //     image3,
  //     imageUrl3,
  //     image4,
  //     imageUrl4,
  //     image5,
  //     get,
  //     enviarDado,
  //     imageUrl5,
  //     handleUploadImage,
  //     handleUploadImage2,
  //     handleUploadImage3,
  //     handleUploadImage4,
  //     handleUploadImage5
  //   }
  data () {
    return {
      manga: {
        ds_sinopse: '',
        ds_titulo: '',
        valor: 0,
        fotoCaminho: 'chain.jpg',
        quantidade: ''
      }
    }
  },
  methods: {
    AdicionarManga () {
      const data = {
        ds_sinopse: this.manga.ds_sinopse,
        ds_titulo: this.manga.ds_titulo,
        valor: this.manga.valor,
        fotoCaminho: 'chain.jpg',
        quantidade: this.manga.quantidade
      }

      MangaDataService.cadastrar(data)
        .then(() => {
          alert('MangaAdicionado')
        })
    }
  }
})
</script>
