<template>
    <div class="div">
    <NavBar/>
    <!-- <h1 class="display-4">People you follow</h1><br> -->
    <div class="container text-center  mt-5 mb-5">
            <ul class="nav nav-tabs justify-content-center">
                <li class="nav-item">
                    <a 
                            :class="{
                            'nav-link active': follower,
                            'nav-link': !follower,
                            }"
                    @click="!follower" href="#">Followers</a>
                </li>
                <li class="nav-item">
                    <a 
                            :class="{
                            'nav-link active': !follower,
                            'nav-link': follower,
                            }"
                    @click="follower == false" href="#">Following</a>
                </li> 
            </ul>
            
    </div>
    
        <div class="container border border-primary" v-if="follower">
            <table class="table">
                <tbody>
                <tr>
                    <th scope="row">1.</th>
                    <td>Username</td>
                    <td>
                        <button class="btn btn-danger" type="button">Unfollow</button>
                    </td>
                </tr> 
                </tbody>
                </table>
        </div>

        <div class="container border border-primary" v-if="!follower">
            <table class="table">
                <tbody>
                <tr>
                    <th scope="row">1.</th>
                    <td>Following</td>
                    <td>
                        <button class="btn btn-success" type="button">Follow</button>
                        <button class="btn btn-danger" type="button">Unfollow</button>
                        
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
            follower: true,
        }
         
    },



}
</script>

<style>

</style>