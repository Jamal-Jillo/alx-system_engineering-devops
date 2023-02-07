# Application Server

## Description

I had a few problems starting upt the application server. I had to do the following:
After cloning my Airbnb_clone_v2 repository on web-01 server. I had to configure  the file web_flask/0-hello_route.py to serve its content from the route /airbnb-onepage/ on port 5000.
But I still had problems starting my flask app. with this error:

```bash
ubuntu@62305-web-01:~/AirBnB_clone_v2/web_flask$ python3 0-hello_route.py
* Serving Flask app '0-hello_route'
 * Debug mode: off
Address already in use
Port 5000 is in use by another program. Either identify and stop that program, or start the server with a different port.
```

I tried running ```lsof -i :5000``` to see what was using port 5000. But I didnt get any output indicating that port 5000 was not in use. So I tried running ```sudo lsof -i :5000``` and I got the following output:

```bash
ubuntu@62305-web-01:~/AirBnB_clone_v2/web_flask$ sudo lsof -i :5000
COMMAND  PID     USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
agent   1970 dd-agent    8u  IPv4  36124      0t0  TCP localhost:5000 (LISTEN)
```

This showed that I had a process running on this port. The USER was 'dd-agent'. Which was probably a datadog agent.
So I tried stopping the datadog agent with ```sudo kill 1970```. My flask app was now running on port 5000.

```bash
ubuntu@62305-web-01:~/AirBnB_clone_v2/web_flask$ python3 0-hello_route.py
 * Serving Flask app '0-hello_route'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```
