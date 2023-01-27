<template>
  <div>
    <NavBar/>
     
      <div class="container d-flex justify-content-center">
        <div class="row bigbox ">
        
          <div class="col align-self-center">
          
            <div class="row text-center mt-5">
              <h1>Create an account</h1>
            </div>
             <div v-show="flag" class="alert alert-danger my-3 mx-3 text-center" role="alert">
              Username or Email is already taken.
            </div>
            <div class="row">
              <form @submit.prevent="signup_backend">
                <!-- <div class="row">
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
                </div> -->
                <div class="form-floating mb-3">
                  <input  v-model="username" type="text" class="form-control" placeholder="username" required/>
                  <label for="floatingInput">Username</label>
                </div>
                <div class="form-floating mb-3">
                  <input  v-model="email" type="email" class="form-control" placeholder="Email" required/>
                  <label for="floatingInput">Email address*</label>
                </div>
                <div class="form-floating">
                  <input v-model="password" type="password" class="form-control" minlength="8" placeholder="Password" required/>
                  <label for="floatingPassword">Password*</label><br>
                </div>
                <button  class="btn btn-primary w-100 btn-md" >Create account</button>
              </form>
            </div>
            <div class="row text-center">
              <router-link to="/login">Already have an account? Log in here</router-link>
            </div>
            <!-- <p>username: {{username}}</p>
            <p>email: {{email}}</p>
            <p>password: {{password}}</p>
               -->
          </div>

        </div>
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
          username:"",
          // lname:"",
          // fname:"",
          flag:false
      }      
  },
  methods : {
          signup_backend() {  
          fetch(
              "http://127.0.0.1:5000/signup",
              {
              method: "POST",
              headers:{
                  "Content-Type":"application/json",
                  "Access-Control-Allow-Origin": "*",
              },
              body: JSON.stringify({
              "username":this.username,
              "email": this.email,
              "password": this.password
          }),
              }
          ).then(function(response) {
              return response.json()
          }).then((rdata)=> {
              console.log(rdata)
              if (rdata.signup=="success"){
                this.$router.push({name:'home'})
              }
              else{
                this.flag=true
              }
              
          }).catch(function(error){
              this.flag=true
              console.log('error',error)
          });
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