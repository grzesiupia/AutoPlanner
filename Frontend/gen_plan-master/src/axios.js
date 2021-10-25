import axios from 'axios'

export const URL = "http://18.185.102.150:8000/" //URL serwera

export default axios.create({
    baseURL: URL
})