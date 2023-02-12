<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
     <ToolbarMenu @leftDrawer="toggleLeftDrawer"/>
    </q-header>

    <q-page-container>
     <!--Página aqui-->
      <div class="q-pa-md" style="display: grid; justify-content: center; padding-top:100px;" >
        <div class="q-gutter-y-md column" style="max-width: 300px">

          <span class="text-h5" style="text-align:center;">Cadastre-se</span>

          <form class="q-gutter-md">

            <q-input outlined v-model="cliente.nome" label="Nome *" :dense="dense" lazy-rules />

            <q-input outlined type="email" label="Email *" :dense="dense" lazy-rules />

            <q-input label="Senha *" outlined :type="password ? 'password' : 'text'"/>
            <q-input label="Confirmar senha *" outlined :type="password ? 'password' : 'text'"/>

            <div>
              <q-btn label="Cadastrar" @click="CadastrarCliente" color="positive" style="width:100%"/>

            </div>
            <q class="ribbon" style="display: block; margin-top:15px;">OU</q>
            <div>
              <q-btn font-awesome-icon icon="fa-brands fa-google" label="Entrar com sua conta Google" type="submit"  style="color: black; background-color: #F5F5F5; width:100%;"/>

            </div>
          </form>
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
import { defineComponent } from 'vue'
import EssentialLink from 'components/EssentialLink.vue'
import ToolbarMenu from 'components/ToolbarMenu.vue'

import ClienteDataService from '../services/ClienteDataService'

export default defineComponent({
  name: 'MainLayout',

  components: {
    EssentialLink,
    ToolbarMenu
  },

  data () {
    return {
      cliente: {
        nome: ''
      }
    }
  },
  methods: {
    CadastrarCliente () {
      const data = {
        nome: this.cliente.nome
      }

      ClienteDataService.cadastrar(data)
        .then(() => {
          this.$router.push('logar')
        })
    }
  }
})
</script>
