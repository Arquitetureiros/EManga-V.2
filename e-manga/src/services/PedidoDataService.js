import http from '../http-common'

class PedidoDataService {
  obter (id) {
    return http.get(`/pedido/${id}`)
  }

  listar () {
    return http.get('/pedido')
  }

  listarPorUsuario(id) {
    return http.get(`/pedido/usuario/${id}`)
  }

  cadastrar (pedido) {
    return http.post('/pedido', pedido)
  }

  atualizar (pedido) {
    return http.put('/pedido', pedido)
  }

  async deletar (id) {
    return await http.delete(`/pedido/${id}`)
  }
}

export default new PedidoDataService()
