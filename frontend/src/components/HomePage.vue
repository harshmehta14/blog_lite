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
<NavBar/>
  <div class="container-fluid text-center my-3">
  <div class="row">

    <div class="col-sm-8" >
      <div class="container  my-3">
          <nav class="nav nav-pills nav-justified">
          <a  :class="{'nav-link active': flag,
                       'nav-link': !flag,}" href="#" @click="changetofollower">All</a>
         
          <a class="nav-link" >Professional</a>
          <a class="nav-link ">Casual</a>
        </nav>
      </div>
          <div class="card mb-3" v-for="(blog,index) in blogs" :key="index">
            <div class="row g-0">
              <div class="col-md-4">


                <div class="ratio ratio-4x3">
                  <img src="../assets/loginpage.svg" alt=".." />
                  </div>

               

              </div>
              <div class="col-md-8">
                <div class="card-body">
                  <h5 class="card-title">{{ blog.title }}</h5>
                  <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                  <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
                </div>
              </div>
            </div>
          </div>
    </div>

    <div class="col-sm-4 mt-4">
      <div class="card text-start">
        <h4 class="card-header text-bg-info text-center">
          Trending
        </h4>
        <ul class="list-group list-group-flush"  v-for="(blog,index) in blogs" :key="index">
          <li class="list-group-item">
            <div class="card-body">

              <!-- <div style="display: flex; justify-content: space-between;"> -->
               <router-link to="/profile" style="color:darkblue; text-decoration: none;">
                <h6 class="card-title">@{{ blog.author }}</h6>
               </router-link> 
                
                
            
              <h4 class="card-subtitle" >{{blog.title}}</h4>
              <p class="card-text mt-2">With supporting text below as a natural lead-in to additional content.</p>
          
                <button class="btn btn-light fs-5" @click="blog.readtime++">
                {{ blog.readtime }} &nbsp; 
                <i class="bi bi-hand-thumbs-up text-primary" style="font-size: 20px;"></i>
                </button>

                
            
            </div>
        </li>
      </ul>
        <!-- <div class="card-footer text-muted">
          2 days ago
        </div> -->
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
    count:0,
    flag:true,
    
    blogs:[
      {title:"How to fix computer",summary:"this is how you will fix it in 60 words",date:'Sep 20',readtime:5,author:"login"},
      {title:"What is computer",summary:"Computer in 60 words",date:'Nov 20',readtime:10,author:"signup"},
      {title:"What is computer",summary:"Computer in 60 words",date:'Nov 20',readtime:10,author:"signup"},
      
      {title:"What is computer",summary:"Computer in 60 words",date:'Nov 20',readtime:10,author:"signup"},
    
      
    ]
  }
 }
}
</script>

<style scoped>
.blog-box{
  max-width: 600px;
  margin-left:40px;
}

</style>