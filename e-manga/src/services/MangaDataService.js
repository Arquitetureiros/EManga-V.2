import http from '../http-common'

class MangaDataService {
  obterPorId (id) {
    return http.get(`/manga/${id}`)
  }

  listar () {
    return http.get('/manga/')
  }

  cadastrar (manga) {
    return http.post('/manga', manga)
  }

  atualizar (id, manga) {
    return http.put('/manga/', manga)
  }

  async deletar (id) {
    return await http.delete(`/manga/${id}`)
  }
}

export default new MangaDataService()
