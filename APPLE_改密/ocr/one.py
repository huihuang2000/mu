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

@app.route('/ocr', methods=['GET'])
def home():

    captcha = request.args.get('captcha', default=None, type=str)
    res = ocr.classification(captcha)
    return res

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8044)