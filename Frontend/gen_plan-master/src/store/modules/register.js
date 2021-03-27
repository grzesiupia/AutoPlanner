const state = {
    registerSuccess: true,
    registerError: null,
    registerVerifySuccess: true,
    registerVerifyError: null,
    resendTokenSuccess: true,
    resendTokenError: null,
    email: ""
};

const mutations = {
    'REGISTER_ERROR'(state, error) {
        state.registerError = error;
    },
    'REGISTER_SUCCESS'(state, success) {
        state.registerSuccess = success
    },
    'REGISTER_VERIFY_ERROR'(state, error) {
        state.registerVerifyError = error;
    },
    'REGISTER_VERIFY_SUCCESS'(state, success) {
        state.registerVerifySuccess = success
    },
    'RESEND_TOKEN_ERROR'(state, error) {
        state.resendTokenError = error;
    },
    'RESEND_TOKEN_SUCCESS'(state, success) {
        state.resendTokenSuccess = success
    },
    'SET_EMAIL'(state, email) {
        state.email = email
    },
}

const getters = {
    getRegisterSuccess: state => {
        return state.registerSuccess;
    },
    getRegisterError: state => {
        return state.registerError;
    },
    getRegisterVerifySuccess: state => {
        return state.registerVerifySuccess;
    },
    getRegisterVerifyError: state => {
        return state.registerVerifyError;
    },
    getResendTokenSuccess: state => {
        return state.resendTokenSuccess;
    },
    getResendTokenError: state => {
        return state.resendTokenError;
    },
    getEmail: state => {
        return state.email;
    },
}

export default {
    state,
    mutations,
    getters
};