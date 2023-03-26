import http from '../http-common'

class CartaoDataService {
  obter (id) {
    return http.get(`/cartao/${id}`)
  }

  listar () {
    return http.get('/cartao/')
  }

  listarPorUsuario(id) {
    return http.get(`/cartao/usuario/${id}`)
  }

  cadastrar (cartao) {
    return http.post('/cartao', cartao)
  }

  atualizar (cartao) {
    return http.put('/cartao', cartao)
  }

  async deletar (id) {
    return await http.delete(`/cartao/${id}`)
  }
}

export default new CartaoDataService()
