import axios from 'axios'

export const URL = "http://123.12.123.12:1234/" //URL serwera

export default axios.create({
    baseURL: URL
})