const state = {
    token: window.localStorage.getItem('token'),
    UserId: window.localStorage.getItem('UserId'),
    success: true,
    error: null,
    isLogged: window.localStorage.getItem('token') ? true : false,
    sendPinSuccess: true,
    sendPinError: null,
    newPassSuccess: true,
    newPassError: null,
};

const mutations = {
    'SET_TOKEN'(state, token) {
        state.token = token;
    },
    'SET_USERID'(state, id) {
        state.UserId = id;
    },
    'LOGIN_ERROR'(state, error) {
        state.error = error;
    },
    'LOGIN_SUCCESS'(state, success) {
        state.success = success
        if(success== true)
        {
        state.isLogged = true
        }
    },
    'LOGOUT'(state, success) {
        state.logoutSuccess = success
        state.isLogged = false
        window.localStorage.removeItem('token')
        window.localStorage.removeItem('UserId')
    },
    'SEND_PIN_SUCCESS'(state, success)
    {
        state.sendPinSuccess=success
    },
    'SEND_PIN_ERROR'(state, error)
    {
        state.sendPinError=error
    },
    'NEW_PASS_SUCCESS'(state, success)
    {
        state.newPassSuccess=success
    },
    'NEW_PASS_ERROR'(state, error)
    {
        state.newPassError=error
    }
}

const getters = {
    getToken: state => {
        return state.token;
    },
    getUserId: state => {
        return state.UserId;
    },
    getLoginSuccess: state => {
        return state.success;
    },
    getLoginError: state => {
        return state.error;
    },
    getIsLogged: state => {
        return state.isLogged;
    },
    getSendPinSuccess: state => {
        return state.sendPinSuccess;
    },
    getSendPinError: state => {
        return state.sendPinError;
    },
    getNewPassSuccess: state => {
        return state.newPassSuccess;
    },
    getNewPassError: state => {
        return state.newPassError;
    },
}
export default {
    state,
    mutations,
    getters
};