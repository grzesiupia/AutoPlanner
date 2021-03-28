import axios from 'axios'

export const URL = "http://127.0.0.1:8000/" //URL serwera

export default axios.create({
    baseURL: URL
})