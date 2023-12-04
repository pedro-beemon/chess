import onnx
onnx_model = onnx.load("model_.onnx")
onnx.checker.check_model(onnx_model)
