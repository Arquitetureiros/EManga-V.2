<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <ToolbarMenu @leftDrawer="toggleLeftDrawer"/>
    </q-header>

    <q-page-container class="flex justify-center q-pa-md" style="display: grid; justify-content: center; padding-top:100px;">

    <div class="column q-gutter-y-md" style="max-width: 300px">

      <div class="text-h5" style="text-align:center;">Perfil</div>

      <div style="width: 100%; margin: 40px 0;" class="row justify-center">
        <q-avatar size="150px">
          <img src="public/avatar.png">
        </q-avatar>
      </div>

      <form action="" class="q-gutter-lg">
        <q-input ref="" outlined v-model="usuario.nome" label="Nome" :dense="dense" lazy-rules :rules="nameRules" style="width: 100%;"/>

        <q-input ref="" outlined v-model="usuario.email" label="Email" :dense="dense" lazy-rules :rules="nameRules" style="width: 100%;"/>

        <div class="row" style="flex-wrap: nowrap; width: 100%;">
          <q-input style="width: 70%;" ref="" outlined v-model="endereco.cep" label="Cep" :dense="dense" lazy-rules :rules="nameRules" />

          <q-input style="width: 30%;" ref="" outlined v-model="endereco.num" label="Num" :dense="dense" lazy-rules :rules="nameRules"/>
        </div>

        <q-input ref="" outlined v-model="endereco.logradouro" label="Logradouro" :dense="dense" lazy-rules :rules="nameRules" style="width: 100%;"/>

        <div class="row" style="flex-wrap: nowrap; width: 100%;">
          <q-input style="width: 70%;" ref="" outlined v-model="endereco.cidade" label="Cidade" :dense="dense" lazy-rules :rules="nameRules" />

          <q-input style="width: 30%;" ref="" outlined v-model="endereco.uf" label="UF" :dense="dense" lazy-rules :rules="nameRules" />
        </div>
        <div class="row content-center" style="width: 100%;">
          <q-btn style="width: 100%; padding: 0;" label="Editar Endereço" color="positive" @click="AtualizarEndereco"/>
          <!--<q-icon name="font_download" size="25px" color="green"/>
          Novo Endereço-->
        </div>

        <q-card class="my-card" style="width: 100%;">
          <q-card-section class="row justify-between">
            <div class="text-h6">Meus Cartões</div>
            <div class="text-subtitle2">
              <q-icon name="font_download" size="25px" color="green"/>
              Novo Cartão
            </div>
          </q-card-section>

          <q-separator />

          <q-card-actions vertical>
            <div class="row">
              <q-icon name="font_download" size="25px" color="green"/>
              <q-btn flat>Cartao 1</q-btn>
              <p>****</p>
              <q-icon name="font_download" size="25px" color="green"/>
            </div>
            <div class="row">
              <q-icon name="font_download" size="25px" color="green"/>
              <q-btn flat>Cartao 2</q-btn>
              <p>****</p>
              <q-icon name="font_download" size="25px" color="green"/>
            </div>
          </q-card-actions>
        </q-card>

        <q-btn style="width: 100%; padding: 0;" label="Salvar Perfil" color="positive" @click="SalvarPerfil"/>
      </form>
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
import ToolbarMenu from 'components/ToolbarMenu.vue'
import EssentialLink from 'components/EssentialLink.vue'

import UsuarioDataService from 'src/services/UsuarioDataService'
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
        id: '',
        nome: '',
        email: '',
        senha: ''
      },
      endereco: {
        id: '',
        user_id: '',
        cep: '',
        num: '',
        logradouro: '',
        cidade: '',
        uf: ''
      }
    }
  },
  methods: {
    CarregarDados () {
      const token = localStorage.getItem('jwt');
      if(!token) { return; }

      const decodedToken = jwtDecode(token);

      UsuarioDataService.obter(decodedToken['user_id'])
        .then((response) => {
          this.usuario = response.data
            
        })

        EnderecoDataService.listarPorUsuario(decodedToken['user_id'])
          .then((response) => {
            console.log(response)
            this.endereco = response.data[0];
          })
    },
    AtualizarEndereco()
    {
      const data = this.endereco;

      EnderecoDataService.atualizar(data)
        .then((response) => {
            
        })
    },
    SalvarPerfil()
    {
      const data = this.usuario
      console.log(data)

      UsuarioDataService.atualizar(data)
        .then((response) => {
          this.AtualizarEndereco()
        })
    }
  },
  mounted()
  {
    this.CarregarDados();
  }
})
</script>
