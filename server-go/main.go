package main

import (
	"log"
	"net"
	"os"
	"os/signal"
	"syscall"

	"google.golang.org/grpc"
	"google.golang.org/grpc/reflection"

	greetpb "github.com/sevendollar/grpc/server-go/proto/greet"
)

const listenPort = "50051"

func main() {
	// create a TCP listener
	lis, err := net.Listen("tcp", ":"+listenPort)
	if err != nil {
		log.Fatal(err)
	}
	// close the listener before exit
	defer lis.Close()

	// create a gRPC server
	srv := grpc.NewServer(
		grpc.ChainUnaryInterceptor(logger),
	)

	// registe gRPC services to gRPC server
	greetpb.RegisterGreetServiceServer(srv, &GreetService{})

	// reflect the gRPC services(use for development purposes)
	reflection.Register(srv)

	log.Println("starting gRPC server...")
	go func() {
		// run gRPC server
		log.Println("gRPC server is running...")
		if err := srv.Serve(lis); err != nil {
			log.Fatal(err)
		}
	}()

	// listen to interrups from system
	quit := make(chan os.Signal, 1)
	signal.Notify(quit, syscall.SIGINT, syscall.SIGTERM)
	<-quit
	log.Println("receiving interrupt from system...")

	// gracefully shutdown the gRPC server
	log.Println("gRPC server is shutting down...")
	srv.GracefulStop()
	log.Println("gRPC server has shutdowned")

}
