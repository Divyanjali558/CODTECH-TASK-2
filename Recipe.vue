<template>
  <div>
    <h1>{{ recipe.title }}</h1>
    <p>{{ recipe.description }}</p>
    <button @click="editRecipe">Edit</button>
    <button @click="deleteRecipe">Delete</button>
    <form v-if="editing" @submit.prevent="updateRecipe">
      <input v-model="title" type="text" placeholder="Title">
      <textarea v-model="description" placeholder="Description"></textarea>
      <button type="submit">Update</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  props: ['id'],
  data() {
    return {
      recipe: {},
      editing: false,
      title: '',
      description: ''
    };
  },
  created() {
    axios.get(`/recipes/${this.id}`).then(response => {
      this.recipe = response.data;
      this.title = this.recipe.title;
      this.description = this.recipe.description;
    });
  },
  methods: {
    editRecipe() {
      this.editing = true;
    },
    async updateRecipe() {
      try {
        await axios.put(`/recipes/${this.id}`, {
          title: this.title,
          description: this.description
        });
        this.recipe.title = this.title;
        this.recipe.description = this.description;
        this.editing = false;
      } catch (error) {
        console.error('Update failed:', error);
      }
    },
    async deleteRecipe() {
      try {
        await axios.delete(`/recipes/${this.id}`);
        this.$router.push('/');
      } catch (error) {
        console.error('Delete failed:', error);
      }
    }
  }
};
</script>
