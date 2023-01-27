<template>
  <div class="login-signup">
    <NavBar/>
     
      <div class="container d-flex justify-content-center">
        <div class="row bigbox ">
        
          <div class="col align-self-center">
          
            <div class="row text-center mx-3">
              <h1>Log into Blog Lite</h1>
            </div>
             <div v-show="flag" class="alert alert-danger my-3 mx-5 text-center" role="alert">
              Invalid Credintial
            </div>
            <div class="row">
              <form @submit.prevent="login_token">
                <div class="form-floating mb-3">
                  <input  v-model="email" type="email" class="form-control" id="floatingInput" placeholder="Email" required>
                  <label for="floatingInput">Email address</label>
                </div>
                <div class="form-floating">
                  <input v-model="password" type="password" class="form-control" id="floatingPassword" placeholder="Password" required>
                  <label for="floatingPassword">Password</label><br>
                </div>
                <button class="btn btn-primary w-100 btn-md" >Login</button>
              </form>
            </div>
            <div class="row text-center">
              <router-link to="/signup">Don't have an account</router-link>
            </div>
              
          </div>

        </div>
      </div>
  </div>
  </template>
  
  <script>

  export default{
      data(){
          return{
              email:"",
              password:"",
              flag:false
          }      
      },
      methods : {
          login_token() {     
              fetch(
                  "http://127.0.0.1:5000/login",
                  {
                  method: "POST",
                  headers:{
                      "Content-Type":"application/json",
                      "Access-Control-Allow-Origin": "*",
                  },
                  body: JSON.stringify({
                  "email": this.email,
                  "password": this.password
              }),
                  }
                  ).then(function(response) {
                      return response.json()
                  }).then((rdata)=> {
                      console.log(rdata);
                      if (rdata.login == "success")
                        this.$router.push({name:'home'})
                      else{
                        this.flag = true;
                      }
                  }).catch(function(error){
                      console.log('error',error)
                  });
              // ).then(res =>{
              //     return res.json();
                  
              // }).then(data=> {
              //     if(data.token){
              //         localStorage.setItem('token', data.token);
              //         this.welcome="Welcome "+data.user
              //         localStorage.setItem('user', data.user);
              //     }
              //     else{
              //         this.msg= data.data;
              //     }
              //     }).catch(function(error){
              //     console.log('error',error)
              // });
          }
      }
  }
  </script>
  
  <style scoped>
  .bigbox{
    max-width: 600px;
    min-width: 400px;
    min-height: 600px;
    /* padding: 1px 2px; */
    
  }
  .row{
    padding: 16px 16px;
  }
  .alert {
  margin-bottom: 1px;
  height: 40px;
  line-height:40px;
  padding:0px 15px;
  }
  /* .login-signup{
    background-image: url(../assets/loginpage.svg);
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-position: left bottom; 
    background-size: 20rem 20rem;
  } */

  input {
  /* background-color: grey; */
  /* border: grey;
  color: white; */
  padding: 16px 10px;
  /* text-decoration: none; */
  /* margin: 4px 2px; */
  cursor: pointer;
  width: 100% ;
  height:20%;
}

  </style>