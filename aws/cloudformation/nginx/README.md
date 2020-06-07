# NGINX - Reverse Proxy, Web Server

Nginx is a lightweight, multipurpose server that can be used as a web server, reverse proxy, or load balancer, inter alia. It handles connections asynchronously and can handle as many connections as the underlying machine can support, in contrast to an Apache web server, which can only handle a pre-configured number of connections at a time. When an Nginx host has reached its maximum capacity, new incoming connections will be queued and handled when resources are filled up, instead of dropped.

This folder contains a Cloudformation template and an example parameter file to create an Nginx server.

## Documentation

Nginx documentation can be found in two places:
- [nginx.org](https://nginx.org)
- [nginx.com](https://nginx.com)

## Usage

Create a stack
```SHELL
aws cloudformation create-stack \
--stack-name nginx \
--template-body file://nginx-server.yml \
--parameters file://nginx-server-parameters.json \
--region=us-east-1
```

Update a stack
```SHELL
aws cloudformation update-stack \
--stack-name nginx \
--template-body file://nginx-server.yml \
--parameters file://nginx-server-parameters.json \
--region=us-east-1
```

When you're done, delete the stack
```SHELL
aws cloudformation delete-stack \
--stack-name nginx
```

## Resources
### Online Courses on Nginx
- [NGINX Fundamentals: High Performance Servers from Scratch](https://www.udemy.com/course/nginx-fundamentals/)
- [Full Node.js Deployment - NGINX, SSL With Lets Encrypt](https://www.youtube.com/watch?v=oykl1Ih9pMg)
- [Nginx Official Tutorials](https://www.youtube.com/watch?v=X3Pr5VATOyA&list=PLGz_X9w9raXf748bzuGOV6XJv7q3wLxhZ)

### Books on Nginx
- [NGINX Cookbook: Over 70 recipes for real-world configuration, deployment, and performance](https://www.amazon.com/gp/product/1786466171/)
- [Nginx HTTP Server - Fourth Edition: Harness the power of Nginx to make the most of your infrastructure and serve pages faster than ever before](https://www.amazon.com/Nginx-HTTP-Server-Harness-infrastructure/dp/178862355X/)
- [Nginx Essentials: Excel in Nginx quickly by learning to use its most essential features in real-life applications](https://www.amazon.com/Nginx-Essentials-Valery-Kholodkov/dp/1785289535/)

### Linux Reference for Managing Nginx
- [How To Use Systemctl to Manage Systemd Services and Units](https://www.digitalocean.com/community/tutorials/how-to-use-systemctl-to-manage-systemd-services-and-units)