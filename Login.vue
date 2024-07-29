<template>
  <div>
    <h1>Login</h1>
    <form @submit.prevent="login">
      <input v-model="email" type="email" placeholder="Email">
      <input v-model="password" type="password" placeholder="Password">
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
import { useStore } from 'vuex';

export default {

  data() {
    return {
      email: '',
      password: ''
    };
  },
  setup() {
    const store = useStore();

    const login = async () => {
      try {
        const response = await axios.post('/login', {
          email: this.email,
          password: this.password
        });
        store.dispatch('login', { user: response.data.user, token: response.data.token });
        axios.defaults.headers.common['Authorization'] = `Bearer ${response.data.token}`;
        this.$router.push('/');
      } catch (error) {
        console.error('Login failed:', error);
      }
    };

    return { login };
  }
};
</script>
