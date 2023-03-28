import http from '../http-common'

class MangaDataService {
  obter (id) {
    return http.get(`/manga/${id}`)
  }

  listar () {
    return http.get('/manga')
  }

  listarPorUsuario(id) {
    return http.get(`/manga/usuario/${id}`)
  }

  cadastrar (manga) {
    return http.post('/manga', manga)
  }

  atualizar (manga) {
    return http.put('/manga', manga)
  }

  async deletar (id) {
    return await http.delete(`/manga/${id}`)
  }
}

export default new MangaDataService()
