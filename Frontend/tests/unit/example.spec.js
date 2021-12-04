import login from '../../src/store/modules/login'
import store from '../../src/store'

describe('mutations', () => {
  test('setToken', () => {
    const token = "abcd"
    const state = {
      token: ""
    }
    store.commit('SET_TOKEN', { token })
    expect(store.getters.getToken.token).toBe(token)
  }),
  test('setUserId', () => {
    const UserId = "abcd"
    const state = {
      token: ""
    }
    store.commit('SET_USERID', { UserId })
    expect(store.getters.getUserId.UserId).toBe(UserId)
  })
},
)
