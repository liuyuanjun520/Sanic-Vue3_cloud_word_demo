import {createRouter,createWebHashHistory} from 'vue-router'

//此处用于引入需要用到的组件
import Demo from "../components/Demo";

export default createRouter({
    //此处用于说明是history模式(没有#),还是hash模式(有#)
    history:createWebHashHistory(),
    //此处用于定义需要用到的路由，以及嵌套路由等
    routes:[
        {
            path:'/',
            component:Demo,
            meta:{
                title:"Cloud_Word"
            }
        }
    ]
})
