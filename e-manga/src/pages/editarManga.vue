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
            <q-file v-model="imagem"
                      label="+"
                      filled
                      style="width: 100%; height: 100%"
                      @update:model-value="handleUploadImage()"
                      accept=".jpg, image/*"
              ></q-file>
          </div>
          <div class="">
            <div class="q-pa-md" style="max-width: 300px">
              Atualizar titulo do anúncio:
              <q-input outlined v-model="mangaAtt.ds_titulo" :rules="regrasCampoTexto" label="Titulo" />
            </div>
            <div class="q-pa-md" style="max-width: 300px">
              Atualizar descrição do anúncio: <br>
              <q-input v-model="mangaAtt.ds_sinopse" :rules="regrasCampoTexto" outlined type="textarea" />
            </div>
            <div class="q-pa-md row" style="max-width: 400px">
              <div class="q-pr-md" style="max-width: 150px">
                Cidade
                <q-input outlined v-model="mangaAtt.cidade" :rules="regrasCampoTexto" label="Cidade" />
              </div>
              <div class="q-pr-md" style="max-width: 150px">
                Estado abrevidado:
                <q-input outlined v-model="mangaAtt.estado" :rules="regrasEstado" label="Estado" />
              </div>
            </div>
            <div class="q-pa-md row" style="max-width: 300px">
              <div class="q-pr-md" style="max-width: 300px">
                Quantidade:
                <q-input v-model.number="mangaAtt.quantidade" type="number" :rules="[validarValor]" style="max-width: 100px" dense outlined />
              </div>
              <div class="q-pr-md" style="max-width: 300px">
                Preço:
                <q-input outlined v-model="mangaAtt.valor" type="number" :rules="[validarValor]" prefix="R$" dense style="max-width: 100px" />
              </div>
              <div class="q-pa-md">
                <q-btn color="primary" to="/meusProdutos" label="Atualizar anúncio" @click="AtualizarManga" />
              </div>
              <div class="q-pa-md">
                <q-btn color="primary" to="/meusProdutos" label="Desativar anúncio" @click="DesativarManga" />
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
      product,
      manga,
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
      mangaAtt: {}
    }
  },
  methods: {
    obterPorId () {
      const idSite = this.$route.params.id // Obter o ID da rota
      MangaDataService.obterPorId(idSite).then((response) => {
        this.product = response.data
        console.log(this.product)
        this.manga = this.product[0]
        console.log(this.manga)

        this.mangaAtt = {
          id: idSite,
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
      if (this.mangaAtt.quantidade > 0 && this.mangaAtt.valor > 0 && this.mangaAtt.ds_titulo.length > 0) {
        MangaDataService.atualizar(this.mangaAtt.id, this.mangaAtt)
          .then(() => {
            alert('manga atualizado')
          })
      } else {
        alert('A quantidade e o preço do manga devem ser maior que 0 e ele precisa possuir um titulo')
      }
    },
    DesativarManga () {
      const idSite = this.$route.params.id // Obter o ID da rota

      this.mangaDest = {
        id: idSite,
        ds_titulo: this.manga.ds_titulo,
        ds_sinopse: this.manga.ds_sinopse,
        cidade: this.manga.cidade,
        estado: this.manga.estado,
        valor: this.manga.valor,
        fotoCaminho: this.manga.fotoCaminho.name,
        quantidade: 0
      }
      MangaDataService.atualizar(this.mangaDest.id, this.mangaDest)
        .then(() => {
          alert('manga desativado')
        })
    },
    handleUploadImage () {
      if (this.imagem) {
        this.mangaAtt.fotoCaminho = URL.createObjectURL(this.imagem)
      }
    },
    validarValor (valor) {
      if (valor < 1) {
        return 'não pode ser negativo ou zero.'
      }
      return true
    }
  },
  mounted () {
    this.obterPorId()
  }
})
</script>
