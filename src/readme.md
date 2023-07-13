# How to start
1. Install dependencies with init.sh
2. Run server
```
./init.sh
./run.sh
```
Oneliner to send a message with curl:
`curl -X POST "https://api.telegram.org/botXXX:YYYY/sendMessage" -d "chat_id=-zzzzzzzzzz&text=my sample text"`