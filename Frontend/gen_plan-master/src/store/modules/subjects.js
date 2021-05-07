const state = {
    subjects: [],
    addSubjectSuccess: true,
    addSubjectError: null,
    getSubjectsSuccess: true,
    getSubjectsError: null
}

const mutations = {
    'SET_SUBJECTS'(state, s) {
        state.subjects = s
    },
    'ADD_SUBJECT_SUCCESS'(state, success) {
        state.addSubjectSuccess = success
    },
    'ADD_SUBJECT_ERROR'(state, error) {
        state.addSubjectError = error;
    },
    'GET_SUBJECTS_SUCCESS'(state, success) {
        state.getSubjectsSuccess = success
    },
    'GET_SUBJECTS_ERROR'(state, error) {
        state.getSubjectsError = error;
    },
    
}

const getters = {
    getSubjects: state => {
        return state.subjects;
    },
    getAddSubjectSuccess: state => {
        return state.addSubjectSuccess;
    },
    getAddSubjectError: state => {
        return state.addSubjectError;
    },
    getSubjectsSuccess: state => {
        return state.getSubjectsSuccess;
    },
    getSubjectsError: state => {
        return state.getSubjectsError;
    },
}

export default {
    state,
    mutations,
    getters
};