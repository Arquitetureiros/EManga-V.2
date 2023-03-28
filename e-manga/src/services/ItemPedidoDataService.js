import http from '../http-common'

class ItemPedidoDataService {
  obter (id) {
    return http.get(`/itempedido/${id}`)
  }

  listar () {
    return http.get('/itempedido')
  }

  listarPorPedido(id) {
    return http.get(`/itempedido/pedido/${id}`)
  }

  obterManga(id) {
    return http.get(`/itempedido/manga/${id}`)
  }

  cadastrar (itempedido) {
    return http.post('/itempedido', itempedido)
  }

  atualizar (itempedido) {
    return http.put('/itempedido', itempedido)
  }

  async deletar (id) {
    return await http.delete(`/itempedido/${id}`)
  }
}

export default new ItemPedidoDataService()
