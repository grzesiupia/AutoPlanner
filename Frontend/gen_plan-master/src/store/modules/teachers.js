const state = {
    teachers: [],
    teacher:{},
    addTeacherSuccess: true,
    addTeacherError: null,
    editTeacherSuccess: true,
    editTeacherError: null,
    getTeachersSuccess: true,
    getTeachersError: null
}

const mutations = {
    'SET_TEACHERS'(state, s) {
        state.teachers = s
    },
    'SET_TEACHER'(state, s) {
        state.teacher = s
    },
    'ADD_TEACHER_SUCCESS'(state, success) {
        state.addTeacherSuccess = success
    },
    'ADD_TEACHER_ERROR'(state, error) {
        state.addTeacherError = error;
    },
    'EDIT_TEACHER_SUCCESS'(state, success) {
        state.editTeacherSuccess = success
    },
    'EDIT_TEACHER_ERROR'(state, error) {
        state.editTeacherError = error;
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
    getTeacher: state => {
        return state.teacher;
    },
    getAddTeacherSuccess: state => {
        return state.addTeacherSuccess;
    },
    getAddTeacherError: state => {
        return state.addTeacherError;
    },
    getEditTeacherSuccess: state => {
        return state.editTeacherSuccess;
    },
    getEditTeacherError: state => {
        return state.ditTeacherError;
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