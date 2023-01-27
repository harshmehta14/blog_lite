<template>
  <div>
    <NavBar/>
    <h1 class="display-3 text-center mt-3">My Posts</h1>
    <div class="container">
        <div class="row" >
           <div class="col-md-3"  v-for="(blog,index) in myblogs" :key="index" >
                <div class="card my-3 " style="min-height:350px;">
                <img src="../assets/download.png" class="card-img-top" alt="...">
                <div class="card-body">
                    <h5 class="card-title">{{blog.title}}</h5>
                    <p class="card-text">{{ blog.description.slice(0, 100) }}</p>
                    <p class="card-text text-muted">{{ blog.posted_on }}</p>
                    <div class="footer">
                        <a href="#" class="btn btn-info mx-4"><i class="bi bi-pencil-fill"></i> Edit</a>
                    <a href="#" class="btn btn-outline-danger"><i class="bi bi-trash3-fill"></i> Delete</a>
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
    username:"test123",
    
    myblogs:[
      // {title:"How to fix computer",summary:"this is how you will fix it in 60 words",date:'Sep 20',readtime:5,author:"login"},
      // {title:"What is computer",summary:"Computer in 60 words",date:'Nov 20',readtime:10,author:"signup"},
      // {title:"What is computer",summary:"Computer in 60 words",date:'Nov 20',readtime:10,author:"signup"},
      // {title:"What is computer",summary:"Computer in 60 words",date:'Nov 20',readtime:10,author:"signup"},
      // {title:"What is computer",summary:"Computer in 60 words",date:'Nov 20',readtime:10,author:"signup"},
      // {title:"What is computer",summary:"Computer in 60 words",date:'Nov 20',readtime:10,author:"signup"},
      // {title:"What is computer",summary:"Computer in 60 words",date:'Nov 20',readtime:10,author:"signup"},
      
     
    
      
    ]
  }
 },
 methods:{
  getuserposts(){
      fetch(
        "http://127.0.0.1:5000/getuserposts?username="+this.username,
        {
        method: "GET",
        headers:{
            "Content-Type":"application/json",
            "Access-Control-Allow-Origin": "*",
        },
      }).then(function(response) {
        return response.json()
      }).then((myblogs) => {
          // console.log(myblogs[0])
          myblogs.forEach(item => this.myblogs.push(item));
      }).catch(function(error){
          console.log('error',error)
      });
    }, 
  },
  beforeMount(){
    this.getuserposts()
  }

}
</script>

<style scoped>
 .footer {
    /* position: absolute; */
    bottom: 10px;
}

</style>