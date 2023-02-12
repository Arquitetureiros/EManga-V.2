import http from '../http-common'

class ClienteDataService {
  obterPorId (id) {
    return http.get(`/cliente/${id}`)
  }

  listar () {
    return http.get('/cliente/')
  }

  cadastrar (cliente) {
    return http.post('/cliente', cliente)
  }

  atualizar (id, cliente) {
    return http.put('/cliente/', cliente)
  }

  async deletar (id) {
    return await http.delete(`/cliente/${id}`)
  }
}

export default new ClienteDataService()
