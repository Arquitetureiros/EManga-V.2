<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar class="bg-primary">
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"
        />

        <q-toolbar-title class="bg-primary">
          Cadastro
        </q-toolbar-title>
        <div>
          <q-btn to="/login" flat color="white" label="Entrar/Cadastrar"
          size="13px"
          />
        </div>
        <div>
          <q-btn round>
            <q-avatar size="42px">
              <img src="public/blankicon.jpeg">
            </q-avatar>
          </q-btn>
        </div>
      </q-toolbar>
    </q-header>

    <q-page-container>
     <!--Página aqui-->
      <div class="q-pa-md" style="display: grid; justify-content: center; padding-top:100px;" >
        <div class="q-gutter-y-md column" style="max-width: 300px">

          <span class="text-h5">Cadastre-se</span>

          <form @submit.prevent.stop="onSubmit" @reset.prevent.stop="onReset" class="q-gutter-md">

            <q-input ref="nameRef" outlined v-model="name" label="Nome *" :dense="dense" lazy-rules :rules="nameRules" />

            <q-input ref="emailRef" outlined v-model="email" type="email" label="Email *" :dense="dense" lazy-rules :rules="emailRules" />

            <q-input ref="passwRef" v-model="password" label="Senha *" outlined :type="password ? 'password' : 'text'" :rules="passwRules" />
            <q-input ref="accPassRef" v-model="acceptPassword" label="Confirmar senha *" outlined :type="password ? 'password' : 'text'" :rules="accPasswRules" />

            <div>
              <q-btn label="Cadastrar" type="submit" color="positive" style="width:100%"/>

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
          v-for="link in essentialLinks"
          :key="link.title"
          v-bind="link"
        />

      </q-list>
    </q-drawer>
  </q-layout>
</template>

<script>
import { useQuasar } from 'quasar'
import { defineComponent, ref } from 'vue'
import EssentialLink from 'components/EssentialLink.vue'

const linksList = [
  {
    title: 'Início',
    icon: 'school',
    link: '#/buscar'
  },
  {
    title: 'Criar Anuncio',
    icon: 'chat',
    link: '#/manterManga'
  },
  {
    title: 'Carrinho/Pagamento',
    icon: 'receipt',
    link: '#/pagamentos'
  },
  {
    title: 'Meus Pedidos',
    icon: 'record_voice_over',
    link: '#/acompanharpedido'
  },
  {
    title: 'Meus Produtos',
    icon: 'favorite',
    link: '#/meusProdutos'
  }
]

export default defineComponent({
  name: 'MainLayout',

  components: {
    EssentialLink
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
    const acceptPassword = ref()
    const accPassRef = ref()

    return {
      essentialLinks: linksList,
      leftDrawerOpen,
      toggleLeftDrawer () {
        leftDrawerOpen.value = !leftDrawerOpen.value
      },
      nrItens,
      password,
      passwRef,
      isPwd,
      acceptPassword,
      accPassRef,
      email,
      emailRef,
      name,
      nameRef,
      nameRules: [
        val => (val && val.length > 0) || 'Digite um nome'
      ],
      emailRules: [
        val => (val && val.length > 0) || 'Digite um email'
      ],
      passwRules: [
        val => (val && val.length > 0) || 'Digite uma senha'
      ],
      accPasswRules: [
        val => (val && val.length > 0) || 'Digite a mesma senha'
      ],
      accept,

      onSubmit () {
        nameRef.value.validate()
        emailRef.value.validate()
        passwRef.value.validate()
        accPassRef.value.validate()

        if (nameRef.value.hasError || emailRef.value.hasError || passwRef.value.hasError || accPassRef.value.hasError) {
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
        acceptPassword.value = null

        nameRef.value.resetValidation()
        emailRef.value.resetValidation()
        passwRef.value.resetValidation()
        accPassRef.value.resetValidation()
      }
    }
  }
})
</script>
