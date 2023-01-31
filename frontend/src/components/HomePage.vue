<template>
  <!-- <div>
    <NavBar/>
    
    <div class="container-sm my-5 border border-primary blog-box" v-for="blog in blogs" :key="blog" >
      <router-link style="text-decoration: none; color: inherit;" :to= blog.author>
          <h3>{{blog.title}}</h3>
      <div class="mx-1">
        <p>{{ blog.summary }} </p>
        <p>{{blog.date}} &emsp; {{ blog.readtime }} min &emsp;{{ blog.author }}</p>
      </div> 
    </router-link>
  </div>
  </div> -->
  <!-- <div>
    <NavBar/>
    <div class="row">

      <div class="container-sm border border-primary  my-3">
       
       <div class="row">
     <div class="col-md-7 "  v-for="(blog,index) in blogs" :key="index">
       <div class="card my-2" >
         <div class="row">
           <div class="col-md-4 align-self-center ">
             <img src="../assets/loginpage.svg" class="img-fluid" alt="image">
           </div>
           <div class="col-md-8">
             <div class="card-body">
               <h5 class="card-title">{{blog.title}}</h5>
               <p class="card-text">aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
               <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
             </div>
           </div>
         </div>
       </div>
     </div>  

      
    
   </div>
   </div>

   <div class="container-sm border border-primary  my-3">
    
    <div class="row">
  <div class="col-md-7 "  v-for="(blog,index) in blogs" :key="index">
    <div class="card my-2" >
      <div class="row">
        <div class="col-md-4 align-self-center ">
          <img src="../assets/loginpage.svg" class="img-fluid" alt="image">
        </div>
        <div class="col-md-8">
          <div class="card-body">
            <h5 class="card-title">{{blog.title}}</h5>
            <p class="card-text">aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
            <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
          </div>
        </div>
      </div>
    </div>
  </div>  

   
 
</div>
</div>

    </div>
     
  </div> -->
<div class="div">
<NavBar  v-bind:login=login_flag />
  <div class="container-fluid text-center my-3">
  <div class="row">

    <div class="col-sm-8 " >
      <div class="container text-center my-4">
        <h1 class="display-4 alert alert-success">Welcome</h1>
      </div>
      <!-- <div class="container my-3 ">
          <nav class="nav nav-pills nav-justified ">
          <a :class="{'nav-link active': sort_flag === 1,
                       'nav-link': sort_flag !== 1,}" href="#" @click="sortposts(1)" >Latest</a>
          <a :class="{'nav-link active': sort_flag === 2,
                       'nav-link': sort_flag !== 2,}" href="#" @click="sortposts(2)">Top</a>
        </nav>
      </div> -->
      <div class="display-4 mt-5 mx-5" v-if="no_friend">
        <br/>
        <h1 class="display-3">Welcome to Blog Lite v2</h1><br/>
        <h1 class="display-4">Go ahead and connect with people to fill up you Home Page Wall</h1>
      </div>

      

          <div class="card mb-3" v-for="(blog,index) in user_blogs" :key="index">
            
      
            <div class="row g-0">
              <router-link to="/myprofile" style="text-decoration:none; color:inherit;">
                <h2 class="card-title mt-4">{{ blog.title }} </h2>
           
              </router-link>
              <div class="col-md-4 my-3 mx-3">


                <div class="ratio ratio-4x3">
                  <img src="../assets/loginpage.svg"   class="img-fluid"   />
                  </div>

                
              </div>
        
              <div class="col-md-7 my-3">
                <div class="card-body ">
                  
                <router-link to="/myprofile" style="text-decoration:none; color:inherit;">
                  <p class="card-text blockquote">{{ blog.description.slice(0,100) }}...</p>
                </router-link>

                  <div class="row align-items-center">  
                   
                 <div class="col-md-6">
                  <router-link to="/userprofile" style="color:darkblue; text-decoration: none;">
                  <h5 class="card-text">Posted By: @{{ blog.posted_by}}</h5>
                  </router-link>
                 </div>
                  <div class="col-md-6">
                    <h5 class="card-text">Likes 
                      <button class="btn btn-light fs-5" @click="blog_like(blog.blog_id)">
                          {{ blog.likes }} &nbsp; 
                        <i class="bi bi-hand-thumbs-up icon-magenta text-primary " style="font-size: 20px;"></i>
                      </button>
                    </h5>
                 </div>
                  </div><br/>
                 
                  <div class="col">
                      <p class="card-text fs-5"><small class="text-muted">{{ blog.posted_on.slice(0,-7)}}</small></p>
                    </div>
                </div>
              </div>
            </div>
            
      
          </div>
    </div>

    <div class="col-sm-4 mt-4">
      <div class="card text-start">
        <h3 class="card-header text-bg-dark text-center opacity-75">
          <i class="bi bi-pin-angle-fill"></i> Trending
        </h3>
        <ul class="list-group list-group-flush"  v-for="(blog,index) in trendingblogs" :key="index">
          
          <li class="list-group-item">
            <div class="card-body">
              <router-link to="/userprofile" style="color:inherit; text-decoration: none;">
              <!-- <div style="display: flex; justify-content: space-between;"> -->
               <router-link to="/myprofile" style="color:darkblue; text-decoration: none;">
                <h5 class="card-title">@{{ blog.posted_by }}</h5>
               </router-link> 
                
                
            
              <h4 class="card-subtitle" >{{blog.title}}</h4>
              <p class="card-text mt-2">{{ blog.description.slice(0,100)}}..</p>
            </router-link>
          
              <div class="row align-items-center">
                <div class="col-md-6">
                  <button class="btn btn-light fs-5" @click="blog_like(blog.blog_id)">
                      {{ blog.likes }} &nbsp; 
                    <i class="bi bi-hand-thumbs-up icon-magenta text-primary" style="font-size: 20px;"></i>
                   </button>
                </div>
                <div class="col-md-6">
                    <p class="card-text fs-5"><small class="text-muted">{{ blog.posted_on.slice(0,-7)}}</small></p>
                </div>

              </div>
               

                
            
            </div>
        </li>
   
      </ul>
      
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
    no_friend:false,
    sort_flag:0, 
    user_blogs:[],
    trendingblogs:[],
    login_flag:false,

  }
  },
  methods:{
    check_login(){
      if (localStorage.getItem('auth_token')){
        this.login_flag=true
      }
    },


    blog_like(blog_id){
      // console.log(blog_id);
      fetch(
        "http://127.0.0.1:5000/like_post?blog_id="+blog_id,
        {
        method: "GET",
        headers:{
            "Authentication-token":localStorage.getItem("auth_token"),
            "Content-Type":"application/json",
            "Access-Control-Allow-Origin": "*",
        },
      }).then(function(response) {
        return response.json()
      }).then((res) => {
        console.log(res);
        this.$router.go()
        
      }).catch(function(error){
          console.log('error',error)
      });
    },
   
    // sortposts(flag){
    //   // console.log(flag)
    //   if (flag === 1){
    //     this.user_blogs = this.user_blogs.sort(function (x, y) { 
    //         return Date(x) - Date(y)
          
    //             // var a = new Date(var1), b = new Date(var2);
    //             //   if (a > b)
    //             //     return 1;
    //             //   if (a < b)
    //             //     return -1;
    //             //   return 0;
    //           });
    //     // console.log(user_blogss)
    //     this.sort_flag = 1;
    //   }
    //   else if(flag === 2){
    //     this.user_blogs.sort((a, b) => parseFloat(b.likes) - parseFloat(a.likes));
    //     this.sort_flag=2;
    //   }
    // },
    // sortbytime(flag){
    //   if (flag==3 && this.user_blogs!==null){
    //     if(this.copy_user_blogs.length == 0){this.copy_user_blogs = this.user_blogs.slice();}
    //     this.user_blogs.sort((a, b) => parseFloat(b.likes) - parseFloat(a.likes));
    //   }
    //   else if (flag==2 && this.user_blogs!==null){
    //     if(this.copy_user_blogs.lenght == 0){this.copy_user_blogs = this.user_blogs.slice();}
    //     this.user_blogs.sort((a, b) => (a.posted_on) > (b.posted_on));
    //     console.log(this.user_blogs)
    //   }
    //   else if (flag==1 && this.user_blogs!==null){
    //     this.user_blogs = this.copy_user_blogs
    //   }
   
    // },

    getblogs(){
      fetch(
        "http://127.0.0.1:5000/getblogs",
        {
        method: "GET",
        headers:{
            "Authentication-token":localStorage.getItem("auth_token"),
            "Content-Type":"application/json",
            "Access-Control-Allow-Origin": "*",
        },
      }).then(function(response) {
        return response.json()
      }).then((blogspost) => {
        // console.log(blogspost)
          if (blogspost.length == 0){
            this.no_friend=true;
          }
          else{
           blogspost.forEach(item => this.user_blogs.push(item));
          } 
      }).catch(function(error){
          console.log('error',error)
      });
    }, 

    
    gettrendingblogs(){
      fetch("http://127.0.0.1:5000/gettrendingblogs",{
        method: "GET",
        headers:{
            "Content-Type":"application/json",
            "Access-Control-Allow-Origin": "*",
        },
      }).then(function(response) {
        return response.json()
      }).then((trendingblogs) => {
          // console.log(trendingblogs)
          trendingblogs.forEach(item => this.trendingblogs.push(item));
      }).catch(function(error){
          console.log('error',error)
      });

    }  
    },
    beforeMount(){
          this.getblogs()
          this.gettrendingblogs()
          this.check_login()
        }
}
</script>

<style scoped>
.blog-box{
  max-width: 600px;
  margin-left:40px;
}

</style>