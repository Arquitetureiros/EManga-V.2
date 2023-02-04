
const routes = [
  {
    path: '/',
    component: () => import('pages/TelaInicial.vue')
    // children: [
    //   { path: '', component: () => import('pages/IndexPage.vue') }
    // ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue')
  },
  {
    path: '/pagamentos',
    component: () => import('pages/IndexPagamento.vue')
  },
  {
    path: '/login',
    component: () => import('pages/logarSistema.vue')
  },
  {
    path: '/manterManga',
    component: () => import('pages/ManterManga.vue')
  },
  {
    path: '/meusProdutos',
    component: () => import('pages/meusProdutos.vue')
  },
  {
    path: '/acompanharpedido',
    component: () => import('pages/AcompanharPedido.vue')
  },
  {
    path: '/buscar',
    component: () => import('pages/BuscaProduto.vue')
  },
  {
    path: '/verManga',
    component: () => import('pages/verManga.vue')
  },
  {
    path: '/editarManga',
    component: () => import('pages/editarManga.vue')
  }
]

export default routes
