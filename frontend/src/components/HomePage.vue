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
  <div>
    <NavBar/>
      <div class="container text-center">
        <div class="row gy-2 gx-3">
          <div class="col-md-7 border border-primary" >
            <div class="p-3">Custom column padding1</div>
          </div>
          <div class="col-4 border border-primary">
            <div class="p-3">Custom column padding2</div>
          </div>
          <div class="col-6 border border-primary">
            <div class="p-3">Custom column padding3</div>
          </div>
          <div class="col-6 border border-primary">
            <div class="p-3">Custom column padding4</div>
          </div>
        </div>
      </div>

  </div>
 
</template>

<script>
export default {
 data(){
  return{
    blogs:[
      {title:"How to fix computer",summary:"this is how you will fix it in 60 words",date:'Sep 20',readtime:5,author:"login"},
      {title:"What is computer",summary:"Computer in 60 words",date:'Nov 20',readtime:10,author:"signup"},
      {title:"What is computer",summary:"Computer in 60 words",date:'Nov 20',readtime:10,author:"signup"}
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