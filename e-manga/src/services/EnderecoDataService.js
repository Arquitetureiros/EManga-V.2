import http from '../http-common'

class EnderecoDataService {
  obter (id) {
    return http.get(`/endereco/${id}`)
  }

  listar () {
    return http.get('/endereco/')
  }

  listarPorUsuario(id) {
    return http.get(`/endereco/usuario/${id}`)
  }

  cadastrar (endereco) {
    return http.post('/endereco', endereco)
  }

  atualizar (endereco) {
    return http.put('/endereco', endereco)
  }

  async deletar (id) {
    return await http.delete(`/endereco/${id}`)
  }
}

export default new EnderecoDataService()
