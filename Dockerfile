FROM golang:alpine as builder
WORKDIR /app
COPY . .
RUN  CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -a -installsuffix cgo -ldflags="-w -s" -o /go/bin/zombiestorm .

FROM scratch
VOLUME /tmp
VOLUME /data
WORKDIR /root/
COPY --from=builder /go/bin/zombiestorm /go/bin/zombiestorm
COPY commit.id commit.id
EXPOSE 8080
ENTRYPOINT ["/go/bin/zombiestorm"]
