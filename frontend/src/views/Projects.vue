<template>

  <a href = 'http://127.0.0.1:8000/login' v-if = "this.$route.params.password==None">Login</a>
  <form class="m-5" v-on:submit.prevent='create'>
    <div>
      <input type="text" v-model="name">
    </div>
    <div>
      <input type="text" v-model="description">
    </div>
    <div>
      <input type="file" ref = "file" v-on:change="handleFileUpload()">
    </div>
    <button>Submit</button>
  </form>


  <div v-for="(item, index) in projects">
        <label v-bind:for="index">
          <h2>
            {{item.name}}<br/>
            {{item.description}}<br/>
            <a v-bind:href = "item.file"><img src = "https://vaidyamanager.com/templates/default/img/iconimage/file.png"></a>
            <br/>
          </h2>
          <router-link :to="{ name: 'comments', params: { id_pr: item.id }}">Comments</router-link>
          <button v-bind:id="index" @click="Delete(item.id)">Delete</button>
        </label>
      </div>
</template>

<script>
  import axios from 'axios'
  const API = 'http://127.0.0.1:8000/projects/Project/'
  export default {
    name:'Projects',
    data(){
      return {
        projects: [],
        name: '',
        description: '',
        file: '',
        authors: []
      }
    },
    mounted() {
      console.log(this.$route.params.username);
      console.log(this.$route.params.password);
      this.get_projects();
    },
    methods:{
      get_projects(){
        var vue = this;
        axios({
          method:'GET',
          url: API,
          auth:{
            'username':'Kalm',
            'password':'12345'
          }
        }).then(function(response){
          console.log(response.data);
          vue.projects = response.data;
        }).catch(function(error) {
          console.log(error);
        });
      },
      create(){
        var vue = this
        let formData = new FormData();
        formData.append('name',this.name);
        formData.append('description', this.description);
        formData.append('file',this.file)

        axios.post(
          API,
          formData,
          {
            headers: {
            'Content-Type': 'multipart/form-data'
          },
          auth:{
            'username':'Kalm',
            'password':'12345'
          }
        }).then(function(response){
          console.log(response.data)
          var new_pr = {
            'id': response.data.id,
            'name': response.data.name,
            'description': response.data.description,
            'file': response.data.file
          }

          vue.projects.push(new_pr);
          vue.name = '';
          vue.description = '';
          vue.file = '';
          console.log(vue.projects);
        }).catch(function(error){
          console.log(error);
        });
      },
      handleFileUpload(){
        this.file = this.$refs.file.files[0];
      },
      Delete(id){
        var vue = this;
        axios({
          method: 'DELETE',
          url: API + id + '/',
          auth:{
            'username':'Kalm',
            'password':'12345'
          }
        }).then(function(response){
          console.log('GOOD DELETE');
          vue.get_projects();
        }).catch(function(error) {
          console.log(error);
        });
      }
    }
  }
</script>