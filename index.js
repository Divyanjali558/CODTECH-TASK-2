import { createStore } from 'vuex';

export default createStore({
  state: {
    user: null,
    token: null
  },
  mutations: {
    setUser(state, user) {
      state.user = user;
    },
    setToken(state, token) {
      state.token = token;
    }
  },
  actions: {
    login({ commit }, userData) {
      commit('setUser', userData.user);
      commit('setToken', userData.token);
    },
    logout({ commit }) {
      commit('setUser', null);
      commit('setToken', null);
    }
  },
  modules: {}
});
