const state = {
    classes: [],
    addClassSuccess: true,
    addClassError: null,
    getClasssSuccess: true,
    getClasssError: null
}

const mutations = {
    'SET_CLASSES'(state, s) {
        state.Clasess = s
    },
    'ADD_CLASS_SUCCESS'(state, success) {
        state.addClassSuccess = success
    },
    'ADD_CLASS_ERROR'(state, error) {
        state.addClassError = error;
    },
    'GET_CLASSES_SUCCESS'(state, success) {
        state.getClassesSuccess = success
    },
    'GET_CLASSES_ERROR'(state, error) {
        state.getClassesError = error;
    },
    
}

const getters = {
    getClasses: state => {
        return state.classes;
    },
    getAddClassSuccess: state => {
        return state.addClassSuccess;
    },
    getAddClassError: state => {
        return state.addClassError;
    },
    getClassesSuccess: state => {
        return state.getClassesSuccess;
    },
    getClassesError: state => {
        return state.getClassesError;
    },
}

export default {
    state,
    mutations,
    getters
};