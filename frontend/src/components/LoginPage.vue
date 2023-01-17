<template>
<div>
  <div class="container bigbox d-flex justify-content-center border align-items-center border-primary"> 
      <form @submit.prevent="login_token">
      <label for="email">Email:</label><br>
      <input v-model="email" type="text" required/><br>
  
      <label for="password">Password:</label><br>
      <input v-model="password" type="password" /><br><br> 

      <button class="btn btn-primary mx-2" >Login</button>
      <router-link class="btn btn-outline-success mx-2" to="/signup" >Sign Up</router-link>
     
   
     </form>
      
      
  </div>

</div>
    

  
  
  <!-- <p>email: {{email}}</p>
  <p>password: {{password}}</p>
  <p>msg:{{msg}}</p> -->


 
  </template>
  
  <script>

  export default{
      data(){
          return{
              email:"",
              password:"",
              msg:"",
              welcome:""
          }      
      },
  //     methods : {
  //         login_token() {     
  //             fetch(
  //                 "http://127.0.0.1:5000/login",
  //                 {
  //                 method: "POST",
  //                 headers:{
  //                     "Content-Type":"application/json",
  //                     "Access-Control-Allow-Origin": "*",
  //                 },
  //                 body: JSON.stringify({
  //                 "email": this.email,
  //                 "password": this.password
  //             }),
  //                 }
  //             ).then(res =>{
  //                 return res.json();
                  
  //             }).then(data=> {
  //                 if(data.token){
  //                     localStorage.setItem('token', data.token);
  //                     this.welcome="Welcome "+data.user
  //                     localStorage.setItem('user', data.user);
  //                 }
  //                 else{
  //                     this.msg= data.data;
  //                 }
  //                 }).catch(function(error){
  //                 console.log('error',error)
  //             });
  //         }
  //     }
  }
  </script>
  
  <style scoped>
  .bigbox{
    max-width: 600px;
    min-height: 600px;
  }

  </style>