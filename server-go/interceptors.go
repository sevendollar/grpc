package main

import (
	"context"
	"log"

	"google.golang.org/grpc"
)

// implementing the gRPC Unary Interceptor
func logger(ctx context.Context, req interface{}, info *grpc.UnaryServerInfo, handler grpc.UnaryHandler) (resp interface{}, err error) {
	log.Printf("---> Unary interceptor: %v\n", info.FullMethod)
	return handler(ctx, req)
}
