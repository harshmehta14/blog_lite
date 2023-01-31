<template>
  <!-- <nav class="navbar navbar-expand-lg bg-body-tertiary" style="background-color: #e3f2fd;">
  <div class="container-fluid">
    <router-link class="navbar-brand" to="/">Project</router-link>
    <div class="collapse navbar-collapse" id="navbarTogglerDemo03">
      <ul class="navbar-nav ms-auto">
        <li class="nav-item mx-2">
          <router-link class="nav-link active " to="/">Something</router-link>
        </li>
        <li class="nav-item mx-2">
          <router-link class="nav-link active " to="/profile">Profile</router-link>
        </li>
        <li class="nav-item mx-2">
          <router-link class="btn btn-success " to="/login">Log In</router-link>
        </li>   
        <li class="nav-item mx-2">
          <router-link class="btn btn-outline-primary" to="/signup">Sign Up</router-link>
        </li>
      </ul>
    </div>

  </div>
</nav> -->
<nav class="navbar navbar-expand-sm navbar-dark bg-dark">
        <div class="container-fluid">
          <a class="navbar-brand me-5" href="/"><h6 class="display-6">Project</h6></a>
      
          
          <!-- <form class="d-flex" role="search">
                <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search" v-model="username">
             <router-link to="/search/"><button class="btn btn-outline-success" @click="gotosearchpage" >Search</button></router-link>   
          </form> -->

   
          
          <button class="navbar-toggler my-2" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav ms-auto">
              <li class="nav-item px-2">
                <router-link to="/search"  class="nav-link active"><i class="bi bi-search"></i> Search</router-link>
              </li>
              <!-- <li class="nav-item px-2" >
                <router-link to="/myposts"  class="nav-link active">My Posts</router-link>
              </li>
              <li class="nav-item px-2" >
                <router-link to="/profile"  class="nav-link active">My Profile</router-link>
              </li> -->
              
              <li class="nav-item mx-2 my-1" >
                <router-link to="/createpost" class="btn btn-primary" >Post Now</router-link>
              </li>
              <li>
              <div class="dropdown mx-2 my-1 me-5" v-if="login">
                <button class="btn btn-success dropdown-toggle" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
                 Welcome
                </button>
                <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
                <!-- <p class="dropdown-item">Welcome </p>
                <div class="dropdown-divider"></div> -->
                <li><router-link class="dropdown-item" to="/myprofile"><i class="bi bi-person-circle"></i> My Profile</router-link></li>
                <li><router-link class="dropdown-item" to="/myposts"><i class="bi bi-card-text" fill="red"></i> My Posts</router-link></li>
                <div class="dropdown-divider"></div>
                <li><router-link class="dropdown-item" @click="logout()" to="/login"><i class="bi bi-box-arrow-right"></i> Logout</router-link></li>
                </ul>
              </div>
              
              </li>
              <li class="nav-item px-2 mt-1" v-if="!login">
                <router-link to="/login" class="btn btn-success" >Login</router-link>
              </li>
              <li class="nav-item px-2 me-3 mt-1" v-if="!login">
                <router-link to="/signup" class="btn btn-outline-primary" >Signup</router-link>
              </li>
              

             
              <!-- <li class="nav-item px-2 " v-if="!login">
                <router-link to="/signup" class="btn btn-outline-danger">Log out  &nbsp;<i class="bi bi-box-arrow-right"></i></router-link>
              </li> -->
            </ul>

          </div>  
          </div>
  
      </nav>
      



</template>

<script>
export default {
  props:['login'],
  data(){
    return{
      username:"",
          
    }
  },
  methods:{
    gotosearchpage(){
      console.log(this.username)
      this.$router.push({name: "search", params:{id : this.username} })
    },
    logout(){
      localStorage.removeItem('auth_token')
    }
  }

}
</script>

<style>

</style>