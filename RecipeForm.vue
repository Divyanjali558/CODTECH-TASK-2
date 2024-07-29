<template>
  <div>
    <h1>Create Recipe</h1>
    <form @submit.prevent="createRecipe">
      <input v-model="title" type="text" placeholder="Title">
      <textarea v-model="description" placeholder="Description"></textarea>
      <button type="submit">Create</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      title: '',
      description: ''
    };
  },
  methods: {
    async createRecipe() {
      try {
        await axios.post('/recipes', {
          title: this.title,
          description: this.description
        });
        this.$router.push('/');
      } catch (error) {
        console.error('Creation failed:', error);
      }
    }
  }
};
</script>
