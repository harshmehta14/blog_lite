<template>
  <div>
  <div class="container bigbox d-flex justify-content-center border align-items-center border-primary"> 
      <form @submit.prevent="login_token">
      <label for="email">Email:</label><br>
      <input v-model="email" type="text" required/><br>
  
      <label for="password">Password:</label><br>
      <input v-model="password" type="password" /><br><br> 

      <button class="btn btn-primary mx-2" >Signup-></button>
      <router-link class="btn btn-outline-success mx-2" to="/login" >Login</router-link>
      
     </form>  
  </div>
</div>

</template>

<script>
export default {

}
</script>

<style scoped>
  .bigbox{
    max-width: 600px;
    min-height: 600px;
  }
</style>