import axios from 'axios'

const FRIDGE_URL = 'http://fridge.mckenzie-house.com'
const FRIDGE_API_URL = `${FRIDGE_URL}/api`

class ItemDataService {

    retrieveAllItems() {
        return axios.get(`${FRIDGE_API_URL}/items`);
    }

    deleteItem(id) {
        //console.log('executed service')
        return axios.delete(`${FRIDGE_API_URL}/items/${id}`);
    }

    retrieveItem(id) {
        return axios.get(`${FRIDGE_API_URL}/items/${id}`);
    }

    updateItem(id, item) {
        return axios.put(`${FRIDGE_API_URL}/items/${id}`, item);
    }
  
    createItem(item) {
        return axios.post(`${FRIDGE_API_URL}/items`, item);
    }
}

export default new ItemDataService()