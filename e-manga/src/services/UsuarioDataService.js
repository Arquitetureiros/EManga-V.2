import http from '../http-common'

class UsuarioDataService {
  obter (id) {
    return http.get(`/usuario/${id}`)
  }

  listar () {
    return http.get('/usuario/')
  }

  cadastrar (usuario) {
    return http.post('/usuario', usuario)
  }

  atualizar (usuario) {
    return http.put('/usuario', usuario)
  }

  async deletar (id) {
    return await http.delete(`/usuario/${id}`)
  }

  logar (usuario) {
    return http.post('/login/', usuario)
  }
}

export default new UsuarioDataService()
