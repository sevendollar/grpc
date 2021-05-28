const grpc = require('@grpc/grpc-js');
const protoLoader = require('@grpc/proto-loader');

const PROTO_PATH = __dirname + '/proto/greet/greet.proto';

// Loading service descriptors from proto files 
const packageDefinition = protoLoader.loadSync(
    PROTO_PATH,
    {keepCase: true,
     longs: String,
     enums: String,
     defaults: true,
     oneofs: true
    });

// The protoDescriptor object has the full package hierarchy
const protoDescriptor = grpc.loadPackageDefinition(packageDefinition);

// get the namespace <- package github.com.sevendollar.grpc.greet;
const greet = protoDescriptor.github.com.sevendollar.grpc.greet;

// create a GreetService service connection
const greetServiceClient = new greet.GreetService(
        "192.168.16.95:50051",
        grpc.credentials.createInsecure())

// call the Ping function of GreetService service
greetServiceClient.Ping({}, (err, resp) => {
        if (err) {
                console.log(err)
        }
        console.log(resp.message)
})

// call the Hello function of GreetService service
greetServiceClient.Hello({name: "Jef"}, (err, resp) => {
        if (err) {
                console.log(err)
        }
        console.log(resp.message)
})