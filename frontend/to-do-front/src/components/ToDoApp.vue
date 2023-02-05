<template>
  <div class="hello">
    <h1>To-Do-App</h1>
    <div>
    <ul>
      <li v-for="item in response" :key="item.id">{{ item.name }} {{ item.id }}
        <button @click="deleteItem(item.id)">Delete</button>
      
      </li>
    </ul>
  
  </div>



  <div>

    <form @submit.prevent="submitForm">
      <input type="text" v-model="to_do_name">
      <button type="submit">Submit</button>


    </form>
   
  </div>


  </div>



</template>

<script>

import axios from 'axios';

export default {
  name: 'ToDoApp',
  data () {
    return {
      response: null,
      to_do_name: null,

    }
  },

  mounted () {
    this.fetchData()
  },
  methods: {
    submitForm() {
      axios.post('http://127.0.0.1:8000/todo/', {
        name: this.to_do_name
      })
        .then(response => {
          console.log(response.data)
          this.fetchData()
        })
        .catch(error => {
          console.error(error)
        })
    },
    fetchData(){
      axios.get('http://127.0.0.1:8000/todo/'
   
      )
      .then(response => {
        this.response = response.data
        console.log(response.data)
        
      })
      .catch(error => {
        console.error(error)
      })

    },
    deleteItem(id) {
      axios.delete(`http://127.0.0.1:8000/todo/${id}`)
        .then(response => {
          console.log(response.data)
          this.fetchData()
        })
        .catch(error => {
          console.error(error)
        })
    }
  }
 
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: kannada;
  padding: 0;
}
li {
  display: list-item;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
