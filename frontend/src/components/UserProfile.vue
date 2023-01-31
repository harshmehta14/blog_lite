<template>
  <div class="div">
    <NavBar />
    <h1 class="display-3 text-center my-3">{{ (this.$route.params.username).toUpperCase().slice(0,1) + (this.$route.params.username).toLowerCase().slice(1)}}'s Profile</h1>
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
                        <!-- <router-link to="/friends" style="text-decoration: none; color: inherit;"> -->
                            <div class="card-body">
                            <h3 class="card-title text-center text-muted">Followers</h3>
                            <!-- <h6 class="card-subtitle mb-2 text-muted">Card subtitle</h6> -->
                            <h4 class="card-title text-center">{{followers}}</h4>                          
                        </div>
                        <!-- </router-link> -->
                        </div>
                </div>
                <div class="col-md-2 mx-2">                   
                    <div class="card my-3 mx-2 bg-light" style="width: 13rem;">
                        <!-- <router-link to="/friends" style="text-decoration: none; color: inherit;"> -->
                        <div class="card-body">
                            <h3 class="card-title text-center text-muted">Following</h3>
                            <!-- <h6 class="card-subtitle mb-2 text-muted">Card subtitle</h6> -->
                            <h4 class="card-title text-center">{{following}}</h4>                          
                        </div>
                    <!-- </router-link> -->
                        </div>
                </div>
            </div> 
        </div>
        <h1 class="display-3 text-center my-3">{{ (this.$route.params.username).toUpperCase().slice(0,1) + (this.$route.params.username).toLowerCase().slice(1) }}'s Posts</h1>

        <div class="container" >
        <div class="row" >
           <div class="col-md-3"  v-for="(blog,index) in posts" :key="index" >
                <div class="card my-3 " style="min-height:350px;">
                <img src="../assets/download.png" class="card-img-top" alt="...">
                <div class="card-body">

                  <div class="row align-items-center">
                    <div class="col-md-8">
                      <h5 class="card-title">{{blog.title}}</h5>
                    </div>
                    <div class="col-md-4">
                    <button :class="{'btn btn-success btn-sm ': !blog.private_public,
                                      'btn btn-primary btn-sm': blog.private_public,
                                    }">
                                    {{ blog.private_public==false ? "Public" :"Private"}}</button>
                    </div>
                  </div>
                    
                    <p class="card-text">{{ blog.description.slice(0, 100) }}</p>
                    <div class="row">
                      <div class="col-md-8">
                        <p class="card-text text-muted">{{ blog.posted_on.slice(0,-7) }}</p>

                      </div>
                      <div class="col-md-4">
                        <p>{{ blog.likes }} &nbsp; <i class="bi bi-hand-thumbs-up icon-magenta text-primary"></i></p>
                      </div>
                    </div>
                  
                </div>
                </div>
            </div>
        </div>
            
        </div>
            


        
  </div>
 
</template>

<script>
export default {
  data(){
    return{
      total_posts:0,
      followers:0,
      following:0,
      posts:[],
     
    }
  },
  methods:{
    userprofile() {
    fetch(
        "http://127.0.0.1:5000/userprofile?username="+this.$route.params.username,
        {
        method: "GET",
        headers:{
            "Authentication-Token":localStorage.getItem("auth_token"),
            "Content-Type":"application/json",
            "Access-Control-Allow-Origin": "*",
        },
      }).then(function(response) {
        return response.json()
      }).then((user_data) => { 
        console.log(user_data)
          if(user_data.profile){
          this.total_posts=user_data.total_posts;
          this.followers=user_data.followers;
          this.following=user_data.following;
          user_data.posts.forEach(item => this.posts.push(item));
          // this.profile_username=user_data.username;
          // this.email=user_data.email;
          // this.last_login=user_data.last_login;
        
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
        this.userprofile()
    }
}
</script>

<style>

</style>