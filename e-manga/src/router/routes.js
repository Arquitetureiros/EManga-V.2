
const routes = [
  {
    path: '/',
    component: () => import('pages/BuscaProduto.vue')
    // children: [
    //   { path: '', component: () => import('pages/IndexPage.vue') }
    // ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/pagamentos',
    component: () => import('pages/IndexPagamento.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/cadastro',
    component: () => import('src/pages/Cadastro.vue')
  },
  {
    path: '/manterManga',
    component: () => import('pages/ManterManga.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/meusProdutos',
    component: () => import('pages/meusProdutos.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/acompanharpedido',
    component: () => import('pages/AcompanharPedido.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/buscar',
    component: () => import('pages/BuscaProduto.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/login',
    component: () => import('pages/Login.vue')
  },
  {
    path: '/editarperfil',
    component: () => import('pages/EditarPerfil.vue'),
    meta: { requiresAuth: true }
  }
]

export default routes
