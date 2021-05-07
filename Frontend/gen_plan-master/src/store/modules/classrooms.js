const state = {
    classrooms: [],
    addClassroomSuccess: true,
    addClassroomError: null,
    getClassroomsSuccess: true,
    getClassroomsError: null
}

const mutations = {
    'SET_CLASSROOMS'(state, s) {
        state.classrooms = s
    },
    'ADD_CLASSROOM_SUCCESS'(state, success) {
        state.addClassroomSuccess = success
    },
    'ADD_CLASSROOM_ERROR'(state, error) {
        state.addClassroomError = error;
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
    getAddClassroomSuccess: state => {
        return state.addClassroomSuccess;
    },
    getAddClassroomError: state => {
        return state.addClassroomError;
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