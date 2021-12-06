import axios from 'axios'

export const URL = "http://3.68.195.5:8000/" //URL serwera

export default axios.create({
    baseURL: URL
})