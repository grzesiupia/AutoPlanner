import axios from 'axios'

export const URL = "http://3.120.208.16:8000/" //URL serwera

export default axios.create({
    baseURL: URL
})
