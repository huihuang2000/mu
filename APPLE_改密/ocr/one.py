from flask import Flask, request
import ddddocr
import asyncio

ocr = ddddocr.DdddOcr(
    det=False,
    show_ad=False,
    ocr=False,
    import_onnx_path="APPLE_改密\ocr\A1.onnx",
    charsets_path="APPLE_改密\ocr\charsets.json",
)

app = Flask(__name__)


@app.route("/ocr", methods=["GET", "POST"])
async def home():
    captcha = request.args.get("captcha") or request.form.get("captcha")
    if not captcha:
        return "未提供验证码文件", 400

    res = await asyncio.to_thread(ocr.classification, captcha)  # 异步执行 OCR
    return res

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8044)