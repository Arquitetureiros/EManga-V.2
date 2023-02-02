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
              <h4 style="margin:0" >Chainsaw man vol.1</h4>
            </div>
            <div class="q-pa-md">
              <q-rating size="2rem" v-model="ratingModel" :max="5" readonly color="yellow" />
            </div>
            <div class="q-pa-md" style="max-width: 300px">
              <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Voluptatibus eaque assumenda sapiente
                mollitia, reiciendis inventore labore maiores dicta modi quisquam asperiores ratione voluptas fugit
                aperiam nesciunt, dolorem minus ullam. Perferendis.</p>
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
                <p style="font-size: large;">R$20</p>
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
      ratingModel
    }
  }
})
</script>
