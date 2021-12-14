const state = {
    classPlans: [],
    teacherPlans: [],
    classroomPlans: [],
    getClassPlansSuccess: true,
    getClassPlansError: null,
    getTeacherPlansSuccess: true,
    getTeacherPlansError: null,
    getClassroomPlansSuccess: true,
    getClassroomPlansError: null
}

const mutations = {
    'SET_CLASS_PLANS'(state, s) {
        state.classPlans = s
    },
    'GET_CLASS_PLANS_SUCCESS'(state, success) {
        state.getClassPlansSuccess = success
    },
    'GET_CLASS_PLANS_ERROR'(state, error) {
        state.getClassPlansError = error;
    },
    'SET_TEACHER_PLANS'(state, s) {
        state.teacherPlans = s
    },
    'GET_TEACHER_PLANS_SUCCESS'(state, success) {
        state.getTeacherPlansSuccess = success
    },
    'GET_TEACHER_PLANS_ERROR'(state, error) {
        state.getTeacherPlansError = error;
    },
    'SET_CLASSROOM_PLANS'(state, s) {
        state.classPlans = s
    },
    'GET_CLASSROOM_PLANS_SUCCESS'(state, success) {
        state.getClassroomPlansSuccess = success
    },
    'GET_CLASSROOM_PLANS_ERROR'(state, error) {
        state.getClassroomPlansError = error;
    },
}

const getters = {
    getClassPlans: state => {
        return state.classPlans;
    },
    getClassPlansSuccess: state => {
        return state.getClassPlansSuccess;
    },
    getClassPlansError: state => {
        return state.getClassPlansError;
    },
    getTeacherPlans: state => {
        return state.classPlans;
    },
    getTeacherPlansSuccess: state => {
        return state.getTeacherPlansSuccess;
    },
    getTeacherPlansError: state => {
        return state.getTeacherPlansError;
    },
    getClassroomPlans: state => {
        return state.classroomPlans;
    },
    getClassroomPlansSuccess: state => {
        return state.getClassroomPlansSuccess;
    },
    getClassroomPlansError: state => {
        return state.getClassroomPlansError;
    },
}

export default {
    state,
    mutations,
    getters
};