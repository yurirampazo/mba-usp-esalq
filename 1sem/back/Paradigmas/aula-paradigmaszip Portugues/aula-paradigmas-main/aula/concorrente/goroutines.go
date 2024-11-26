package main

import(
	"fmt"
	"time"
)

func trabalho(nome string) {
	fmt.Println(nome, "iniciou")
	time.Sleep(2 * time.Second)
	fmt.Println(nome, "finalizou")
}


func main() {

	go trabalho("goroutinne 1")
	go trabalho("goroutinne 2")

    time.Sleep(3 * time.Second)
	fmt.Println("todos os jobs foram finalizados")

}