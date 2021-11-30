const state = {
    classrooms: [],
    classroom:{},
    addClassroomSuccess: true,
    addClassroomError: null,
    editClassroomSuccess: true,
    editClassroomError: null,
    deleteClassroomSuccess: true,
    deleteClassroomError: null,
    getClassroomsSuccess: true,
    getClassroomsError: null
}

const mutations = {
    'SET_CLASSROOMS'(state, s) {
        state.classrooms = s
    },
    'SET_CLASSROOM'(state, s) {
        state.classroom = s
    },
    'ADD_CLASSROOM_SUCCESS'(state, success) {
        state.addClassroomSuccess = success
    },
    'ADD_CLASSROOM_ERROR'(state, error) {
        state.addClassroomError = error;
    },
    'EDIT_CLASSROOM_SUCCESS'(state, success) {
        state.editClassroomSuccess = success
    },
    'EDIT_CLASSROOM_ERROR'(state, error) {
        state.editClassroomError = error;
    },
    'DELETE_CLASSROOM_SUCCESS'(state, success) {
        state.deleteClassroomSuccess = success
    },
    'DELETE_CLASSROOM_ERROR'(state, error) {
        state.deleteClassroomError = error;
    },
    'GET_CLASSROOMS_SUCCESS'(state, success) {
        state.getClassroomsSuccess = success
    },
    'GET_CLASSROOMS_ERROR'(state, error) {
        state.getClassroomsError = error;
    },
    
}

const getters = {
    getClassrooms: state => {
        return state.classrooms;
    },
    getClassroom: state => {
        return state.classroom;
    },
    getAddClassroomSuccess: state => {
        return state.addClassroomSuccess;
    },
    getAddClassroomError: state => {
        return state.addClassroomError;
    },
    getEditClassroomSuccess: state => {
        return state.editClassroomSuccess;
    },
    getEditClassroomError: state => {
        return state.editClassroomError;
    },
    getDeleteClassroomSuccess: state => {
        return state.deleteClassroomSuccess;
    },
    getDeleteClassroomError: state => {
        return state.deleteClassroomError;
    },
    getClassroomsSuccess: state => {
        return state.getClassroomsSuccess;
    },
    getClassroomsError: state => {
        return state.getClassroomsError;
    },
}

export default {
    state,
    mutations,
    getters
};