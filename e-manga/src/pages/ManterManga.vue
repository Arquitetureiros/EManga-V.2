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
              <q-input outlined v-model="manga.ds_titulo" :rules="regrasCampoTexto" label="Titulo" />
            </div>
            <div class="q-pa-md" style="max-width: 300px">
              Adicionar descrição do anúncio:
              <q-input v-model="manga.ds_sinopse" :rules="regrasCampoTexto" outlined type="textarea" />
            </div>
            <div class="q-pa-md row" style="max-width: 400px">
              <div class="q-pr-md" style="max-width: 150px">
                Cidade:
                <q-input outlined v-model="manga.cidade" :rules="regrasCampoTexto" label="Cidade" />
              </div>
              <div class="q-pr-md" style="max-width: 150px">
                Estado abrevidado:
                <q-input outlined v-model="manga.estado" :rules="regrasEstado" label="Estado" />
              </div>
            </div>
            <div class="q-pa-md row" style="max-width: 300px">
              <div class="q-pr-md" style="max-width: 300px">
                Quantidade:
                <q-input v-model.number="manga.quantidade" type="number" :rules="[validarValor]" style="max-width: 100px" dense outlined />
              </div>
              <div class="q-pr-md" style="max-width: 300px">
                Preço:
                <q-input outlined v-model="manga.valor" type="number" :rules="[validarValor]" prefix="R$" dense style="max-width: 100px" />
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
import { defineComponent, ref } from 'vue'
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

  setup () {
    const imageUrl = ref('')
    const image = ref(null)
    const imageUrl2 = ref('')
    const image2 = ref(null)
    const imageUrl3 = ref('')
    const image3 = ref(null)
    const imageUrl4 = ref('')
    const image4 = ref(null)
    const imageUrl5 = ref('')
    const image5 = ref(null)

    const handleUploadImage2 = () => {
      if (image2.value) {
        imageUrl2.value = URL.createObjectURL(image2.value)
      }
    }
    const handleUploadImage3 = () => {
      if (image3.value) {
        imageUrl3.value = URL.createObjectURL(image3.value)
      }
    }
    const handleUploadImage4 = () => {
      if (image4.value) {
        imageUrl4.value = URL.createObjectURL(image4.value)
      }
    }
    const handleUploadImage5 = () => {
      if (image5.value) {
        imageUrl5.value = URL.createObjectURL(image5.value)
      }
    }

    return {
      imageUrl,
      image,
      imageUrl2,
      image2,
      imageUrl3,
      image3,
      imageUrl4,
      image4,
      imageUrl5,
      image5,
      handleUploadImage2,
      handleUploadImage3,
      handleUploadImage4,
      handleUploadImage5,
      regrasCampoTexto: [
        val => (val && val.length > 0) || 'O campo não pode ser vazio'
      ],
      regrasEstado: [
        val => (val && val.length > 0) || 'O campo não pode ser vazio',
        val => (val.length <= 2) || 'O estado tem que ser abreviado'
      ]
    }
  },
  data () {
    return {
      manga: {
        ds_titulo: null,
        ds_sinopse: '',
        cidade: '',
        estado: '',
        valor: 0,
        fotoCaminho: '',
        quantidade: 1
      },
      leftDrawerOpen: false
    }
  },
  methods: {
    AdicionarManga () {
      const data = {
        ds_titulo: this.manga.ds_titulo,
        ds_sinopse: this.manga.ds_sinopse,
        cidade: this.manga.cidade,
        estado: this.manga.estado,
        valor: this.manga.valor,
        fotoCaminho: this.image.name,
        quantidade: this.manga.quantidade
      }

      MangaDataService.cadastrar(data)
        .then(() => {
          alert('manga adicionado')
        })
    },
    toggleLeftDrawer () {
      this.leftDrawerOpen = !this.leftDrawerOpen
    },
    handleUploadImage () {
      if (this.image) {
        this.imageUrl = URL.createObjectURL(this.image)
      }
    },
    validarValor (valor) {
      if (valor < 0) {
        return 'O valor não pode ser negativo.'
      }
      return true
    }
  }
})
</script>
