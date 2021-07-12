package main

//import "time"
import "os/exec"
import "log"
import "fmt"
//import "os/signal"
//import "syscall"
//import "runtime"

func main() {

    //signal.Ignore(syscall.SIGCHLD)
    makezombie();
    forever()
}

func makezombie(){

theCmd,err := exec.Command("/bin/sleep","3").Output()
if err != nil {
        log.Fatal(err)
    }
fmt.Println(theCmd)


}

func forever() {
    for {
        //runtime.Gosched()
    }
}
