<template>
  <div>
    <NavBar  v-bind:login=true />
    <h1 class="display-3 text-center mt-3">My Posts</h1>

    <div class="container" v-if="empty_post">
      <h1 class="display-4 mt-5 mx-5 text-center">You have no posts</h1>

    </div>
    <div class="container" v-if="!empty_post">
        <div class="row" >
           <div class="col-md-3"  v-for="(blog,index) in myblogs" :key="index" >
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
                  
                    <div class="footer">
                      <router-link to="editpost" class="btn btn-info mx-4">
                        <i class="bi bi-pencil-fill"></i> Edit
                      </router-link>
                    <a href="#" class="btn btn-outline-danger" @click="Delete_userpost(blog.blog_id)"><i class="bi bi-trash3-fill"></i> Delete</a>
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
    empty_post:true,
    myblogs:[]
  }
 },
 methods:{
  Get_userpost(){
      fetch(
        "http://127.0.0.1:5000/crud_user_post",
        {
        method: "GET",
        headers:{
            "Authentication-Token": localStorage.getItem("auth_token"),
            "Content-Type":"application/json",
            "Access-Control-Allow-Origin": "*",
        },
      }).then(function(response) {
        return response.json()
      }).then((myblogs) => {
          console.log(myblogs)
          if (myblogs.length == 0){
              console.log(myblogs.length)
          }
          else{
            this.empty_post=false
            myblogs.forEach(item => this.myblogs.push(item));
          }
        
          
      }).catch(function(error){
          console.log('error',error)
      });
    }, 

    Delete_userpost(blog_id){
      console.log(blog_id)
      fetch(
        "http://127.0.0.1:5000/crud_user_post?blog_id="+blog_id,
        {
        method: "DELETE",
        headers:{
            "Authentication-Token": localStorage.getItem("auth_token"),
            "Content-Type":"application/json",
            "Access-Control-Allow-Origin": "*",
        },
      }).then(function(response) {
        return response.json()
      }).then((res) => {
          if(res.delete == "success"){
            this.$router.go()  
          }
          else{
            alert("Failed to delete it ")
          }
          // if (myblogs.length == 0){
          //     console.log(myblogs.length)
          // }
          // else{
          //   this.empty_post=false
          //   myblogs.forEach(item => this.myblogs.push(item));
          // }
      }).catch(function(error){
          console.log('error',error)
      });
  },
},
beforeMount(){
    this.Get_userpost()
  }
}
</script>

<style scoped>
 .footer {
    /* position: absolute; */
    bottom: 10px;
}

</style>