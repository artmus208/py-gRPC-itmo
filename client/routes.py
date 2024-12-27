import grpc
import sys
import traceback

from flask import Blueprint, redirect, render_template, request, url_for
from flask import current_app




from grpc_client import GlossaryClient
from protobufs import glossary_pb2
from protobufs import  glossary_pb2_grpc


# Инициализация gRPC-клиента
grpc_client = GlossaryClient()

bp = Blueprint('routes', __name__)


@bp.route('/', methods=['GET'])
def index():
    try:
        glossary = grpc_client.get_glossary()
        return render_template('index.html', glossary=glossary)
    except grpc.RpcError as e:
        tb = sys.exc_info()[2]
        handler_name = traceback.format_tb(tb)[0]
        current_app.logger.exception(handler_name)
        return render_template("index.html")

# Роут для добавления термина через gRPC
@bp.route('/add', methods=['POST'])
def add_term():
    name = request.form.get('name')
    description = request.form.get('description')
    if name and description:
        success, message = grpc_client.add_term(name, description)
        if success:
            return redirect(url_for('routes.index'))
        return f"Ошибка: {message}", 400
    return "Ошибка: необходимо заполнить оба поля.", 400
    
    

    
# @app.route('/glossary/update', methods=['PUT'])
# def update_term():
#     data = request.json
#     term = glossary_pb2.Term(name=data.get("name"), description=data.get("description"))
#     try:
#         response = stub.UpdateTerm(term)
#         return jsonify({"success": response.success, "message": response.message})
#     except grpc.RpcError as e:
#         return jsonify({"error": f"gRPC Error: {e.details()}"}), grpc.StatusCode.INTERNAL
    
    
# @app.route('/glossary/delete', methods=['DELETE'])
# def delete_term():
#     data = request.json
#     term_request = glossary_pb2.TermRequest(name=data.get("name"))
#     try:
#         response = stub.DeleteTerm(term_request)
#         return jsonify({"success": response.success, "message": response.message})
#     except grpc.RpcError as e:
#         return jsonify({"error": f"gRPC Error: {e.details()}"}), grpc.StatusCode.INTERNAL

# @app.route('/get', methods=['GET'])
# def get_glossary():
#     try:
#         render_template(
#             "index.html",
#             data = glossary
#         )
#     except:
#         tb = sys.exc_info()[2]
#         handler_name = traceback.format_tb(tb)[0]
#         app.logger.exception(handler_name)
#         return render_template("index.html")
