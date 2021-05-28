package main

import (
	"context"
	"fmt"
	"log"

	"google.golang.org/grpc"

	greetpb "github.com/sevendollar/grpc/client-go/proto/greet"
)

func main() {
	const (
		grpcDial = ":50051"

		// argument for GraceService.HelloRequest.Name
		name = "Jef"
	)

	// create a gRPC client connection
	conn, err := grpc.Dial(grpcDial, grpc.WithInsecure())
	if err != nil {
		log.Fatal(err)
	}
	// close the gRPC client connection before exit
	defer conn.Close()

	ctx := context.Background()

	// create a GreetService client
	c := greetpb.NewGreetServiceClient(conn)

	// test out the gRPC service jonnectivity
	if _, err := c.Ping(ctx, &greetpb.PingRequest{}); err != nil {
		log.Fatal(err)
	}

	// call Hell function of GreetService service
	helloResp, err := c.Hello(ctx, &greetpb.HelloRequest{
		Name: name,
	})
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(helloResp.GetMessage())
}
