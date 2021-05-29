import grpc
import greet_pb2_grpc
import greet_pb2

# create a connection channel
chan = grpc.insecure_channel("localhost:50051")

# create a GreetService service connection
greetServiceStub = greet_pb2_grpc.GreetServiceStub(chan)

# call the Ping function of GreetService service
pingResp = greetServiceStub.Ping(greet_pb2.PingRequest())
print(pingResp.message)

# call the Hello function of GreetService service
helloStub = greetServiceStub.Hello(greet_pb2.HelloRequest(name="Python"))
print(helloStub.message)
