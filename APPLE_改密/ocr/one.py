from flask import Flask, request
import ddddocr

ocr = ddddocr.DdddOcr(
    det=False,
    show_ad=False,
    ocr=False,
    import_onnx_path="APPLE_改密\ocr\A1.onnx",
    charsets_path="APPLE_改密\ocr\charsets.json",
)

app = Flask(__name__)

@app.route("/ocr", methods=["GET", "POST"])  # 添加 "POST"
def home():
    # 如果是GET请求，从查询参数中获取captcha
    # 如果是POST请求，从表单数据中获取captcha
    captcha = request.args.get("captcha") or request.form.get("captcha")
    
    if not captcha:
        return "No captcha data provided", 400  # 如果没有提供captcha，返回错误信息

    res = ocr.classification(captcha)
    return res

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8044)