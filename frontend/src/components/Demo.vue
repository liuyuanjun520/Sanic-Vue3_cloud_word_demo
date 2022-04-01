<template>
  <div>

    <div id="word-text-area">

      <el-input type="textarea" :rows="10" placeholder="请输入内容" v-model="textarea"></el-input>


      <div id="word-img">
        <el-image :src="'data:image/png;base64,'+pic" fit="fill">
          <template v-slot:error>
            <i class="el-icon-picture-outline"></i>
          </template>
        </el-image>
      </div>


      <div id="word-operation">
        <el-row>
          <el-button type="primary" round @click="show_pic">生成</el-button>
          <el-button type="info" round @click="download_pic">下载</el-button>
        </el-row>
      </div>

    </div>



    </div>
</template>
<script>

import {  ref} from 'vue'
import {cloud_generate} from "../server/api_test";
export default {
    name:"demo",
    setup(){
      let pic = ref("no")
      let p_str = ref("")
      let textarea = ref("")

      //方法
      const show_pic = () =>{
        cloud_generate({word:textarea.value}).then(res=>{
          pic.value=res.data
        }).catch(()=>{
          console.log('catch')
        })
      }
      const download_pic = ()=>{
        p_str.value = ""
      }

      return {
        pic,
        p_str,
        textarea,
        show_pic,
        download_pic
      }
    }
}
</script>

<style scoped>
#word-text-area {
  margin-left: 20%;
  margin-right: 20%;
}
#word-operation {
  margin-top: 20px;
}
#word-img {
  width: 800px;
  height: 300px;
  margin: 20px;
}
</style>
