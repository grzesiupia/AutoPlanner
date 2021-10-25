const state = {
    subjects: [],
    addSubjectSuccess: true,
    addSubjectError: null,
    editSubjectSuccess: true,
    editSubjectError: null,
    deleteSubjectSuccess: true,
    deleteSubjectError: null,
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
    'EDIT_SUBJECT_SUCCESS'(state, success) {
        state.editSubjectSuccess = success
    },
    'EDIT_SUBJECT_ERROR'(state, error) {
        state.editSubjectError = error;
    },
    'DELETE_SUBJECT_SUCCESS'(state, success) {
        state.deleteSubjectSuccess = success
    },
    'DELETE_SUBJECT_ERROR'(state, error) {
        state.deleteSubjectError = error;
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
    getEditSubjectSuccess: state => {
        return state.editSubjectSuccess;
    },
    getEditSubjectError: state => {
        return state.editSubjectError;
    },
    getDeleteSubjectSuccess: state => {
        return state.deleteSubjectSuccess;
    },
    getDeleteSubjectError: state => {
        return state.deleteSubjectError;
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