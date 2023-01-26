<template>
    <div>
        <NavBar/>
        <div class="container my-3">
            <form >
                <div class="title my-3 shadow p-3 mb-5 bg-body rounded">
                    <textarea type="text" class="form-control" rows="1" id="title" placeholder="Type in title for the Post here..."  v-model="title"  required />
                </div>
                <div class="mb-3 shadow p-3 mb-5 bg-body rounded">
                    <h4 class="form-label text-muted">Add image to support your post</h4>
                    <div class="ratio ratio-21x9 viewingimage border border-primary" :style="{'background-image': `url(${pimage})`}" @click="selectImage"> 
                    
                    </div>
                    <br/>
    
                    <input class="form-control form-control-sm" id="formFileSm" ref="fileInput" @input="pickFile" type="file" required>
                </div>

                <div class="subtitle my-4 shadow p-3 mb-5 bg-body rounded">
                    <textarea type="text" rows="10" class="form-control" id="subtitle" placeholder="Start typing you story here..."  v-model="description"  required />
                </div>

                <div class="additionallinks my-4 shadow p-3 mb-5 bg-body rounded">
                    <textarea type="text" rows="1" class="form-control" id="additionallinks" placeholder="Add links here (seperated by comma) ..."  v-model="additionallinks"  required />
                </div>
                
                <div class="alert alert-warning text-center" role="alert" v-if="check">
                    Please enter all the field before posting
                </div>
                <div class="d-flex justify-content-center">
                    <button type="button" class="btn btn-success btn-lg" @click="checkallfield">Post <i class="bi bi-check2-circle"></i></button>

                </div>
                

            </form>
            
        </div>
        

    </div>
</template>

<script>

export default {
data(){
    return{
        title:"",
        pimage:null,
        description:"",
        additionallinks:"",
        check:false,
    }
},
methods:{
    selectImage(){
        this.$refs.fileInput.click()

    },
    checkallfield(){
        if (this.title=="" || this.pimage==null || this.description==""){
            console.log("hello")
            this.check=true;
        }
        else{
            this.check=false
        }
    },
    pickFile(){
        let input = this.$refs.fileInput
        let file =input.files
        if(file && file[0]){
            let reader = new FileReader
            reader.onload = e =>{
                this.pimage = e.target.result
            }
            reader.readAsDataURL(file[0])
            this.$emit('input',file[0])
        }


    }
}
}
</script>

<style scoped>
.viewingimage{
    width: 100%;
    height: 300px;
    display: block;
    background-repeat:no-repeat ;
    cursor: pointer;
    margin: 10px auto 30px;
    background-size: cover;
    background-position: center center;
   
}
textarea[id=title] {
    background-color: none;
    border: none;
    /* color: white; */
    font-weight: bold;
    font-size: 50px ;
    padding: 16px 10px;
    text-decoration: none;
    margin: 4px 2px;
    cursor: pointer;
    /* width: 100% ; */
    /* height:10%; */
    text-align: center;
}
textarea[id=subtitle]{
    background-color: none;
    border: none;
    /* color: white; */
    font-size: 30px ;
    padding: 16px 10px;
    text-decoration: none;
    margin: 4px 2px;
    cursor: pointer;
    /* width: 100% ; */
    height:100%;
}

textarea[id=additionallinks] {
    background-color: none;
    border: none;
    /* color: white; */
    color: darkblue;
    padding: 16px 10px;
    text-decoration: none;
    margin: 4px 2px;
    cursor: pointer;
    /* width: 100% ; */
    height:100%;
}

</style>