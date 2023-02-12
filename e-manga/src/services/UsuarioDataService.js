import http from '../http-common'

class ClienteDataService {
  obterPorId (id) {
    return http.get(`/usuario/${id}`)
  }

  listar () {
    return http.get('/usuario/')
  }

  cadastrar (cliente) {
    return http.post('/usuario', cliente)
  }

  atualizar (id, cliente) {
    return http.put('/usuario/', cliente)
  }

  async deletar (id) {
    return await http.delete(`/usuario/${id}`)
  }
}

export default new ClienteDataService()
