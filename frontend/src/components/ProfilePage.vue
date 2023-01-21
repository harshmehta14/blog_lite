<template>
    <div>
        <NavBar/>
        <div class="container-fluid shadow-lg p-3 mb-5 bg-body rounded">
            <div class="row justify-content-center">
                <div class="col-md-2 mx-2 ">                   
                    <div class="card my-3 mx-2 bg-light" style="width: 13rem;">
                        <div class="card-body">
                            <span>
                                <h3 class="card-title text-center text-muted"> 
                                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-person-lines-fill" viewBox="0 0 16 16">
                                    <path d="M6 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm-5 6s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1H1zM11 3.5a.5.5 0 0 1 .5-.5h4a.5.5 0 0 1 0 1h-4a.5.5 0 0 1-.5-.5zm.5 2.5a.5.5 0 0 0 0 1h4a.5.5 0 0 0 0-1h-4zm2 3a.5.5 0 0 0 0 1h2a.5.5 0 0 0 0-1h-2zm0 3a.5.5 0 0 0 0 1h2a.5.5 0 0 0 0-1h-2z"/>
                                    </svg> Total Posts
                                </h3>
                                
                            </span>
                         
                            <!-- <h6 class="card-subtitle mb-2 text-muted">Card subtitle</h6> -->
                            <h4 class="card-title text-center">10</h4>                          
                        </div>
                        </div>
                </div>
                <div class="col-md-2 mx-2 ">                   
                    <div class="card my-3 mx-2 bg-light" style="width: 13rem;">
                        <div class="card-body">
                            <h3 class="card-title text-center text-muted">Followed by</h3>
                            <!-- <h6 class="card-subtitle mb-2 text-muted">Card subtitle</h6> -->
                            <h4 class="card-title text-center">194</h4>                          
                        </div>
                        </div>
                </div>
                <div class="col-md-2 mx-2">                   
                    <div class="card my-3 mx-2 bg-light" style="width: 13rem;">
                        <div class="card-body">
                            <h3 class="card-title text-center text-muted">Following</h3>
                            <!-- <h6 class="card-subtitle mb-2 text-muted">Card subtitle</h6> -->
                            <h4 class="card-title text-center">205</h4>                          
                        </div>
                        </div>
                </div>
                <!-- <div class="col-md-2 mx-2">                   
                    <div class="card my-3 mx-2" style="width: 13rem;">
                        <div class="card-body">
                            <h3 class="card-title text-center">Followers</h3>
                            <h4 class="card-title text-center">194</h4>                          
                        </div>
                        </div>
                </div> -->
            </div> 
        </div>
        <h1 class="display-3 text-center">My Profile</h1>
        <div class="container-fluid bcontent shadow-lg p-3 mb-5 bg-body rounded" >
        <div class="card border-0">
            <div class="row no-gutters">
                <div class="col-sm-5">
                    <img class="card-img" src="../assets/loginpage.svg" style="padding:10px 10px" alt="">
                </div>
                <div class="col-sm-7"> 
                    <div class="card-body">
                        <p class="card-title"><span style="font-weight:bold">First Name: </span> Harsh</p>
                        <hr>
                        <p class="card-title"><span style="font-weight:bold">Last Name:  </span> Mehta</p>
                        <hr>
                        <p class="card-title"><span style="font-weight:bold">Username: </span> harshmehta14</p>
                        <hr>
                        <p class="card-title"><span style="font-weight:bold">Email: </span> test@test.com</p>
                        <hr>
                        <p class="card-title"><span style="font-weight:bold">Last Login: </span>12th Sep 2022</p>
                        <hr>
                        <!-- <p class="card-text">Suresh Dasari is a founder and technical lead developer in tutlane.</p> -->
                        <!-- <a href="#" class="btn btn-primary">View Profile</a> -->
                    </div>
                </div>
            </div>
        </div>
    </div>

    <h1 class="display-3 text-center">My Post</h1>
        


    </div>
  
</template>

<script>
export default {

}
</script>

<style>

</style>