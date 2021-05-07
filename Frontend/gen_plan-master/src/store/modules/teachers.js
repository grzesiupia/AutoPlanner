const state = {
    teachers: [],
    addTeacherSuccess: true,
    addTeacherError: null,
    getTeachersSuccess: true,
    getTeachersError: null
}

const mutations = {
    'SET_TEACHERS'(state, s) {
        state.teachers = s
    },
    'ADD_TEACHER_SUCCESS'(state, success) {
        state.addTeacherSuccess = success
    },
    'ADD_TEACHER_ERROR'(state, error) {
        state.addTeacherError = error;
    },
    'GET_TEACHERS_SUCCESS'(state, success) {
        state.getTeachersSuccess = success
    },
    'GET_TEACHERS_ERROR'(state, error) {
        state.getTeachersError = error;
    },
    
}

const getters = {
    getTeachers: state => {
        return state.teachers;
    },
    getAddTeacherSuccess: state => {
        return state.addTeacherSuccess;
    },
    getAddTeacherError: state => {
        return state.addTeacherError;
    },
    getTeachersSuccess: state => {
        return state.getTeachersSuccess;
    },
    getTeachersError: state => {
        return state.getTeachersError;
    },
}

export default {
    state,
    mutations,
    getters
};