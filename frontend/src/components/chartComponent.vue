<template>  
    <div>
        <canvas id="myChart"></canvas>
    </div>
    
</template>

<script>
import Chart from 'chart.js/auto'
export default {
  
    data(){
        return{
          label:['Tuesday', 'Monday', 'Sunday', 'Saturday', 'Friday'],
          data:[1,2,3,4,5],   
        }
    },
    methods:{
       getchartdata(){
          fetch(
              "http://127.0.0.1:5000/getchartdata",
              {
              method: "GET",
              headers:{
                  "Authentication-Token":localStorage.getItem("auth_token"),
                  "Content-Type":"application/json",
                  "Access-Control-Allow-Origin": "*",
              },

            }).then(function(response) {
              return response.json()
            }).then((res) => { 
                console.log(res)
                
                this.label = res.label
                this.data = res.data
                // if(user_data.profile){
                // this.total_posts=user_data.total_posts;
                // this.followers=user_data.followers;
                // this.following=user_data.following;
                // this.profile_username=user_data.username;
                // this.email=user_data.email;
                // this.last_login=user_data.last_login;
              
                // }
                // else{
                //     console.log(user_data)
                // }
                // this.$router.push({name:'home'})
            }).catch(function(error){
                console.log('error',error)
            });

          
        
      },
      chart(){
        console.log(this.data)
        const ctx = document.getElementById('myChart');
        
        const mychart =  new Chart(ctx, {
             type: 'bar',
             data: {
               labels:this.label,
               datasets: [{
                 label: '# No of Posts',
                 data: this.data,
                 borderWidth: 1
               }]
             },
             options: {
               scales: {
                 y: {
                   beginAtZero: true
                 }
               }
             }
           });
           mychart; 
          }
    },
    async created(){
      await fetch(
              "http://127.0.0.1:5000/getchartdata",
              {
              method: "GET",
              headers:{
                  "Authentication-Token":localStorage.getItem("auth_token"),
                  "Content-Type":"application/json",
                  "Access-Control-Allow-Origin": "*",
              },
            }).then(function(response) {
              return response.json()
            }).then((res) => { 
                console.log(res)
                this.label = res.label
                this.data = res.data
            }).catch(function(error){
                console.log('error',error)
            });
     
     },
     mounted(){
      this.chart();
      
     
        }
      }
</script>

<style>

</style>