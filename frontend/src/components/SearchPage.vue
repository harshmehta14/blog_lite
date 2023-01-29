<template>
    <div class="div" >
        
    <NavBar v-bind:login=login_flag />
  

        <div class="container my-5" >
            <table class="table table-dark table-striped">
                <thead>
                <tr>
                <th class="text-center" scope="col"><h5>#</h5></th>
                <th class="text-center" colspan="5" scope="col"><h5>Username</h5></th>
                <th class="text-center" scope="col"><h5>Options</h5></th>
                </tr>
            </thead>
            <tbody>
            <tr class="table" v-for="(item,index) in followinglist" :key="index">
                <td  class="text-center" scope="row">{{ index+1 }}</td>
                <td colspan="5" class="fs-5 text-center">@{{item}}</td>
                <td class="text-center">
                    <button  class="btn btn-danger mt-1" @click="following_unfollow(item)">Unfollow</button>                      
                </td>
            </tr> 
            </tbody>
            </table>
        </div>

    </div>
</template>

<script>
export default {
data(){
    return{
        login_flag:false,
        
    }
},
methods:{
    check_login(){
      if (localStorage.getItem('auth_token')){
        this.login_flag=true
      }
    },

},
    beforeMount(){
            this.check_login()
            }
}
</script>

<style>

</style>