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

  cadastrar (usuario) {
    return http.post('/endereco', usuario)
  }

  atualizar (id, usuario) {
    return http.put('/endereco/', usuario)
  }

  async deletar (id) {
    return await http.delete(`/endereco/${id}`)
  }
}

export default new EnderecoDataService()
