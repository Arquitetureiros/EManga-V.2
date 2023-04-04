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
        <q-input outlined v-model="usuario.nome" label="Nome" :dense="dense" lazy-rules :rules="nameRules" style="width: 100%;" readonly/>

        <q-input outlined v-model="usuario.email" label="Email" :dense="dense" lazy-rules :rules="nameRules" style="width: 100%;" readonly/>

        <div class="row" style="flex-wrap: nowrap; width: 100%;">
          <q-input style="width: 70%;" ref="" outlined v-model="endereco.cep" label="Cep" :dense="dense" lazy-rules :rules="nameRules" readonly/>

          <q-input style="width: 30%;" ref="" outlined v-model="endereco.num" label="Num" :dense="dense" lazy-rules :rules="nameRules" readonly/>
        </div>

        <q-input ref="" outlined v-model="endereco.logradouro" label="Logradouro" :dense="dense" lazy-rules :rules="nameRules" style="width: 100%;" readonly/>

        <div class="row" style="flex-wrap: nowrap; width: 100%;">
          <q-input style="width: 70%;" ref="" outlined v-model="endereco.cidade" label="Cidade" :dense="dense" lazy-rules :rules="nameRules" readonly/>

          <q-input style="width: 30%;" ref="" outlined v-model="endereco.uf" label="UF" :dense="dense" lazy-rules :rules="nameRules" readonly/>
        </div>
        <div class="row" style="width: 100%; justify-content: space-between;">
          <q-btn style="width: 40%; padding: 0;" label="Editar Perfil" color="positive" @click="ToggleUpdateInfo"/>
          <q-btn style="width: 40%; padding: 0;" label="Editar Endereço" color="positive" @click="ToggleUpdateEndereco"/>
          <!--<q-icon name="font_download" size="25px" color="green"/>
          Novo Endereço-->
        </div>

        <q-card class="my-card" style="width: 100%;">
          <q-card-section class="row justify-between">
            <div class="text-h6">Meus Cartões</div>
            <q-btn class="text-subtitle2" @click="ToggleAddCartao">
              <q-icon name="add" size="25px" color="blue"/>
              Novo Cartão
            </q-btn>
          </q-card-section>

          <q-separator />

          <q-card-actions vertical v-for="cartao in cartoes">
            <div class="row" style="width: 100%;">
            <q-btn class="row align-items-center">
              <q-icon name="credit_card" size="25px" color="black"/>
              <q-btn flat @click="ToggleEditCartao(cartao)">{{ cartao.nome }}</q-btn>
            </q-btn>
            <q-icon name="delete" size="25px" color="red" @click="DeletarCartao(cartao.id)"/>
          </div>
          </q-card-actions>
        </q-card>

        <!--<q-btn style="width: 100%; padding: 0;" label="Salvar Perfil" color="positive" @click="SalvarPerfil"/>-->

      </form>
    </div>

    <q-dialog v-model="updateInfo">
      <q-card>
        <q-card-section>
          <div class="text-h6">Atualizar Informações</div>
        </q-card-section>

        <q-card-section class="q-pt-none">
          <q-input outlined v-model="aux_usuario.nome" label="Nome" :dense="dense" lazy-rules :rules="nameRules" style="width: 100%;"/>
          <q-input outlined v-model="aux_usuario.email" label="Email" :dense="dense" lazy-rules :rules="nameRules" style="width: 100%;"/>
          <q-input outlined v-model="aux_usuario.senha" label="Nova Senha" type="" :dense="dense" lazy-rules :rules="nameRules" style="width: 100%;"/>
          <q-input outlined v-model="conf_senha" label="Senha" type="" :dense="dense" lazy-rules :rules="nameRules" style="width: 100%;"/>
        </q-card-section>

        <q-card-actions>
          <q-btn style="width: 100%; padding: 0;" label="Salvar Informações" color="positive" v-close-popup @click="SalvarPerfil"/>
        </q-card-actions>
      </q-card>
    </q-dialog>

    <q-dialog v-model="updateEndereco">
      <q-card>
        <q-card-section>
          <div class="text-h6">Atualizar Endereco</div>
        </q-card-section>

        <q-card-section class="q-pt-none">
          <div class="row" style="width: 100%">
            <q-input outlined v-model="aux_endereco.cep" label="CEP" :dense="dense" lazy-rules :rules="nameRules" style="width: 70%;"/>
            <q-input outlined v-model="aux_endereco.num" label="Numero" type="number" :dense="dense" lazy-rules :rules="nameRules" style="width: 30%;"/>
          </div>
          <q-input outlined v-model="aux_endereco.logradouro" label="Logradouro" :dense="dense" lazy-rules :rules="nameRules" style="width: 100%;"/>
          <q-input outlined v-model="aux_endereco.cidade" label="Cidade" :dense="dense" lazy-rules :rules="nameRules" style="width: 100%;"/>
          <q-input outlined v-model="aux_endereco.uf" label="UF" :dense="dense" lazy-rules :rules="nameRules" style="width: 100%;"/>
        </q-card-section>

        <q-card-actions>
          <q-btn style="width: 100%; padding: 0;" label="Salvar Endereco" color="positive" v-close-popup @click="AtualizarEndereco"/>
        </q-card-actions>
      </q-card>
    </q-dialog>

    <q-dialog v-model="addCartao">
      <q-card>
        <q-card-section>
          <div class="text-h6">Adicionar Cartão</div>
        </q-card-section>

        <q-card-section class="q-pt-none">
          <q-input ref="" outlined v-model="cartao.nome" label="Nome" :dense="dense" lazy-rules :rules="nameRules" style="width: 100%;"/>
          <q-input ref="" outlined v-model="cartao.numero" label="Numero" type="number" :dense="dense" lazy-rules :rules="nameRules" style="width: 100%;"/>
          <div class="row">
            <q-input ref="" outlined v-model="cartao.validade" label="Validade" :dense="dense" lazy-rules :rules="nameRules" style="width: 70%;"/>
            <q-input ref="" outlined v-model="cartao.cvc" label="Cvc" :dense="dense" lazy-rules :rules="nameRules" style="width: 30%;"/>
          </div>
        </q-card-section>

        <q-card-actions>
          <q-btn style="width: 100%; padding: 0;" label="Salvar Cartao" color="positive" v-close-popup @click="CriarCartao"/>
        </q-card-actions>
      </q-card>
    </q-dialog>
    <q-dialog v-model="editCartao">
      <q-card>
        <q-card-section>
          <div class="text-h6">Editar Cartão</div>
        </q-card-section>

        <q-card-section class="q-pt-none">
          <q-input ref="" outlined v-model="cartao_aux.nome" label="Nome" :dense="dense" lazy-rules :rules="nameRules" style="width: 100%;"/>
          <q-input ref="" outlined v-model="cartao_aux.numero" label="Numero" type="number" :dense="dense" lazy-rules :rules="nameRules" style="width: 100%;"/>
          <div class="row">
            <q-input ref="" outlined v-model="cartao_aux.validade" label="Validade" :dense="dense" lazy-rules :rules="nameRules" style="width: 70%;"/>
            <q-input ref="" outlined v-model="cartao_aux.cvc" label="Cvc" :dense="dense" lazy-rules :rules="nameRules" style="width: 30%;"/>
          </div>
        </q-card-section>

        <q-card-actions>
          <q-btn style="width: 100%; padding: 0;" label="Salvar Cartao" color="positive" v-close-popup @click="SalvarCartao"/>
        </q-card-actions>
      </q-card>
    </q-dialog>
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
import CartaoDataService from 'src/services/CartaoDataService'
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
      aux_usuario: {
        id: '',
        nome: '',
        email: '',
        senha: ''
      },
      conf_senha: '',
      updateInfo: false,
      endereco: {
        id: '',
        user_id: '',
        cep: '',
        num: '',
        logradouro: '',
        cidade: '',
        uf: ''
      },
      updateEndereco: false,
      aux_endereco: {
        id: '',
        user_id: '',
        cep: '',
        num: '',
        logradouro: '',
        cidade: '',
        uf: ''
      },
      addCartao: false,
      editCartao: false,
      cartoes: [],
      cartao: {
        nome: '',
        user_id: 0,
        numero: '',
        validade: '',
        cvc: ''
      },
      cartao_aux: {
        nome: '',
        user_id: 0,
        numero: '',
        validade: '',
        cvc: ''
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
          console.log(this.usuario)
            
        })

      EnderecoDataService.listarPorUsuario(decodedToken['user_id'])
        .then((response) => {
          this.endereco = response.data[0];
        })

      CartaoDataService.listarPorUsuario(decodedToken['user_id'])
        .then((response) => {
          console.log(response)
          this.cartoes = response.data;
        })

    },
    AtualizarEndereco()
    {
      this.aux_endereco.id = this.endereco.id;
      this.aux_endereco.user_id = this.endereco.user_id;
      const data = this.aux_endereco;

      if(this.aux_endereco.length > 2)
        return;

      EnderecoDataService.atualizar(data)
        .then((response) => {
            
        })
    },
    SalvarPerfil()
    {
      let test_nome = /^[a-zA-Z\s]+$/;
      let test_email = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      let test_senha = /^(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[a-z\d@#$!%*?&]{8,}$/i

      if(!test_nome.test(this.aux_usuario.nome))
      {
        alert("Nome Invalido")
        return;
      }
      if(!test_email.test(this.aux_usuario.email))
      {
        alert("Email Invalido")
        return;
      }
      if(this.conf_senha != this.usuario.senha)
      {
        alert("Senha Invalida")
        return;
      }
      if(this.aux_usuario.senha.length == 0)
      {
        this.aux_usuario.senha = this.usuario.senha;
      }
      else
      {
        if(!test_senha.test(this.aux_usuario.senha))
        {
          alert("Nova Senha Invalida")
          return;
        }else
        {
          if(this.conf_senha != this.usuario.senha)
          {
            alert("Senhas não batem")
            return;
          }

          this.aux_usuario.id = this.usuario.id;

        }
      }
      const data = this.aux_usuario;

          UsuarioDataService.atualizar(data)
            .then((response) => {
              this.$router.go(this.$router.currentRoute)

            })
      
    },
    ToggleUpdateInfo()
    {
      this.aux_usuario.id = this.usuario.id;
      this.aux_usuario.nome = this.usuario.nome;
      this.aux_usuario.email = this.usuario.email;
      this.aux_usuario.senha = '';
      this.conf_senha = '';  
      this.updateInfo = !this.updateInfo;
    },
    ToggleUpdateEndereco()
    {
      this.aux_endereco = this.endereco;
      this.updateEndereco = !this.updateEndereco;
    },
    ToggleAddCartao()
    {
      this.addCartao = !this.addCartao;
    },
    ToggleEditCartao(cartao)
    {
      this.editCartao = !this.editCartao;
      this.cartao_aux = cartao;
    },
    SalvarCartao()
    {
      const data = this.cartao_aux

      CartaoDataService.atualizar(data)
        .then((response) => {
          console.log(response)
        })
    },
    CriarCartao()
    {
      const token = localStorage.getItem('jwt');
      if(!token) { return; }

      const decodedToken = jwtDecode(token);

      const data = {
        user_id: decodedToken['user_id'],
        nome: this.cartao.nome,
        numero: this.cartao.numero,
        validade: this.cartao.validade,
        cvc: this.cartao.cvc
      }

      CartaoDataService.cadastrar(data)
      .then((response) => {
        location.reload();
        })
    },
    DeletarCartao(id)
    {
      if(confirm("Tem Certeza que deseja deletar o cartao?"))
      {
        CartaoDataService.deletar(id)
        .then((response) => {
          location.reload();
          })
      }
    }
  },
  mounted()
  {
    this.CarregarDados();
  }
})
</script>
