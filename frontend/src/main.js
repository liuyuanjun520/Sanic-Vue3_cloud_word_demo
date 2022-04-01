import { createApp } from 'vue'
import App from './App.vue'
import ElementPlus from 'element-plus'
import 'element-ui/lib/theme-chalk/index.css'
import axios from './utils/request';
import router from './router'


const app = createApp(App)

//根据路由增加标题
router.beforeEach((to,from,next)=>{
    if(to.meta.title){
        document.title  = to.meta.title
    }
    next()
})

//全局ctx上挂载$axios
app.config.globalProperties.$api=axios
app.use(router)
app.use(ElementPlus)
app.mount('#app')
