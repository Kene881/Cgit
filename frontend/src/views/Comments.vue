<template>
    <div v-for = "(item, index) in comments">
        <label v-bind:for="index">
          <h2 v-if = "item.project == this.$route.params.id_pr">
            ::{{item.content}}<br/>
            {{item.author}}<br/>
            {{item.project}}<br/>
          </h2>
        </label>
    </div>
</template>

<script>
    import axios from 'axios'
    const API = 'http://127.0.0.1:8000/comments/Comments/'

    export default{
        name:'AppComments',
        data(){
            return {
                comments:[],
                author: '',
                project: '',
                content: ''
            }
        },
        mounted() {
            console.log(this.$route.params.id_pr);
            this.get_comments()
        },
        methods:{
            get_comments(){
                var vue = this;
                axios({
                    url: API,
                    method: 'GET'
                }).then(function(response){
                    console.log(response.data)
                    vue.comments = response.data
                }).catch(function(error) {
                    console.log(error);
                });
            }
        }
    }
</script>