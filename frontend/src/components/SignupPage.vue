<template>
  <div class="login-signup">
    <NavBar/>
     
      <div class="container d-flex justify-content-center">
        <div class="row bigbox ">
        
          <div class="col align-self-center">
          
            <div class="row text-center mt-5">
              <h1>Create an account</h1>
            </div>
             <div v-show="flag" class="alert alert-danger my-3 mx-3 text-center" role="alert">
              Password should more than 8 characters
            </div>
            <div class="row">
              <form @submit.prevent="login_token">
                <div class="row">
                  <div class="col-6 ">
                      <div class="form-floating mb-3">
                        <input  v-model="fname" type="text" class="form-control" id="floatingInput" placeholder="fname" required>
                        <label for="floatingInput">First Name</label>
                       </div>
                  </div>
                  <div class="col-6">
                    <div class="form-floating mb-3">
                        <input  v-model="lname" type="text" class="form-control" id="floatingInput" placeholder="lname" required>
                        <label for="floatingInput">Last Name</label>
                       </div>
                  </div>
                </div>
                <div class="form-floating mb-3">
                  <input  v-model="email" type="email" class="form-control" id="floatingInput" placeholder="Email" required>
                  <label for="floatingInput">Email address*</label>
                </div>
                <div class="form-floating">
                  <input v-model="password" type="password" class="form-control" id="floatingPassword" placeholder="Password" required>
                  <label for="floatingPassword">Password*</label><br>
                </div>
                <button type="button" class="btn btn-primary w-100 btn-md" >Create account</button>
              </form>
            </div>
            <div class="row text-center">
              <router-link to="/login">Already have an account? Log in here</router-link>
            </div>
              
          </div>

        </div>
      </div>

  </div>

  
  
  <!-- <p>email: {{email}}</p>
  <p>password: {{password}}</p>
  <p>msg:{{msg}}</p> -->
  </template>

<script>
export default {
  data(){
          return{
              email:"",
              password:"",
              lname:"",
              fname:"",
              flag:false
          }      
      },
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
    padding: 10px 10px;
  }
  .alert {
  margin-bottom: 1px;
  height: 40px;
  
  line-height:40px;
  padding:0px 10px;
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
  /* padding: 16px 10px; */
  /* text-decoration: none; */
  /* margin: 4px 2px; */
  cursor: pointer;
  width: 100% ;
  height:20%;
}
</style>