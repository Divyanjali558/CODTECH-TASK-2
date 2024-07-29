<template>
  <div>
    <h1>Recipes</h1>
    <ul>
      <li v-for="recipe in recipes" :key="recipe.id">
        <router-link :to="'/recipes/' + recipe.id">{{ recipe.title }}</router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      recipes: []
    };
  },
  created() {
    axios.get('/recipes').then(response => {
      this.recipes = response.data;
    });
  }
};
</script>
