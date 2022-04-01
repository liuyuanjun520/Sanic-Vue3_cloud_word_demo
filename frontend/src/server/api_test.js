//权限管理API
import request from "../utils/request";

export function cloud_generate(param){
    return request({
        url:"/word/cloud/generate",
        method:'get',
        params:param
        })
}
