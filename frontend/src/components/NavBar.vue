<template>
  <nav class="navbar navbar-expand-lg bg-body-tertiary" style="background-color: #e3f2fd;">
  <div class="container-fluid">
    <router-link class="navbar-brand" to="/">Project</router-link>
    <div class="collapse navbar-collapse" id="navbarTogglerDemo03">
      <ul class="navbar-nav ms-auto">
        <li class="nav-item mx-2">
          <router-link class="nav-link active " to="/">Something</router-link>
        </li>
        <li class="nav-item mx-2">
          <!-- <a class="nav-link active" aria-current="page" href="#">Home</a> -->
          <router-link class="btn btn-success " to="/login">Log In</router-link>
        </li>   
        <li class="nav-item mx-2">
          <router-link class="btn btn-outline-primary" to="/signup">Sign Up</router-link>
        </li>
      </ul>
    </div>

  </div>
</nav>
</template>

<script>
export default {

}
</script>

<style>

</style>