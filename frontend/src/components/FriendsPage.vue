<template>
    <div class="div">
    <NavBar/>
    <!-- <h1 class="display-4">People you follow</h1><br> -->
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
                            'nav-link': !follower,}" href="#" @click="changetofollower">People you follow</a>
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
                            'nav-link': follower,}" href="#" @click="changefollower">Followers</a>
                </li> 
            </ul>
            
    </div>

        <div class="container " v-if="!follower">
            <table class="table table-dark table-striped">
                <tbody>
                <tr class="table mx-3" v-for="(followers,index) in followerslist" :key="index">
                    <th  class="text-center" scope="row">{{ index+1 }}</th>
                    <td colspan="5" class="fs-5 text-center"  style="word-wrap: break-word;min-width: 160px;max-width: 160px;">{{followers.name}}</td>
                    <td class="text-center">
                        <button class="btn btn-success mx-3 mt-1 " >Follow</button>
                        <button class="btn btn-outline-danger mt-1">Unfollow</button>                
                    </td>
                </tr> 
                </tbody>
                </table>
        </div>
        <div class="container " v-if="follower">
            <table class="table table-dark table-striped">
                <tbody>
                <tr class="table" v-for="(followers,index) in followerslist" :key="index">
                    <th  class="text-center" scope="row">{{ index+1 }}</th>
                    <td colspan="5" class="fs-5 text-center">{{followers.name}}</td>
                    <td class="text-center">
                        <button class="btn btn-danger mt-1">Unfollow</button>                
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
            follower: false,
            followerslist:[
                {name:"Harsh",type:"Following"},
                {name:"Dinesh",type:"Following"},
                {name:"Vikram",type:"Following"},
                {name:"Raj",type:"Following"},
                ]
        }
         
    },
    methods: {
            changefollower: function() {
                this.follower=false;
            },
            changetofollower: function() {
                this.follower=true;
            }   
        
       
    }



}
</script>

<style>

</style>