const state = {
    classes: [],
    class: {},
    addClassSuccess: true,
    addClassError: null,
    editClassSuccess: true,
    editClassError: null,
    getClasssSuccess: true,
    getClasssError: null
}

const mutations = {
    'SET_CLASSES'(state, s) {
        state.Clasess = s
    },
    'SET_CLASS'(state, s) {
        state.Class = s
    },
    'ADD_CLASS_SUCCESS'(state, success) {
        state.addClassSuccess = success
    },
    'ADD_CLASS_ERROR'(state, error) {
        state.addClassError = error;
    },
    'EDIT_CLASS_SUCCESS'(state, success) {
        state.editClassSuccess = success
    },
    'EDIT_CLASS_ERROR'(state, error) {
        state.editClassError = error;
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
    getClass: state => {
        return state.class;
    },
    getAddClassSuccess: state => {
        return state.addClassSuccess;
    },
    getAddClassError: state => {
        return state.addClassError;
    },
    getEditClassSuccess: state => {
        return state.editClassSuccess;
    },
    getEditClassError: state => {
        return state.editClassError;
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