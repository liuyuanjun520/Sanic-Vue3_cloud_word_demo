from sanic import Sanic, request, response
from wordcloud import WordCloud
import io
import base64
import jieba

app = Sanic(__name__)

# 加载静态文件，vue生成的静态文件
app.static('/static', '../frontend/dist/static')


@app.get('/')
async def index(request: request.Request):
    # 此处不加上await会出错
    # 渲染file
    return await response.file('../frontend/dist/index.html')


# 真正调用词云库生成图片
async def get_word_cloud(text):
    # 1.  worldcloud默认是不支持中文的，使用中文的字体使得能够支持中文
    font = r"SimHei.ttf"
    pil_img = WordCloud(width=800, height=300, font_path=font, background_color="white").generate(text=text).to_image()

    # 2. 默认方法：不支持中文
    # pil_img = WordCloud(width=800, height=300, background_color="white").generate(text=text).to_image()

    img = io.BytesIO()
    pil_img.save(img, "PNG")
    img.seek(0)
    img_base64 = base64.b64encode(img.getvalue()).decode()
    return img_base64


# 生成词云图片接口，以base64格式返回
@app.route('/word/cloud/generate', methods=["get"])
async def cloud(request: request.Request):
    import time
    last_time = time.time()
    text = request.args.get("word", None)
    if text:
        # 中文分词
        seg_list_exact = jieba.cut(text, cut_all=True)
        # 调用写好的生成云图的方法
        res = await get_word_cloud(" ".join(seg_list_exact))
        print(time.time()-last_time)
        return response.text(res)
    else:
        return response.text("no word")


if __name__ == '__main__':
    app.run(debug=True)
