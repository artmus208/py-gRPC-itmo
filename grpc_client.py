import grpc
from protobufs import glossary_pb2, glossary_pb2_grpc

class GlossaryClient:
    def __init__(self, host='localhost', port=50051):
        self.channel = grpc.insecure_channel(f"{host}:{port}")
        self.stub = glossary_pb2_grpc.GlossaryControllerStub(self.channel)

    def get_glossary(self):
        try:
            response = self.stub.GetAllTerms(glossary_pb2.Empty())
            return {term.name: term.description for term in response.terms}
        except grpc.RpcError as e:
            print(f"gRPC error: {e}")
            return {}

    def add_term(self, name, description):
        try:
            request = glossary_pb2.Term(name=name, description=description)
            response = self.stub.AddTerm(request)
            return response.success, response.message
        except grpc.RpcError as e:
            print(f"gRPC error: {e}")
            return False, str(e)
