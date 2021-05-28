package main

import (
	"context"

	greetpb "github.com/sevendollar/grpc/server-go/proto/greet"
)

// implementing the "GreetService" service
// /github.com.sevendollar.grpc.greet.GreetService
type GreetService struct{}

// implementing the "Ping" function of "GreetService" service
// /github.com.sevendollar.grpc.greet.GreetService/Ping
func (*GreetService) Ping(ctx context.Context, req *greetpb.PingRequest) (*greetpb.PingResponse, error) {
	return &greetpb.PingResponse{
		Message: "pong",
	}, nil
}

// implementing the "Hello" function of "GreetService" service
// /github.com.sevendollar.grpc.greet.GreetService/Hello
func (*GreetService) Hello(ctx context.Context, req *greetpb.HelloRequest) (*greetpb.HelloResponse, error) {
	return &greetpb.HelloResponse{
		Message: "hello, " + req.GetName(),
	}, nil
}
