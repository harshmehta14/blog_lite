<template>
    <div>
        <NavBar  v-bind:login=true />
        <div class="container-fluid shadow-lg p-3 mb-5 bg-body rounded">
            <div class="row justify-content-center">
                <div class="col-md-2 mx-2 ">                   
                    <div class="card my-3 mx-2 bg-light" style="width: 13rem;">
                        <div class="card-body">
                            <span>
                                <h3 class="card-title text-center text-muted"> 
                                     Total Posts
                                </h3>
                                
                            </span>
                         
                            <!-- <h6 class="card-subtitle mb-2 text-muted">Card subtitle</h6> -->
                            <h4 class="card-title text-center">{{ total_posts }}</h4>                          
                        </div>
                        </div>
                </div>
                <div class="col-md-2 mx-2 ">                   
                    <div class="card my-3 mx-2 bg-light" style="width: 13rem;">
                        <router-link to="/friends" style="text-decoration: none; color: inherit;">
                            <div class="card-body">
                            <h3 class="card-title text-center text-muted">Followers</h3>
                            <!-- <h6 class="card-subtitle mb-2 text-muted">Card subtitle</h6> -->
                            <h4 class="card-title text-center">{{followers}}</h4>                          
                        </div>

                        </router-link>
                        </div>
                </div>
                <div class="col-md-2 mx-2">                   
                    <div class="card my-3 mx-2 bg-light" style="width: 13rem;">
                        <router-link to="/friends" style="text-decoration: none; color: inherit;">
                        <div class="card-body">
                            <h3 class="card-title text-center text-muted">Following</h3>
                            <!-- <h6 class="card-subtitle mb-2 text-muted">Card subtitle</h6> -->
                            <h4 class="card-title text-center">{{following}}</h4>                          
                        </div>
                    </router-link>
                        </div>
                </div>
                <!-- <div class="col-md-2 mx-2">                   
                    <div class="card my-3 mx-2" style="width: 13rem;">
                        <div class="card-body">
                            <h3 class="card-title text-center">Followers</h3>
                            <h4 class="card-title text-center">194</h4>                          
                        </div>
                        </div>
                </div> -->
            </div> 
        </div>
        <h1 class="display-3 text-center">My Profile</h1>
        <div class="container-fluid bcontent shadow-lg p-3 mb-5 bg-body rounded " >
        <div class="card border-0">
            <div class="row no-gutters">
                <div class="col-sm-4">
                    <svg xmlns="http://www.w3.org/2000/svg" width="400" height="200" fill="currentColor" class="bi bi-person-circle" viewBox="0 0 16 16">
                    <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z"/>
                    <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z"/>
                    </svg>
                </div>
                <div class="col-sm-7"> 
                    <div class="card-body">
                        <!-- <p class="card-title"><span style="font-weight:bold">First Name: </span> Harsh</p>
                        <hr> -->
                        <!-- <p class="card-title"><span style="font-weight:bold">Last Name:  </span> Mehta</p>
                        <hr> -->
                        <p class="card-title"><span style="font-weight:bold">Username: </span> {{profile_username}}</p>
                        <hr>
                        <p class="card-title"><span style="font-weight:bold">Email: </span> {{email}}</p>
                        <hr>
                        <!-- <p class="card-title"><span style="font-weight:bold">Last Login: </span>{{last_login}}</p>
                        <hr> -->
                        <!-- <p class="card-text">Suresh Dasari is a founder and technical lead developer in tutlane.</p> -->
                        <!-- <a href="#" class="btn btn-primary">View Profile</a> -->
                    </div>
                </div>
            </div>
        </div>

        
        
    </div>
    <h1 class="display-4 text-center mt-5">Insights - My Posts</h1>
        <div class="container my-5">
            <chart ></chart>
        </div>
    


    </div>
  
</template>

<script>
import chart from './chartComponent.vue';
export default {
  components: { chart },
    data(){
        return{
            total_posts:0,
            followers:0,
            following:0,
            profile_username:"",
            email:"",
            last_login:"",
        }
    },
    methods:{
        profile() {
    
          fetch(
              "http://127.0.0.1:5000/profile",
              {
              method: "GET",
              headers:{
                  "Authentication-Token":localStorage.getItem("auth_token"),
                  "Content-Type":"application/json",
                  "Access-Control-Allow-Origin": "*",
              },
            //   body: JSON.stringify({
            //   "title":this.title,
            //   "description": this.description,
            //   "links": this.additionallinks,
            //   "username":"test123"
            // }),
            }).then(function(response) {
              return response.json()
            }).then((user_data) => { 
                if(user_data.profile){
                this.total_posts=user_data.total_posts;
                this.followers=user_data.followers;
                this.following=user_data.following;
                this.profile_username=user_data.username;
                this.email=user_data.email;
                this.last_login=user_data.last_login;
              
                }
                else{
                    console.log(user_data)
                }
                // this.$router.push({name:'home'})
            }).catch(function(error){
                console.log('error',error)
            });
    }

    },
    beforeMount(){
        this.profile()

    }

}
</script>

<style>

</style>