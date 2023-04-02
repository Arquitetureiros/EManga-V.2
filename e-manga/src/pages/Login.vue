<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
     <ToolbarMenu @leftDrawer="toggleLeftDrawer"/>
    </q-header>

    <q-page-container>
     <!--Página aqui-->
      <div class="q-pa-md" style="display: grid; justify-content: center; padding-top:100px;" >
        <div class="q-gutter-y-md column" style="max-width: 300px">

          <span class="text-h5" style="text-align:center;">Login</span>

          <form @submit.prevent.stop="onSubmit" @reset.prevent.stop="onReset" class="q-gutter-md">

            <q-input ref="emailRef" outlined v-model="usuario.email" type="email" label="Email *" :dense="dense" lazy-rules :rules="emailRules" />

            <q-input ref="passwRef" v-model="usuario.senha" label="Senha *" outlined :type="password ? 'password' : 'text'" :rules="passwRules" />
            <div>
              <q-btn label="Entrar" @click="Logar" color="positive" style="width:100%"/>
            </div>
            <div style="text-align: center;">
              <span>Não é cadastrado?</span>
              <q-btn label="Cadastrar-se" to="/cadastro" color="positive" style="width:100%"/>
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
import { useQuasar } from 'quasar'
import { defineComponent, ref } from 'vue'
import EssentialLink from 'components/EssentialLink.vue'
import ToolbarMenu from 'components/ToolbarMenu.vue'

import UsuarioDataService from '../services/UsuarioDataService'

export default defineComponent({
  name: 'MainLayout',

  components: {
    EssentialLink,
    ToolbarMenu
  },

  setup () {
    const $q = useQuasar()
    const leftDrawerOpen = ref(false)
    const nrItens = ref(1)
    const name = ref()
    const email = ref()
    const password = ref()
    const isPwd = ref(true)
    const accept = ref(false)
    const nameRef = ref()
    const emailRef = ref()
    const passwRef = ref()

    return {
      leftDrawerOpen,
      toggleLeftDrawer () {
        leftDrawerOpen.value = !leftDrawerOpen.value
      },
      nrItens,
      password,
      passwRef,
      isPwd,
      email,
      emailRef,
      emailRules: [
        val => (val && val.length > 0) || 'Digite um email'
      ],
      passwRules: [
        val => (val && val.length > 0) || 'Digite uma senha'
      ],
      accept,

      onSubmit () {
        emailRef.value.validate()
        passwRef.value.validate()

        if (emailRef.value.hasError || passwRef.value.hasError) {
          // form has error
        } else if (accept.value !== true) {
          $q.notify({
            color: 'negative',
            message: 'É preciso aceitar os termos de uso antes'
          })
        } else {
          $q.notify({
            icon: 'done',
            color: 'positive',
            message: 'Submitted'
          })
        }
      },

      onReset () {
        name.value = null
        email.value = null
        password.value = null

        nameRef.value.resetValidation()
        emailRef.value.resetValidation()
        passwRef.value.resetValidation()
      }
    }
  },

  data () {
    return {
      usuario: {
        email: '',
        senha: ''
      }
    }
  },
  methods: {
    Logar () {
      const data = {
        email: this.usuario.email,
        senha: this.usuario.senha
      }

      UsuarioDataService.logar(data)
        .then((response) => {
          localStorage.setItem('jwt', JSON.stringify(response.data))
          if (this.$route.query.redirect) {
            this.$router.push(this.$route.query.redirect)
          } else {
            this.$router.push('/')
          }
        })
    }
  }
})
</script>
