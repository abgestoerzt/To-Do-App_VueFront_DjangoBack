<template>
  <div class="hello">
    <h1>To-Do-App</h1>
  </div>
</template>

<script>

import axios from 'axios';

export default {
  name: 'ToDoApp',

  mounted () {
    axios.get('http://127.0.0.1:8000/todo/'
   
      )
      .then(response => {
        this.response = response.data
        console.log(response.data)
      })
      .catch(error => {
        console.error(error)
      })
  }
 
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
