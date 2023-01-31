<template>
  <q-layout view="lHh Lpr lFf">
     <q-header elevated>
        <ToolbarMenu @leftDrawer="toggleLeftDrawer"/>
     </q-header>
     <q-page-container>
        <div class="q-pa-xl">
           <div>
              <div class="text-h4">
                Carrinho
              </div>
              <div class="row justify-between">
                 <div v-if="itensCarrinho" class="col-5">
                    <q-card class="q-py-lg q-px-sm" bordered>
                       <q-scroll-area style="height: 700px; max-width: 760px;">
                          <span class="q-px-sm">Quantidade de itens: {{itensCarrinho.length}}</span>
                          <div class="row">
                             <div class="col-11 q-pa-sm" v-for="(product, p) in itensCarrinho" :key="p">
                                <q-card bordered>
                                   <q-card-section horizontal>
                                      <div class="row">
                                         <q-checkbox
                                          v-model="product.inOrder"
                                          />
                                         <q-img
                                         class="q-my-md"
                                         :src="product.url_image"
                                         style="height: 200px; width: 150px"
                                         />
                                         <div class="col q-pa-md " >
                                            <span class="text-h6">{{product.name}}</span>
                                            <p class="text-subtitle1" style="opacity: 0.7"> Vendido por: {{ product.owner}} </p>
                                            <span class="text-subtitle1" style="opacity: 0.7"> {{ product.city }}, {{ product.cd_uf }}</span>
                                            <div class="row q-pt-xl">
                                               <q-input
                                               v-model.number="qtd"
                                               dense
                                               type="number"
                                               outlined
                                               style="max-width: 200px,
                                               max-height: 10px;"
                                               label="Quantidade"
                                               />
                                               <div class="col q-px-md">
                                                <span>Valor unitário: </span>
                                                <span class="text-positive">R${{valor}}</span><br>
                                                <span>Valor total: </span>
                                                <span class="text-positive">R${{valor*qtd}}</span>
                                              </div>
                                            </div>
                                         </div>
                                      </div>
                                   </q-card-section>
                                </q-card>
                             </div>
                          </div>
                       </q-scroll-area>
                    </q-card>
                 </div>
                 <div class="col-3">
                    <div class="row ">
                       <div class="col-12">
                          <q-card class="q-pa-md">
                             <div>
                                <div class="text-h6">Endereço de entrega:</div>
                                <q-card-section class="text-body1">
                                   Rua dos Bobos, 0, Formiga - Minas Gerais<br>                        CEP 42069-123
                                   <q-btn flat dense color="primary" icon="edit">
                                      <q-tooltip>Editar</q-tooltip>
                                   </q-btn>
                                </q-card-section>
                             </div>
                             <div>
                                <p class="text-h6">Opções de Frete:</p>
                                <q-radio v-model="opFrete" val=8.00 label="PAC" color="green" />
                                <span class="text-positive"> R$8,00</span><br>
                                <q-radio v-model="opFrete" val=18.00 label="SEDEX" color="green" />
                                <span class="text-positive"> R$18,00</span>
                             </div>
                             <div class="text-h6">Total: <span class="text-positive">R$ {{total()}}</span></div>
                          </q-card>
                          <q-btn class="q-my-md float-left" @click="formaPagamento = !formaPagamento" color="primary">Finalizar pedido</q-btn>
                       </div>
                       <div v-if="formaPagamento" class="col-12">
                          <div class="row">
                             <span class="text-h6"> Forma de Pagamento </span>
                             <q-tabs                  v-model="tab"                  class="text-primary"                >
                                <q-tab name="card" icon="fa-solid fa-credit-card" label="Cartão" />
                                <q-tab name="boleto" icon="fa-solid fa-barcode" label="Boleto" />
                                <q-tab name="pix" icon="fa-solid fa-qrcode" label="Pix" />
                             </q-tabs>
                          </div>
                          <div v-if="tab == 'pix'">
                             <div class="row justify-start q-pa-md">
                                <div class="col-12">
                                   <q-img src="public/qrcode_pix.png" style="height: 150px; width: 150px;"/>
                                </div>
                                <div class="col-12">
                                   <q-btn icon="fa-regular fa-copy" class="col-2 q-hoverable" @click="copyText()" flat dense color="grey" label="Copiar qr code"/>
                                </div>
                             </div>
                             <li>Escaneie o QR Code para realizar o pagamento</li>
                             <li>O pedido será processado quando o pagamento for confirmado</li>
                          </div>
                          <div v-if="tab == 'card'">
                             <div class="row">
                                <div class="col-9 q-pr-sm q-py-md">
                                   <q-input outlined v-model="dadosCartao.nr_cartao" dense color="primary" mask="#### #### #### ####" label="Número do cartao" />
                                </div>
                                <div class="col-3 q-py-md">
                                   <q-input outlined v-model="dadosCartao.nr_cvv" dense color="primary"  mask="###" label="CVV" />
                                </div>
                                <div class="col-3">
                                   <q-input outlined v-model="dadosCartao.dt_validade" dense color="primary"  mask="##/##" label="MM/YY" />
                                </div>
                                <div class="col-9 q-pl-sm">
                                   <q-input outlined v-model="dadosCartao.nm_pessoa" dense color="primary" label="Nome no cartao" />
                                </div>
                             </div>
                             <q-btn class="q-my-md float-left" @click="efetuarPagamento" color="primary">Efetuar pagamento</q-btn>
                          </div>
                          <div v-if="tab == 'boleto'">
                             <div class="text-h6">                    Boleto                  </div>
                          </div>
                       </div>
                    </div>
                 </div>
              </div>
              <div>        </div>
           </div>
        </div>
     </q-page-container>
     <q-drawer      v-model="leftDrawerOpen"      show-if-above      bordered    >
        <q-list>
           <q-item-label          header        >        Opções        </q-item-label>
           <EssentialLink        />
        </q-list>
     </q-drawer>
  </q-layout>
</template>
<script>
import { defineComponent, ref, onMounted } from 'vue'
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
    const img = ref('https://images-na.ssl-images-amazon.com/images/I/71bELfIWTDL.jpg')
    const item = ref('My Hero Academia Vol. 1')
    const val = ref([])
    const vendedor = ref('Valentas Mangas Express')
    const qtd = ref(1)
    const valor = ref(14.90)
    const tab = ref('card')
    const opFrete = ref(0)
    const itensCarrinho = ref([])
    const qrcodeemv = ref('abcnmaskskdjsakdas123')
    const formaPagamento = ref(false)
    const dadosCartao = ref({
      nr_cartao: null,
      nm_pessoa: null,
      dt_validade: null,
      nr_cvv: null
    })
    function total () {
      const vltotal = ((valor.value * qtd.value) + parseFloat(opFrete.value))
      return vltotal
    }
    function efetuarPagamento () {
      console.log(dadosCartao)
    }
    function copyText () {
      const storage = document.createElement('textarea')
      document.body.appendChild(storage)
      storage.value = qrcodeemv.value
      storage.select()
      document.execCommand('copy')
      document.body.removeChild(storage)
    }
    onMounted(() => {
      itensCarrinho.value = JSON.parse(localStorage.getItem('cartProducts'))
      console.log(itensCarrinho.value)
    })
    return {
      leftDrawerOpen,
      toggleLeftDrawer () {
        leftDrawerOpen.value = !leftDrawerOpen.value
      },
      efetuarPagamento,
      itensCarrinho,
      nrItens,
      img,
      item,
      val,
      vendedor,
      qtd,
      valor,
      tab,
      opFrete,
      total,
      formaPagamento,
      dadosCartao,
      copyText,
      qrcodeemv
    }
  }
})
</script>
