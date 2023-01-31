<template>
    <div class="div" >
        
    <NavBar v-bind:login=login_flag />

    <div class="container mt-5 mx-5" style="max-width:600px;justify-content: center;">
        <div class="input-group mb-3">
            <span class="input-group-text" id="basic-addon1"><strong>@</strong></span>
            <input type="text" class="form-control form-control-lg" placeholder="Search here to make new friends..." aria-label="" aria-describedby="button-addon2" v-model="username">
            <button class="btn btn-success btn-lg" type="button" id="button-addon2" @click="search_user()">Search</button>
    </div>


</div>
        <div class="container my-5" >
            <table class="table table-dark table-striped">
                <thead>
                <tr>
                <th class="text-center" scope="col"><h5>#</h5></th>
                <th class="text-center" colspan="5" scope="col"><h5>Username</h5></th>
                <th class="text-center" scope="col"><h5>Options</h5></th>
                </tr>
            </thead>
            <tbody>
                <tr class="table mx-3" v-for="(user,index) in search_list" :key="index">
                    <th  class="text-center" scope="row">{{index+1  }}</th>
                    <td colspan="5" class="fs-5 text-center"  style="word-wrap: break-word;min-width: 160px;max-width: 160px;">@{{user.username}}</td>
                    <td class="text-center">
                        <button  :class="{
                            'btn btn-success mx-3 mt-1': !user.following,
                            'btn btn-success mx-3 mt-1 disabled': user.following,}" 
                            @click="follow_user(user.username)">Follow</button>
                        <button :class="{
                            'btn btn-outline-danger mt-1': user.following,
                            'btn btn-outline-danger mt-1 disabled': !user.following,}"
                            @click="following_unfollow(user.username)">Unfollow</button>                
                    </td>
                </tr> 
            </tbody>
            </table>
        </div>

    </div>
</template>

<script>
export default {
data(){
    return{
        login_flag:false,
        username:"",
        search_list:[],
    }
},
methods:{
    check_login(){
      if (localStorage.getItem('auth_token')){
        this.login_flag=true
      }
    },

    search_user(){
            console.log(this.username)
            fetch(
            "http://127.0.0.1:5000/search_user?username="+this.username,
            {
            method: "GET",
            headers:{
                "Authentication-token":localStorage.getItem('auth_token'),
                "Content-Type":"application/json",
                "Access-Control-Allow-Origin": "*",
            },
            }).then(function(response) {
                return response.json()
                
            }).then((res) => {
                console.log(res)
                this.search_list = res;
                // this.$router.go()
            }).catch(function(error){
                console.log('error',error)
            });

        },
        follow_user(follow_username){
            console.log(follow_username)
            fetch(
            "http://127.0.0.1:5000/follow_user?follow_username="+follow_username,
            {
            method: "GET",
            headers:{
                "Authentication-token":localStorage.getItem('auth_token'),
                "Content-Type":"application/json",
                "Access-Control-Allow-Origin": "*",
            },
            }).then(function(response) {
                return response.json()
            }).then(() => {
                this.$router.go()
            }).catch(function(error){
                console.log('error',error)
            });

        },
        following_unfollow(unfollow_username){
            
            fetch(
            "http://127.0.0.1:5000/unfollow_user?unfollow_username="+unfollow_username,
            {
            method: "GET",
            headers:{
                "Authentication-Token":localStorage.getItem("auth_token"),
                "Content-Type":"application/json",
                "Access-Control-Allow-Origin": "*",
            },
        }).then(function(response) {
            return response.json()
        }).then(() => {
            this.$router.go()
        }).catch(function(error){
            console.log('error',error)
        });
        },
        
},

beforeMount(){
    this.check_login()
    }
}
</script>

<style>

</style>