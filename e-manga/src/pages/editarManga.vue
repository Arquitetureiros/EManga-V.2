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
          <div class="">
              Atuali imagens:
              <div style="padding: 40px" >
                  <img src="public/chain.jpg" style="height: 400px; width: 280px" alt="">
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
              Atualizar titulo do anúncio:
              <q-input outlined v-model="titulo" label="Titulo"/>
            </div>
            <div class="q-pa-md" style="max-width: 300px">
              Atualizar descrição do anúncio:
              <q-input
                 v-model="desc"
                 outlined
                 type="textarea"
              />
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
                />
              </div>
              <div class="q-pr-md" style="max-width: 300px">
                Preço:
                <q-input outlined v-model="number" type="number" prefix="R$" dense style="max-width: 100px"/>
              </div>
            </div>
            <div class="q-pa-md q-gutter-sm">
              <q-btn  to="/meusProdutos" color="primary" label="Desativar anúncio"/>
              <q-btn  to="/meusProdutos" color="primary" label="Atualizar anúncio"/>
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
      imagem4
    }
  }
})
</script>
