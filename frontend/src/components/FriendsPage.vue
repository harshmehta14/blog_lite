<template>
    <div class="div">
    <NavBar/>
    <div class="container text-center  mt-5 mb-5">
            <ul class="nav nav-tabs justify-content-center">
                <li class="nav-item">
                    <!-- <a 
                            :class="{
                            'nav-link active': follower,
                            'nav-link': !follower,
                            }"
                    @click="!follower" href="#">Followers</a> -->
                    <a  :class="{
                            'nav-link active': follower,
                            'nav-link': !follower,}" href="#" @click="changetofollower"><h3>Following</h3> <span class="badge text-bg-primary">{{ total_following }}</span></a>
                </li>
                <li class="nav-item">
                    <!-- <a 
                            :class="{
                            'nav-link active': !follower,
                            'nav-link': follower,
                            }"
                    @click="follower == false" href="#">Following</a> -->
                    <a  :class="{
                            'nav-link active': !follower,
                            'nav-link': follower,}" href="#" @click="changefollower"><h3>Followers</h3> <span class="badge text-bg-primary">{{ total_followers }}</span></a>
                </li> 
            </ul>
            
    </div>

        <div class="container " v-if="!follower">
            <table class="table table-dark table-striped">
                <thead>
                    <tr>
                    <th class="text-center"  scope="col"><h5>#</h5></th>
                    <th class="text-center"  colspan="5" scope="col"><h5>Username</h5></th>
                    <th class="text-center"  scope="col"><h5>Options</h5></th>
                    </tr>
                </thead>
                <tbody>
                <tr class="table mx-3" v-for="(followers,index) in followerslist" :key="index">
                    <th  class="text-center" scope="row">{{index+1  }}</th>
                    <td colspan="5" class="fs-5 text-center"  style="word-wrap: break-word;min-width: 160px;max-width: 160px;">@{{followers.username}}</td>
                    <td class="text-center">
                        <button  :class="{
                            'btn btn-success mx-3 mt-1': !followers.following,
                            'btn btn-success mx-3 mt-1 disabled': followers.following,}" 
                            @click="follow_user(followers.username)">Follow</button>
                        <button :class="{
                            'btn btn-outline-danger mt-1': followers.following,
                            'btn btn-outline-danger mt-1 disabled': !followers.following,}"
                            @click="following_unfollow(followers.username)">Unfollow</button>                
                    </td>
                </tr> 
                </tbody>
                </table>
        </div>
        <div class="container " v-if="follower">
            <table class="table table-dark table-striped">
                <thead>
                    <tr>
                    <th class="text-center"  scope="col"><h5>#</h5></th>
                    <th class="text-center"  colspan="5" scope="col"><h5>Username</h5></th>
                    <th class="text-center"  scope="col"><h5>Options</h5></th>
                    </tr>
                </thead>
                <tbody>
                <tr class="table" v-for="(item,index) in followinglist" :key="index">
                    <td  class="text-center" scope="row">{{ index+1 }}</td>
                    <td colspan="5" class="fs-5 text-center">@{{item}}</td>
                    <td class="text-center">
                        <button  class="btn btn-danger mt-1" @click="following_unfollow(item)">Unfollow</button>                      
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
           
            follower: true,
            // followerslist:[
            //     {name:"Harsh",type:"Following"},
            //     {name:"Dinesh",type:"Following"},
            //     {name:"Vikram",type:"Following"},
            //     {name:"Raj",type:"Following"},
            //     ]
            followerslist:[],
            followinglist:[],
            total_followers:0,
            total_following:0,
        }
         
    },
    methods: {
        follow_user(follow_username){
            console.log(follow_username)
            fetch(
            "http://127.0.0.1:5000/follow_user?follow_username="+this.follow_username,
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
        changefollower: function() {
            this.follower=false;
        },
        changetofollower: function() {
            this.follower=true;
        }, 
        getfriendslist(){
        fetch(
            "http://127.0.0.1:5000/getfriendslist",
            {
            method: "GET",
            headers:{
                "Authentication-token":localStorage.getItem("auth_token"),
                "Content-Type":"application/json",
                "Access-Control-Allow-Origin": "*",
            },
        }).then(function(response) {
            return response.json()
        }).then((friendslist) => {
            // friendslist.followers.forEach(item => this.followerslist.push(item));
            friendslist.followers.forEach(item => this.followerslist.push(item));
            friendslist.following.forEach(item => this.followinglist.push(item));
            this.total_followers = this.followerslist.length
            this.total_following = this.followinglist.length
            // console.log(this.followerslist)
        }).catch(function(error){
            console.log('error',error)
        });
        }, 
      
    },
    beforeMount(){
          this.getfriendslist()
        }
        
       
    }
</script>

<style>

</style>