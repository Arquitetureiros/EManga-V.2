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

            <q-input outlined v-model="usuario.nome" label="Nome *" :dense="dense" lazy-rules />

            <q-input outlined v-model="usuario.email" type="email" label="Email *" :dense="dense" lazy-rules />

            <q-input v-model="usuario.senha" label="Senha *" outlined type="password"/>
            <q-input v-model="aux.conf_senha" label="Confirmar senha *" outlined type="password"/>

            <div>
              <q-btn label="Cadastrar" @click="CadastrarUsuario" color="positive" style="width:100%"/>

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
import { defineComponent, ref } from 'vue'
import EssentialLink from 'components/EssentialLink.vue'
import ToolbarMenu from 'components/ToolbarMenu.vue'

import UsuarioDataService from '../services/UsuarioDataService'
import EnderecoDataService from 'src/services/EnderecoDataService'

import jwtDecode from 'jwt-decode';

export default defineComponent({
  name: 'MainLayout',

  components: {
    EssentialLink,
    ToolbarMenu
  },

  setup () {
    const leftDrawerOpen = ref(false)

    return {
      leftDrawerOpen,
      toggleLeftDrawer () {
        leftDrawerOpen.value = !leftDrawerOpen.value
      }
    }
  },

  data () {
    return {
      usuario: {
        nome: '',
        email: '',
        senha: ''
      },
      aux: {
        conf_senha: ''
      }
    }
  },
  methods: {
    CadastrarUsuario () {
      const data = {
        nome: this.usuario.nome,
        email: this.usuario.email,
        senha: this.usuario.senha
      }

      if (data.senha !== this.aux.conf_senha) {
        return
      }

      UsuarioDataService.cadastrar(data)
        .then(() => {
          const login = {
            email: this.usuario.email,
            senha: this.usuario.senha
            }

          UsuarioDataService.logar(login)
            .then((response) => {
              localStorage.setItem('jwt', JSON.stringify(response.data))

              const token = localStorage.getItem('jwt');

              const decodedToken = jwtDecode(token);

              const endereco = {
                user_id: decodedToken['user_id']
              }

              EnderecoDataService.cadastrar(JSON.stringify(endereco))
                .then((response) => {
                })

              if (this.$route.query.redirect) {
                this.$router.push(this.$route.query.redirect)
              } else {
                this.$router.push('/')
              }
            })
        })
    }
  }
})
</script>
