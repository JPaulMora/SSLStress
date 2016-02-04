# SSLStress

Python script to stress SSL handshakes on server.

## Demo

In the demo below, the colorful terminal window was my Apache server while my CPU and little terminal window show the activity from the client side. You can see pretty easily how the CPU bar in the server terminal rises at the same time the apache process rises to the top of the list. All without moving my client CPU a pixel in that graph.

![demo gif](https://github.com/JPaulMora/SSLStress/blob/master/sslpoc.gif?raw=true)

## Contribute

Currently, this project needs threading support and a way to agree the most "expensive" protocol for the handshake, consuming more resources from the server. If you feel like adding any of these please submit a pull request.
